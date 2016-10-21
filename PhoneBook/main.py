""" Simple program "Phone Book v1.0" to storage contacts you need
 (c)DevByFroz """
import pickle   # for storage
import os       # for clear screen
import sys      # for compute os


class PhoneBook:    # main class for work with my phone book
    def __init__(self):     # constructor
        try:    # open pickle-file
            with open('pb.pickle', 'rb') as file:
                self._phoneBook = pickle.load(file)
        except IOError:  # if file doesn't exist
            self._phoneBook = [[], [], [], []]
            self.add_new_item(input('Input name: '), input('Input address: '), input('Input phone: '))

    def get_last_id(self):
        return len(self._phoneBook[0]) - 1

    def get_pb(self, i, j):
        return self._phoneBook[i][j]

    def add_new_item(self, name, address, phone):
        self._phoneBook[0].append(self.get_last_id() + 1)
        self._phoneBook[1].append(name)
        self._phoneBook[2].append(address)
        self._phoneBook[3].append(phone)

    def search_contact(self, uid):
        if int(uid) < 0:
            return -1
        elif int(uid) > self.get_last_id():
            return -1
        return int(uid)

    def delete_contact(self, uid):  # delete all the elements of string
        for i in range(self.get_last_id() + 1):
            del self._phoneBook[i][self.search_contact(uid)]
        for i in range(int(uid), int(self.get_last_id()) + 1):
            self._phoneBook[0][i] = str(int(self._phoneBook[0][i]) - 1)

    def change_contact(self, uid):
        self._phoneBook[1][self.search_contact(uid)] = input("Input new name: ")
        self._phoneBook[2][self.search_contact(uid)] = input("Input new address: ")
        self._phoneBook[3][self.search_contact(uid)] = input("Input new number: ")

    def __del__(self):  # save pickle-object
            with open('pb.pickle', 'wb') as file:
                pickle.dump(self._phoneBook, file)


class Interface():  # class for UI
    @staticmethod
    def show_menu():
        print('''
    Address book
1. Show address book.
2. Add contact.
3. Change contact.
4. Delete contact.
5. Find contact.
6. Exit. ''')

    @staticmethod
    def print_contact(PhoneBook, uid):
        print('\t')
        for i in range(4):
            print(PhoneBook.get_pb(i, PhoneBook.search_contact(uid)), end='\t\t')
        print()

    @staticmethod
    def print_pb(pb):
        print('id \t\t name \t\t address \t\t phone')
        for j in range(pb.get_last_id() + 1):
            for i in range(len(pb._phoneBook)):
                print(str(pb._phoneBook[i][j]), end=" \t\t")
            print()

    @staticmethod
    def cls():
        if sys.platform == 'windows':
            os.system("cls")
        else:
            os.system("clear")


def main():
    pb = PhoneBook()
    interface = Interface
    choose = 0
    while choose != '6':
        Interface.cls()
        interface.show_menu()
        choose = input('Choose action: ')
        if choose == '1':       # Show phone book
            Interface.cls()
            interface.print_pb(pb)
            input("Press 'Enter' to continue...")
        elif choose == '2':     # Add new contact
            Interface.cls()
            name = input('Input name: ')
            address = input('Input address: ')
            phone = input('Input phone: ')
            pb.add_new_item(name, address, phone)
        elif choose == '3':     # Change exist contact
            Interface.cls()
            pb.change_contact(input("Input ID for change contact: "))
            input("Press 'Enter' to continue...")
        elif choose == '4':     # Delete contact
            Interface.cls()
            pb.delete_contact(input("Input ID for delete: "))
            print("Deleted!")
            input("Press 'Enter' to continue...")
        elif choose == '5':     # Find the contact u want
            Interface.cls()
            interface.print_contact(pb, input("Input ID for search: "))
            input("Press 'Enter' to continue...")
        elif choose == '6':     # Exit
            exit(0)


# Run main
if __name__ == '__main__':
    main()
