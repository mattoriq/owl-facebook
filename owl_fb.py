from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF 

g = Graph()

owl_uri = "http://facebookontology.org/"

#object property
friend_with = URIRef('http://facebookontology.org/friend_with')
member_of = URIRef('http://facebookontology.org/member_of')

# sample data (person)
ani = URIRef('http://facebookontology.org/ani')
g.add((ani, RDF.type, FOAF.Person))
g.add((ani, FOAF.nick, Literal("ani")))
g.add((ani, FOAF.name, Literal("Ani Hani")))

budi = URIRef('http://facebookontology.org/budi')
g.add((budi, RDF.type, FOAF.Person))
g.add((budi, FOAF.nick, Literal("budi")))
g.add((budi, FOAF.name, Literal("Budi Wicaksono")))

bob = URIRef('http://facebookontology.org/bob')
g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.nick, Literal("bobby")))
g.add((bob, FOAF.name, Literal("Bobby Dong")))

ali = URIRef('http://facebookontology.org/ali')
g.add((ali, RDF.type, FOAF.Person))
g.add((ali, FOAF.nick, Literal("ali")))
g.add((ali, FOAF.name, Literal("Ali Dali")))

# sample data (friends relation)
g.add((ani, friend_with, budi))
g.add((budi, friend_with, bob))
g.add((budi, friend_with, ali))

# sample data (group)
chess_group = URIRef('http://facebookontology.org/chess_group')
g.add((chess_group, RDF.type, FOAF.Group))
g.add((chess_group, FOAF.name, Literal("Chess Group")))

# sample data (membership)
g.add((ani, member_of, chess_group))
g.add((ali, member_of, chess_group))

#bind for querying
g.bind("foaf", FOAF)
g.bind("rdf", RDF)

friend_query = """
SELECT DISTINCT ?aname ?bname
WHERE {
    ?a <http://facebookontology.org/friend_with> ?b .
    ?a foaf:name ?aname .
    ?b foaf:name ?bname .
}"""

all_names_query = """
SELECT DISTINCT ?name
WHERE {
    ?a rdf:type foaf:Person .
    ?a foaf:name ?name .
}"""

group_member_query = """
SELECT ?name ?group
WHERE {
    ?n rdf:type foaf:Person .
    ?g rdf:type foaf:Group .
    ?n <http://facebookontology.org/member_of> ?g .
    ?n foaf:name ?name .
    ?g foaf:name ?group .
}"""

all_groups_query = """
SELECT DISTINCT ?group
WHERE {
    ?g rdf:type foaf:Group .
    ?g foaf:name ?group . 
}"""

print("-----------------")

def print_all_names():
    qry = g.query(all_names_query)
    for x in qry:
        print(f"{x.name}")

def print_all_groups():
    qry = g.query(all_groups_query)
    for x in qry:
        print(f"{x.group}")

def print_friends():
    qry = g.query(friend_query)
    for x in qry:
        print(f"{x.aname} is friend with {x.bname}")

def print_memberships():
    qry = g.query(group_member_query)
    for x in qry:
        print(f"{x.name} is a member of {x.group}")