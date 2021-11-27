from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF 

g = Graph()
g.bind("foaf", FOAF)

ani = URIRef("http://facebookontology.org/ani")
g.add((ani, RDF.type, FOAF.Person))
g.add((ani, FOAF.nick, Literal("ani")))
g.add((ani, FOAF.name, Literal("Ani Hani")))

budi = URIRef("http://facebookontology.org/budi")
g.add((budi, RDF.type, FOAF.Person))
g.add((budi, FOAF.nick, Literal("budi")))
g.add((budi, FOAF.name, Literal("Budi Wicaksono")))

bob = URIRef("http://facebookontology.org/bob")
g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.nick, Literal("bobby")))
g.add((bob, FOAF.name, Literal("Bobby Dong")))

g.add((ani, FOAF.knows, budi))
g.add((budi, FOAF.knows, bob))

print("-----------------")
test_query = """
SELECT DISTINCT ?aname ?bname
WHERE {
    ?a foaf:knows ?b .
    ?a foaf:name ?aname .
    ?b foaf:name ?bname .
}"""

qry = g.query(test_query)
for x in qry:
    print(f"{x.aname} knows {x.bname}")