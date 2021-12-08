from rdflib import Graph, Literal, RDF, URIRef, RDFS
from rdflib.namespace import FOAF, OWL
import time

g = Graph()

owl_uri = "http://facebookontology.org/"

#object property
friend_with = FOAF.knows
member_of = FOAF.member
posted = URIRef('http://facebookontology.org/posted')
is_tagging = URIRef('http://facebookontology.org/is_tagging')
liked = URIRef('http://facebookontology.org/liked')
friend_with = URIRef('http://facebookontology.org/friend_with')

# sample data (person)
ani = URIRef('http://facebookontology.org/ani')
g.add((ani, RDF.type, FOAF.Person))
g.add((ani, FOAF.nick, Literal("ani")))
g.add((ani, FOAF.name, Literal("Ani Hani")))

budi = URIRef('http://facebookontology.org/budi')
g.add((budi, RDF.type, FOAF.Person))
g.add((budi, FOAF.nick, Literal("budi")))
g.add((budi, FOAF.name, Literal("Budi Wicaksono")))

bob = URIRef('http://facebookontology.org/bobby')
g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.nick, Literal("bobby")))
g.add((bob, FOAF.name, Literal("Bobby Dong")))

ali = URIRef('http://facebookontology.org/ali')
g.add((ali, RDF.type, FOAF.Person))
g.add((ali, FOAF.nick, Literal("ali")))
g.add((ali, FOAF.name, Literal("Ali Dali")))

# sample data (friends relation)
g.add((ani, friend_with, ali))
g.add((bob, friend_with, ali))
g.add((budi, friend_with, bob))
g.add((budi, friend_with, ani))
g.add((budi, friend_with, ali))
g.remove((budi, friend_with, ali))

# sample data (group)
chess_group = URIRef('http://facebookontology.org/chess_group')
g.add((chess_group, RDF.type, FOAF.Group))
g.add((chess_group, FOAF.name, Literal("Chess Group")))

# sample data (membership)
g.add((chess_group, member_of, ani))
g.add((chess_group, member_of, ali))

# sample data (image)
gambar_pantai = URIRef('http://facebookontology.org/gambar_pantai')
g.add((gambar_pantai, RDF.type, FOAF.Image))
g.add((gambar_pantai, FOAF.name, Literal("Gambar Pantai")))
g.add((budi, posted, gambar_pantai))
g.add((gambar_pantai, is_tagging, ani))
g.add((gambar_pantai, is_tagging, bob))
g.add((gambar_pantai, is_tagging, ali))
g.add((ani, liked, gambar_pantai))

#bind for querying
g.bind("foaf", FOAF)
g.bind("rdf", RDF)

friend_query = """
SELECT ?aname ?bname
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
    ?g foaf:member ?n .
    ?n foaf:name ?name .
    ?g foaf:name ?group .
}"""

all_groups_query = """
SELECT DISTINCT ?group
WHERE {
    ?g rdf:type foaf:Group .
    ?g foaf:name ?group . 
}"""

unresponsive_person_query = """
SELECT ?img ?poster ?tagged
WHERE {
    ?p <http://facebookontology.org/posted> ?i .
    ?i <http://facebookontology.org/is_tagging> ?t .
    ?p <http://facebookontology.org/friend_with> ?t .
    FILTER NOT EXISTS { ?t <http://facebookontology.org/liked> ?i } .
    ?i foaf:name ?img .
    ?p foaf:name ?poster .
    ?t foaf:name ?tagged .
}"""

def print_all_names():
    print("-----------------")
    qry = g.query(all_names_query)
    for x in qry:
        print(f"{x.name}")

def print_all_groups():
    print("-----------------")
    qry = g.query(all_groups_query)
    for x in qry:
        print(f"{x.group}")

def print_friends():
    print("-----------------")
    qry = g.query(friend_query)
    for x in qry:
        print(f"{x.aname} is friend with {x.bname}")

def print_memberships():
    print("-----------------")
    start = time.time()
    qry = g.query(group_member_query)
    for x in qry:
        print(f"{x.name} is a member of {x.group}")
    end = time.time()
    print(end - start)

def print_custom_query():
    print("-----------------")
    qry = g.query(unresponsive_person_query)
    for x in qry:
        print(f"Uploader gambar: {x.poster}, Gambar: {x.img}, Orang yang ditag: {x.tagged}")

print_friends()
print_custom_query()
print_memberships()
