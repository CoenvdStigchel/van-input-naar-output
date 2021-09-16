Ticket = 7.45
aantalTickets = int(input('Hoeveel tickets wil je hebben? '))
GameSeat = 0.37
periodesvan5min = int(input('Hoeveel Periodes van 5 minuten op de VR GameSeat wil je hebben? '))
aantalPersonen = int(input('Voor hoeveel mensen wil je reserveren? '))

Bedrag = Ticket*aantalTickets+GameSeat*periodesvan5min+aantalPersonen

factuurTekst = "Dit geweldige dagje uit met " + str(aantalPersonen) + " mensen in de Speelhal met " + str(periodesvan5min) + " spellen van 5 minuten lang op de VR GameSeat kost je maar " + str( Bedrag) + " euro. Goedkoper krijg je niet! Ga snel naar speelhaldavinci.nl!"

print(factuurTekst)
