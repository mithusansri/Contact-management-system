
"""
The problem that I have wished to solve is managing and organizing a list of contacts. 
Each contact is made up of a name and a phone number. A name can be made up of any character 
however each phone number should be unique and should be made up of 10 numbers.There should 
be many options or functions available to organize and manage a list of contacts. 
Functions to do this are, adding contacts, displaying contacts, searching contacts, 
modifying contacts, removing contacts, import and export contacts. Add contacts, asks the 
user to input a name and a unique, numeric, 10 digit phone number and it would get added to 
contacts. Displays contacts should show all the contacts as well as their information. 
Search contacts should display a desired contact’s information. Modify contacts should 
modify a desired contact’s name or number depending on what the user would like. Remove 
contact would remove a contact the user desires. Export contacts would send all of the 
user’s contacts to a separate file named cps109_a1_output.txt. Import contacts would bring in 
contacts from file cps109_a1_output.txt and add it to the user’s contacts.Imported contacts 
should only be contacts with different phone numbers than contacts already within the contacts list.
"""

def add_contacts(contacts):
    """
    Function that adds contacts to the contacts list
    """
    notvalid_number = False #Variable to check if the phone number is valid or not
    name = input("Enter the name of your contact: ")
    number = input("Enter the phone number of the contact (Eg, XXXXXXXXXX): ")
    for i in range(len(contacts)):
        contact = contacts[i] #Gets the tuple within the list
        if number == contact[1]: #Checks if the same number is already in the contacts list
            notvalid_number = True
            print("Phone number already exists in your contacts list")
    if number.isnumeric() == False: #Checks if the phone number has characters than are not numeric
        print("Phone number can only contain numbers")
        notvalid_number = True
    elif len(number) != 10 and notvalid_number == False: #Checks if the phone number has an incorrect length
        print("Invalid phone number length")
        notvalid_number = True
    if notvalid_number == False: #If the number is valid, adds the name and number in the list as a two-tuple
        contact = (name, number) 
        contacts.append(contact)
        print(name, "has been added to your contacts")
    print()

def display_contacts(contacts):
    """
    Function that prints all the contact information within the contacts list
    """
    position = 1 #Variable that represents the number position of the contact.
    if len(contacts) != 0: #Checks if the contact list is not empty
        for i in range (0, len(contacts)):
            contact = contacts[i] 
            print(str(position) + ".", "Name:", contact[0], "| Number:", contact[1]) #Prints the name and phone number in a formatted way
            position += 1 #Increasing the position variable by one to display position for the next contact
    else:
        print("Your contact list is empty")
    print()

def search(number, contacts):
    """
    A helper function that returns the index of the tuple that is in within the contacts list using the 
    phone number as every phone number is unique
    """
    for i in range(len(contacts)):
        contact = contacts[i]
        if number == contact[1]:
            return i
    return -1 #If the phone number is not any tuple within the list, returns -1

def search_contacts(contacts):
    """
    Function that searches for a contact in the contacts list by using the phone number and prints the name and number 
    if it exists
    """
    search_num = input("Enter the number of the contact you would like to look for (Eg. XXXXXXXXXX): ")
    index = search(search_num, contacts) #Variable that stores the value of the search helper function 
    contact = contacts[index] #Variable that gets the tuple that the phone number is in
    if index != -1: 
        print("Contact has been found")
        print("Name:", contact[0], "| Number:", contact[1]) #Prints the information of the desired contact 
    else:
        print("Contact does not exist") 
    print()

