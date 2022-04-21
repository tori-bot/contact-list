#!/usr/bin/env python3.9
from contact import Contact

def create_contact(fname,lname,phone,email):
    #function to create a new cntact
    new_contact=Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    #save contacts
    contact.save_contact()

def del_contact(contact):
    #delete contact
    contact.delete_contact()

def find_contact(number):
    #find contact by number
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    #check if contact exists
    return Contact.contact_exist(number)

def display_contacts():
    #return all saved contacts
    return Contact.display_contacts() 

#function to copy email
def copy_email(number):
    return Contact.copy_email(number)

# MAIN function
def main():
    print('Hello there! welcome to your contact list. What is your name?')
    user_name=input()

    print(f'Hello {user_name}. What would you like to do? ')
    print('\n')

while True:
    print('Use short codes: cc - create new a contact, dc - display contacts, fc - find a contact, del - delete a contact, ex - exit contact list')

    short_code=input().lower()

    if short_code=='cc':
        print('New contact')
        print('-' *10)

        print('First name ....')
        f_name=input()

        print('Last name ....')
        l_name=input()

        print('Phone number ....')
        p_number=input()

        print('Email address ....')
        e_address=input()

        save_contacts(create_contact(f_name,l_name,p_number,e_address))
        print('/n')
        print(f'New contact {f_name} {l_name} created successfully. ')
        print('/n')

    elif short_code=='dc':
        if display_contacts():
            print('Here is a list of yout contacts')
            print('/n')

            for contact in display_contacts():
                print(f'{contact.first_name} {contact.last_name} ....{contact.phone_number} ')
                print('/n')

        else:
            print('/n')
            print('You dont seem to have any contacts saved yet')
            print('/n')

    elif short_code=='fc':
        print('Enter the number you want to search for')

        search_number=input()

        if check_existing_contacts(search_number):
            search_contact=find_contact(search_number)

            print(f'{search_contact.first_name} {search_contact.last_name} ')
            print('-' *20)

            print(f'Phone number....{search_contact.phone_number} ')
            print(f'Email address....{search_contact.email} ')
            
        else:
            print('That contact does not exist.')

    elif short_code=='del':
        print('Enter the first name of contact you want to delete.')

        delete_name=input()

        if check_existing_contacts(delete_name):
            delete_contact=find_contact(delete_name)
            delete_contact()
        else:
            print('The contact does not exist')

    elif short_code=='ex':
        print('Bye.... ')
        break

    else:
        print('I really did not get that. Please use the short codes. ')


if __name__=='__main__':
    main()










    
