#Phone Book

import sys
import sqlite3

connection = sqlite3.connect("My_SQL_1.db")
cursor = connection.cursor()

#*******************************************************************
def show_menu():

    print("\n\t\t******************")
    print("\t\t*                *")
    print("\t\t*  Contact List  *")
    print("\t\t*                *")
    print("***********************************************\n")

    print("1. Add contact (+)\n")
    print("2. Sort and display contact list\n")
    print("3. Search for a contct\n")
    print("4. Remove a member from contact List\n")
    print("5. Exit Contact List\n")

show_menu()
#****************************************************************************

def add_contact():

    name = input("Enter a name\n")
    number = input("Enter a number\n")
    email = input("Enter a email\n")
    birth_day = input("Enter a birth_day\n")
    category = input("Enter a category(work/home/school/others)\n")

    cursor.execute("""insert into contact (name,number,email,birth_day,category) Values(?,?,?,?,?)""",(name,number,email,birth_day,category))
    connection.commit()

add_contact()

for row in cursor.execute('select * from contact'):
    print(list(row))

connection.close()

#***************************************************************************
def sort_display():
    query = 'select * from contact'
    #member = ''
    member = cursor.execute(query)
    connection.commit()
    list_member = list(member)
    new_list = sorted(list_member)
    print(new_list)

sort_display()

connection.close()

# #****************************************************************************
#
def search(name):
    query = 'select * from contact'
    member = ''
    member = cursor.execute(query)
    connection.commit()
    list_member = list(member)

    output = [item for item in list_member
                if item[0] == name]

    print(output)

name = input("Please Enter a name:\t")

search(name)

connection.close()
#
# #***************************************************************************
#
def remove(name):
    query = 'delete from contact where name = ?'
    cursor.execute(query,(name))
    connection.commit()
    print("Deleted Successfully!.")
name = input("Please Enter a name:\t")

remove(name)

for row in cursor.execute('select * from contact'):
    print(list(row))

connection.close()
#
#
# #****************************************************************************
#
def goodbye():
    print("\n*****************************************")
    print("*** THANKS for using our Contact Book ***")
    print("*****************************************\n")
    print("*************** Good Bye*****************")

    sys.exit()

#*****************************************************************************



#*****************************************************************************
def menu():
    ch = 1
    while ch in (1,2,3,4):
        show_menu()
        choice = int(input("Enter your choice:\n"))
        if choice == 1:
            add_contact()

        elif choice == 2:
            sort_display()

        elif choice == 3:
            search(name)

        elif choice == 4:
            remove(name)

        else:
            goodbye()

menu()
