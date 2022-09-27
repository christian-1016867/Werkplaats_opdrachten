from re import X
from unittest.main import MAIN_EXAMPLES
#Opdracht Integers
people = 7861304740
print(people)
people = 7_861_304_740
print(people)

meals = 3
people_eat = people * meals
print(people_eat)

days = 365
meals_per_year = people_eat * days
print(meals_per_year)

type(meals_per_year)

#Opdracht float
ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)
speed_of_light = 299_792_458
print(speed_of_light)
distance_Rotterdam_NewYork = 5_862.03
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(time_to_reach_NYC)

#String
ship = "titanic"
print(ship)
sentence = "He doesn’t think it’s a good idea to spend all his money on video games."
print(sentence)
paragraph = """Computer Technology means all designs, drawings, procedures(including design, manufacturing, test and maintenance procedures)specifications, software (other than as described within the meaning of the term"Software" defined elsewhere herein), printed circuit board art work, integratedcircuit masks, test equipment, tools, fixtures, documentation, training materials,and information, in whatever form, related to, useful, utilizable or necessary inthe design, manufacture, test and/or maintenance of the computer system, or relate to any Technology Licenses."""
print(paragraph)
characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")


year = 1936
inventor = "Alan Turing"
name_of_machine = "automatic machine"
invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine"  ({name_of_machine}).'
print(invention)

#Boolean
logged_in = False
print(logged_in)
netwerk_activity = True
print(netwerk_activity)

user_name = "John Doe"
entered_name = input("User name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name
print(f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")
print(f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")

lights_on = False
lock_closed = True

alarm_activated = not lights_on and lock_closed
print(f"the alarm is activated, is: {alarm_activated}")

#Berekening
import math

x = 9.1
deel1 = (3 * x) - 1
deel2 = (1 + X)
deel3 = (deel2)**2
y = math.sqrt(deel1) + deel3
print(f'De waarde van y = {y} als x = {x}')

import math

a = 0.87
b = 22.7
c = 5.03
deela = b**2
deelb = 4 * a * c
deelc = deela - deelb
deeld = math.sqrt(deelc)
deele = -b + deeld
deelf = 2 * a
y = deele / deelf

print(f'De waarde van y = {y} als a = {a}, b = {b} en c = {c}')

#Containers
containers_gelost = 331
minuten_gelost = 441
containers_geladen = 287
minuten_laden = 295
Gemiddeld_geladen_tijd = minuten_laden / containers_geladen
Gemiddeld_gelost_tijd = minuten_gelost / containers_gelost

print(f"de gemiddelde tijd lossen: {Gemiddeld_gelost_tijd}")
print(f"de gemiddelde tijd laden: {Gemiddeld_geladen_tijd}")

#Berekening
t = 4
v = 179875474.8
c = 299792458

Deel1 = v**2
deel2 = c**2
deel3 = deel1 / deel2
deel4 = 1 - deel3
deel5 = v * deel4
deel6 = 1 / deel5
delta = t * deel6
type(t)
print(f'Vanaf een komeet gezien zit u {delta} uur op de stoel.')




