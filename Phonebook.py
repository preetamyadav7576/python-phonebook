class Contacts :
    phone_directory = [ ]

    def __init__(self,name,phone_no):
        self.name = name
        self.phone_no = phone_no
        Contacts.phone_directory.append(self)

    def show_contact(self):
        return  f"Name : {self.name}, Phone no. : {self.phone_no}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0 :
            print("There is no contact details to show.")
        else :
                for contact  in  cls.phone_directory :
                    print(contact.show_contact())

    @classmethod
    def search_name(cls,search):
         for contact in cls.phone_directory :
                if contact.name.lower() == search.lower() :
                        return contact.phone_no

         return  f"There is no any contact details for {search} ."

    @staticmethod
    def validate_phone_no(number):
        if len(number) >= 8 and number.isdigit() :
            return True
        else :
            return False


n_contacts = int(input(" How many contacts do want to enter ? "))
for i in range(n_contacts) :
    name = input("Enter your name : ")
    phone_number = (input(" Enter your phone number : "))
    if Contacts.validate_phone_no(phone_number) :
        Contacts(name,phone_number)
    else :
        print(" Invalid Phone Number. ")



Contacts.show_all_contact()
