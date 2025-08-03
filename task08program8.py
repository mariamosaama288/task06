namelist = []
phonelist = []
adresslist = []

def addnum () :
    name = input("enter name : ")
    namelist.append(name)
    phone = input ("enter phone number : ")
    phonelist.append(phone)
    adress = input("enter email adress : ")
    adresslist.append(adress)

def view () :
    for i in range(len(namelist)) :
         print(f"{i+1}. {namelist[i]} - {phonelist[i]} - {adresslist[i]}")
         
def search():
    keyword = input("Enter name or phone to search: ")
    found = False
    for i in range(len(namelist)):
        if keyword.lower() in namelist[i].lower() or keyword in phonelist[i]:
            print(f"Found: {namelist[i]} - {phonelist[i]} - {adresslist[i]}")
            found = True
    if not found:
        print("Contact not found.")

def delete():
    name_to_delete = input("Enter the name to delete: ").lower()
    found = False
    
    i = 0
    while i < len(namelist):
        if namelist[i].lower() == name_to_delete:
            print(f"Deleting {namelist[i]}...")
            del namelist[i]
            del phonelist[i]
            del adresslist[i]
            found = True
          
        else:
            i += 1
    
    if found:
        print("Contact(s) deleted.")
    else:
        print("No contact found with that name.")

while True :
    print("1. add a New Contact")
    print("2. View All Contacts")
    print("3. Search for a Contact")
    print("4. Delete a Contact")
    print("5. Exit")
    answer = int(input (" choose a number : "))

    if answer == 1 :
        addnum()
    elif answer == 2 :
        view()
    elif answer == 3 :
        search()
    elif answer == 4 :
        delete()
    elif answer == 5:
        print("Goodbye!")
        break





    

