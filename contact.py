class Contact:

    contact_list=[]

    #init method
    def __init__(self,firstName,lastName,phoneNumber,email):
        self.first_name=firstName
        self.last_name=lastName
        self.phone_number=phoneNumber
        self.email=email

    #save method
    def save_contact(self):
        Contact.contact_list.append(self)

    #delete method
    def delete_contact(self):
        Contact.contact_list.remove(self)

    #find contact
    @classmethod
    #decorator referring to entire class using the parameter cls
    def find_by_number(cls,number):
        for contact in cls.contact_list:
            if contact.phone_number==number:
                return contact

    @classmethod
    def contact_exist(cls,number):
        #check if contact exists in contact list
        for contact in cls.contact_list:
            if contact.phone_number==number:
                return True
            return False

    @classmethod
    def display_contacts(cls):
        #method to return all contacts on list
        return cls.contact_list

    import pyperclip
    @classmethod
    def copy_email(cls,number):
        contact_found=Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)