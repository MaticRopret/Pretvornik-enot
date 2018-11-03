# -*- encoding: utf-8 -*- #

print "Pozdravljeni v aplikaciji pretvarjanja enot, natančneje iz kilometrov v milje. "

mile = float ( 0.621371192 )

while True:
    convert = raw_input ( "Vnesite število kilometrov: ")

    print "Rezultat željene pretvorbe je: " + str ( float (convert) * mile ) + " milje."

    new_convert = raw_input ("""Želite vnesti novo pretvorbo? 
Vnesite da ali ne: """)
    if new_convert == "ne":
        print """Upamo da Vam v prihodnosti naša aplikacija lahko še kdaj pomaga.
Nasvidenje."""
        break



