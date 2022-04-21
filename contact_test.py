import unittest

from contact import Contact


class TestContact(unittest.TestCase):
    def setUp(self):
        #setup methosd to run before each test cases
        self.new_contact=Contact('james','muriuki','0713253625','james@ms.com')

    
    def tearDown(self):
        #function to clean up after each test is run
        Contact.contact_list=[]


    def test_init(self):
        # test if object is initialized properly
        self.assertEqual(self.new_contact.first_name,'james')
        self.assertEqual(self.new_contact.last_name,'muriuki')
        self.assertEqual(self.new_contact.phone_number,'0713253625')
        self.assertEqual(self.new_contact.email,'james@ms.com')

    def test_save_contact(self):
        #test if the contact is saved on list
        self.new_contact.save_contact()   
        self.assertEqual(len(Contact.contact_list),1)

    def test_save_multiple_contact(self):
        #check if we can save multiple contacts
        self.new_contact.save_contact()
        test_contact=Contact('Test','user','0712345678','test@user.com')
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        #st if we can deletea contact from our list
        self.new_contact.save_contact()  
        test_contact=Contact('Test','user','0712345678','test@user.com') 
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):
        #test if we can find a contact ny number & display info
        self.new_contact.save_contact()
        test_contact=Contact('Test','user','0712345678','test@user.com')
        test_contact.save_contact()

        found_contact=Contact.find_by_number('0712345678')

        self.assertEqual(found_contact.phone_number,test_contact.phone_number)

    def test_contact_exists(self):
        #check to return boolean if we cannot find contact
        self.new_contact.save_contact()
        test_contact=Contact('Test','user','0711223344','test@user.com')
        test_contact.save_contact()

        contact_exists=Contact.contact_exist('0711223344')

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        #return list of all contacts saved
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)

    import pyperclip

    def test_copy_email(self):
        #confirm we are copying email address from found contact
        self.new_contact.save_contact()
        Contact.copy_email('0712345678')

        self.assertEqual(self.new_contact.email,pyperclip.paste())


if __name__=='__main__' :
    unittest.main()      