def modify_contacts(contacts):
    """
    Function that modifies the name or number of a contact from the contacts list
    """
    search_num = input("Enter the number of the contact you would like to modify (Eg. XXXXXXXXXX): ")
    index = search(search_num, contacts)
    notvalid_number = False #Boolean variable that states whether the new user entered phone number is valid or not
    if index != -1:
        print("Contact has been found")
        modify = input("Would you like to modify the contact's name or number? (Type Name or Number): ")
        contact = contacts[index]
        first = contact[0] #Variable that stores the contact's first name so that it's name in the tuple does not get lost
        if contact[1] == search_num:
            if modify == "Name": 
                new_name = input("What is the new name you would like to put?: ")
                contacts[index] = (new_name, search_num) #Replaces the old tuple with a new tuple that has the contact's new name and current phone number
                print("Contact modified")
            elif modify == "Number":
                new_number = input("What is the new number you would to put?: ")
                for i in range(len(contacts)): #Line 89-99 checks whether the user inputted a valid phone number
                    contact = contacts[i]
                    if new_number == contact[1]:
                        notvalid_number = True
                        print("Phone number already exists in your contacts list")
                if new_number.isnumeric() == False:
                    print("Phone number can only contain numbers")
                    notvalid_number = True
                elif len(new_number) != 10 and notvalid_number == False:
                    print("Invalid phone number length")
                    notvalid_number = True
                elif notvalid_number == False: 
                    contacts[index] = (first, new_number) #Replaces the old tuple with a new tuple that has the contact's current name and new phone number
                    print("Contact modified")
            else:
                print("Invalid input") #Prints if user did not enter 'Name' or 'Number as their choice
    else:
        print("Contact does not exist") 
    print()

def remove_contacts(contacts):
    """
    Function that removes a tuple from the contacts list 
    """
    search_num = input("Enter the number of the contact you would like to delete (Eg. XXXXXXXXXX): ")
    index = search(search_num, contacts)
    if index != -1:
        print("Contact has been found")
        answer = input("Are you sure you would like to delete this contact (Type Yes or No): ") #Asks user if they really want to delete the contact
        if answer == "Yes":
            del contacts[index] #Deletes the tuple of the contact if the user answered 'Yes'
            print("Contact removed")
        elif answer != "No" and answer != "Yes":
            print("Invalid Input") #Prints if user did not input 'Yes' or 'No' to the 'answer' variable
    else:
        print("Contact does not exist")
    print()
    
def export_contacts(contacts):
    """
    Function that exports the information of each contact from the contacts list to a different file
    """
    file = open("cps109_a1_output.txt", "w") #Creates the file 'cps109_a1_output.txt' to write in it
    for i in range (len(contacts)):
        contact = contacts[i]
        file.write(contact[0] + " " + contact[1] + "\n") #Writes the name of contact and number seperated by a space to the new file
    file.close()
    print("Contacts exported to cps109_a1_output.txt.")
    print()

def import_contacts(contacts):
    """
    A function that adds new contacts from a different file to the current contacts list
    """
    try:
        file = open("cps109_a1_output.txt", "r")  #Opens the file 'cps109_a1_output.txt' to read its values
        lines = file.readlines()
        for i in range(len(lines)):
            contact = lines[i].strip().split(" ") #Creates a list that has the name as the first element and the phone number as the second element
            contacts.append((contact[0], contact[1])) #Adds the name and phone number to the contacts list
        file.close()
        print("Contacts imported from cps109_a1_output.txt")
    except FileNotFoundError:
        print("The file 'cps109_a1_output.txt' not found.")
    print()
    
def contact_system():
    contacts = [] #Create a list to store all the contacts in
    while True:
        print("Personal Contacts Manager")
        print("1. Add contact")
        print("2. Display contacts")
        print("3. Search contact")
        print("4. Modify contact")
        print("5. Remove contact")
        print("6. Export contacts")
        print("7. Import contacts")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")
        if choice == "1":
            add_contacts(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice ==  "4":
            modify_contacts(contacts)
        elif choice == "5":
            remove_contacts(contacts)
        elif choice == "6":
            export_contacts(contacts)
        elif choice == "7":
            import_contacts(contacts)
        elif choice == "8":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    contact_system() #Calling the main function to start the contact_system
