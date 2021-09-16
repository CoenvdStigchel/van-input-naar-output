#Pizzaria negozio di alimentari (CoenvdStigchel)

prijsKleinePizza = 4.00
prijsMiddelPizza = 7.00
prijsGrotePizza = 11.00

aantalKLeinePizza = int(input("Hoeveel kleine pizza's wil je hebben?" ))
aantalMiddelPizza = int(input("Hoeveel middel pizza's wil je hebben?" ))
aantalGrotePizza = int(input("Hoeveel grote pizza's wil je hebben?" ))

bedragKleinePizza = prijsKleinePizza*aantalKLeinePizza
bedragMiddelPizza = prijsMiddelPizza*aantalMiddelPizza
bedragGrotePizza = prijsMiddelPizza*aantalGrotePizza

totaalbedrag = bedragKleinePizza+bedragMiddelPizza+bedragGrotePizza

print("----------------------------------------------------")
print('|  Kleine Pizzas : ' + str(prijsKleinePizza))       
print('|  Middel Pizzas : ' + str(prijsMiddelPizza))
print('|  Grote Pizzas  : ' + str(prijsGrotePizza))
print('|  Totaalbedrag   : ' + str(totaalbedrag))
print("----------------------------------------------------")