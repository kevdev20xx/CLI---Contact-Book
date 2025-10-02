contact_book = []

turn_on=True

while turn_on:
    print("Insert a new Contact or Search one throught the list.")
    print("Type 'insert' or 'search' to continue")
    command = input()
    name = ""
    phone_number = ""
    if command == "insert":
         name = input("Type the name of the contact: ")
         phone_number = input("Type the phone number of the contact:")
         contact = {}
         contact["name"] = name
         contact["phone_number"] = phone_number
         contact_book.append(contact)
         print("Your contact has been successfully added to the contact book")
         print("Displaying Contacts")
         counter = 1
         for c in contact_book:
            print(f"{counter}. {contact["name"]}  {contact["phone_number"]}")
            counter+=1
    if command == "search":
        search_keyword = input("Type the person's name or phone number to look up")
        contact_matched = []
        for c in contact_book:
            if search_keyword in c["name"] or search_keyword in c["phone_number"]:
                contact_matched.append(c)
        print("These are the results that match your search: ")
        counter = 1
        for c in contact_matched:
            print(f"{counter}. {c["name"]}  {c["phone_number"]}")
            counter+=1
        