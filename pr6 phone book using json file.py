import json

import os

from typing import TextIO

print(f'{'Phone Book':>{15}}')

print(20*'=')

FILE_NAME = 'contacts.json'

def load_contact():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, 'r') as f:

            return json.load(f)

    else:

        return {}

def save(contacts_data):

    with open(FILE_NAME, 'w') as f: # type: TextIO

        json.dump(contacts_data, f, indent = 4)

contacts = load_contact()

def menu():

    print('\nEnter the operation you want to perform:-')

    print(42*'_')

    print('1. Add a contact.')

    print('2. View contacts.')

    print('3. Search contacts')

    print('4. Update a contact.')

    print('5. Delete a contact')

    print('6. Exit the program.')

def add ():

    #contacts = load_contact()

    name = input('\n🙂Enter the contacts name :- ').title()

    phone = input('\n☎️Enter the phone number :- ')

    email = input('\n📧Enter the email :- ').lower()

    contacts[name] = {

        'phone': phone,

        'email': email

    }

    save(contacts)

    print('\nContact has been added successfully. ✅')

def view():

    #contacts = load_contact()

    if not contacts:

        print('\nThere is no contact available. ❌')

    else:

        for name, info in contacts.items():

            print('\nName: ', name)

            print('Phone :', info['phone'])

            print('Email :', info['email'])

            print(28*'-')

def search ():

    name = input('\n🙂Enter tha name of the contact :- ').title()

    if name in contacts:

        info = contacts[name]

        print(f'\n🔍Found the contact for {name}')

        print(f'\n☎️Phone : {info['phone']}')

        print(f'\n📧Email : {info['email']}')
    else:

        print('\nThe contact can\'t be found. ❌')

def update():

    name = input('\n🙂Enter the name of the contact to update :- ').title()

    if name in contacts:

        updating = input('\n🪪Enter the field(phone, email) to update :- ').lower()

        updating_info = input('\n🗃️Enter the info to update :- ').lower()

        update2(name, updating, updating_info)

    else:

        print('\nThe contact can\'t be found. ❌')



def update2(name, updating, updating_info):

    if updating in ('phone', 'email'):

        contacts[name].update({updating: updating_info})

        save(contacts)

        print('\nThe contact has been updated successfully. ✅')

    else:

        print('\nThe field doesn\'t exist. ❌ ')


def delete():
    name = input('\n🙂Enter the name of the contact to delete :- ')

    if name in contacts:

        del contacts[name]

        save(contacts)

    else:

        print('\nThe contact can\'t be found. ❌')

while True:

    menu()

    try:
        operation = int(input('\n😀Enter the operation you want to perform :- '))

    except ValueError:

        print(f'\nOops invalid input please enter a number between 1-6. \n{20*'🙄'}')
        continue

    if operation == 1:

        add()

    elif operation == 2:

        view()

    elif operation == 3:

        search()

    elif operation == 4:

        update()

    elif operation == 5:

        delete()

    elif operation == 6:

        print('\nThank you for using this program. ❤️')
        break

    else:

        print(f'\nOops invalid input please enter a number between 1-6. \n{20 * '🙄'}')
        continue
