from owl_fb import *

def app():
    while(True):
        str = """
1. Tambah instance orang
2. Tambah instance group
3. Lihat daftar orang
4. Lihat daftar group
5. Lihat daftar pertemanan
6. Lihat daftar membership
7. Tambah pertemanan
8. Tambah membership
9. Exit
Anda memilih: """
        choice = input(str)
        if(choice == "1"):
            str_nick = input("Nama panggilan: ")
            str_name = input("Nama panjang: ")
            person = URIRef(owl_uri + str_nick)
            g.add((person, RDF.type, FOAF.Person))
            g.add((person, FOAF.nick, Literal(str_nick)))
            g.add((person, FOAF.name, Literal(str_name)))

        elif(choice == "2"):
            str_group = input("Nama grup: ")
            str_group_uri = str_group.lower().replace(" ","_")
            group = URIRef(owl_uri + str_group_uri)
            g.add((group, RDF.type, FOAF.Group))
            g.add((group, FOAF.name, Literal(str_group)))

        elif(choice == "3"):
            print_all_names()

        elif(choice == "4"):
            print_all_groups()

        elif(choice == "5"):
            print_friends()

        elif(choice == "6"):
            print_memberships()

        elif(choice == "7"):
            person_one = input("Nickname orang pertama: ")
            person_two = input("Nickname orang kedua: ")
            person_one_uri = URIRef(owl_uri + person_one.lower())
            person_two_uri = URIRef(owl_uri + person_two.lower())
            g.add((person_one_uri, friend_with, person_two_uri))

        elif(choice == "8"):
            person = input("Nickname orang: ")
            group = input("Nama grup: ")
            person__uri = URIRef(owl_uri + person.lower())
            group_uri = URIRef(owl_uri + group.lower().replace(" ","_"))
            g.add((person__uri, FOAF.member, group_uri))

        elif(choice == "9"):
            print("Exiting...")
            break

        else:
            print("Invalid")

if __name__ == '__main__':
    app()