from ast import If

age_str = input('what is your age? ')
print(f'your age is {age_str}')

connection_choice_str = input('Welke verbinding wilt U gebruiken [4G, 5G, Wifi open]: ')
connection_keuze = connection_choice_str.upper()

if connection_keuze == "4G":
    print(f"U bent verbonden via {connection_keuze}!")
elif connection_keuze == "5G":
    print(f"U bent verbonden via {connection_keuze}")
elif connection_keuze == "Wifi Open":
    print(f"U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    answer_str = input("wilt u nog steeds een verbinding maken [ja/nee]: ")
    answer = answer_str.upper()
    if answer == "JA":
        print(f"U bent verbonden via {connection_keuze}!")
    else:
        print("U bent niet verbonden!")
else:
    print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")


#Sub-string
print("Is Hello with a capital 'H' within the string 'Hello, everyone!'")
if "Hello" in "Hello, everyone!":
    print('Yes, Hello is within the hello, everyone! string')

print("is Hello with a lower case 'h' within the string 'Hello, everyone!'")
if "hello" in "Hello, everyone!":
    print('Yes, hello is within the Hello, everyone! string')
else:
    print('No, hello with small letters in not within the string')



print("Patient exposed to TB")
question_1_str = input("Is the patient an adult or a child? [Adult/Child]: ")
question_1 = question_1_str.upper()
if question_1 == "ADULT":
    print("Adult")
    question_2_str = input("Has common TB symtoms? [Yes/No]: ")
    question_2 = question_2_str.upper()
    if question_2 == "YES":
        print("Treat as likely TB patient and perform full TB exam.")
    elif question_2 == "NO":
        print("Have patient report back in unwell; return in 1 month for checkup.")
    else:
        print("Abort, unknown input.")
elif question_1 == "CHILD":
    print("Child")
    question_3_str = input("Can TB test be given? [Yes/No]: ")
    question_3 = question_3_str.upper()
    if question_3 == "YES":
        print("Administer TB test.")
        print("Assess TB test results and child's condition.")
    elif question_3 == "NO":
        question_4_str = input("Child well? [Yes/No]: ")
        question_4 = question_4_str.upper()
        if question_4 =="Yes":
            print("6 months preventive isoniazid.")
            print("Have parent bring in if child shows any symptoms.")
        elif question_4 == "NO":
            print("Take full history.\nExamine for TB.")
            print("If TB likely diagnosis, treat for TB.")
            print("If other diagnosis more likely, treat as needed and watch for TB symptoms.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, unknown input.")
else:
    print("Abort, unknown unput.")


#Shopping cart
print("Shopping Cart")
question_1_str = input("Payment method? [Online/Offline]: ")
question_1 = question_1_str.upper()
if question_1 == "ONLINE":
    print("Online, place purchase order")
    question_2_str = input("Admin User? [Yes/No]: ")
    question_2 = question_2_str.upper()
    if question_2 == "YES":
        print("Enter payment details.")
        print("Place order.")
    elif question_2 == "NO":
        question_3_str = input("Approvel rules? [Approved/Rejected]: ")
        question_3 = question_3_str.upper()
        if question_3 == "APPROVED":
            print("Enter payment details.")
            print("Place order.")
        elif question_3 == "REJECTED":
            print("Purchase order rejected.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, Unknown input.")
elif question_1 == "OFFLINE":
    print("Offline, place purchase order")
    question_4_str = input("Admin User? [Yes/No]: ")
    question_4 = question_4_str.upper()
    if question_4 == "YES":
        print("Order created automatically.")
    elif question_4 == "NO":
        question_5_str = input("Approvel rules? [Approved/Rejected]: ")
        question_5 = question_5_str.upper()
        if question_5 == "APPROVED":
            print("Order created automatically.")
        elif question_5 == "REJECTED":
            print("Purchase order rejected.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, unknown input.")
else:
    print("Abort, unknown input.")











        
        













    

