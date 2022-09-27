


popular_games = ["Player's Unknown Battle ground (PUBG) 50 million 2018",
"Fortnite Battle Royale 39 million 2017",
"Apex Legends 50 million (1 month) 2019",
"Leaugue of Legends (LOL) 27 million 2009",
"Counter Strike; Global Offensive 32 million 2014",
"Heartstone 29 Million 20120",
"Minecraft 91 million 2011",
"DOTA 2 4 million 2015",
"The division 2 N/A 2019",
"The Splatoon 2"]
print(popular_games)

# a]
print(f"5] {popular_games[4]}")

#b]
dota_game = popular_games[7]
characters_name = len(dota_game)
print(f"The game {dota_game} has {characters_name} characters.")

#c]
gamelijst = len(popular_games)
print(f"Er zitten {gamelijst} games in de lijst.")

#d]

print(popular_games)
popular_games.insert(1, "Snake")
print(popular_games)

#e]
index_of_splatoon = popular_games.index("The Splatoon 2")
splatoon = popular_games.pop(index_of_splatoon)
print(f"Helaas heeft de game {splatoon} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {splatoon}.")

print("")

print(popular_games)

#f]
index_of_heartstone = popular_games.index("Heartstone 29 Million 20120")
popular_games[index_of_heartstone] = "Heartstone 29 Million 2012"

print("")
print(popular_games)

#TUPLE kan je herkennen aan het () van het lijstje

computer_suppliers = ("Apple",
"Asus",
"Dell",
"Lenovo",
"Acer",
"Samsung",
"MSI",
"Hewlett-Packard (HP)",
"Toshiba",
"Microsoft",
"Chuwi",
"Sony")

print(computer_suppliers)

#a]
number_of_suppliers = len(computer_suppliers)
print(f"De tuple bevat {number_of_suppliers} computer leveranciers.")

#b]
computer_supplier = computer_suppliers[7]
characters_in_name = len(computer_supplier)
print(f"De naam van {computer_supplier} bestaat uit {characters_in_name} karakters.")
print()
#c]
computer_tien = computer_suppliers[9]
print(f"De naam van de computer leverancier op de 10de plaats is {computer_tien}.")

#Dictionary kan je herkennen aan het gebruik van {}
phone_numbers = {"The Simpsons": "636-555-3266",
"Vegas Vacation": "555-0100",
"Ghostbusters": "555-23678",
"Billy Madison": "555-0840",
"Swingers": "213-555-4679",
"Bruce Almighty": "555-0123",
"Seinfeld": "555-FILK",
"Arrested Development": "555-0113",
"Die Hard With a Vengeance": "555-0001",
"The A-Team": "555-6162"}
print(phone_numbers)

#a]
print(f"Het telefoonnummer van Bruce Almighty is {phone_numbers['Bruce Almighty']}.")

#b]
phone_numbers["Harry Potter"] = "605-475-6961"
print(phone_numbers)

#c]
old_phone_number = phone_numbers["Ghostbusters"]
new_phone_number = "555-2368"
phone_numbers["Ghostbusters"] = new_phone_number
print(f"Het telefoonnummr {old_phone_number} van de Ghostbusters is gewijzigd naar {new_phone_number}.")
print(phone_numbers)

#d]
phone_number = phone_numbers.pop("Seinfeld")
print(f"Telefoonnummer {phone_number} van Sienfeld is verwijderd.")
print(phone_numbers)

#e]
number_of_phone_numbers = len(phone_numbers)
print(f"In de dictionary zitten {number_of_phone_numbers} telefoonnummers.")
print(phone_numbers)



