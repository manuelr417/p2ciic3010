##!/usr/bin/python
# Filename: p2.py
import sys

##### ADD YOUR NAME, Student ID, and Section number #######
# NAME:
# STUDENT ID:
# SECTION:
###########################################################



###########  ADD YOUR CODE HERE ###############################



def add_person(first_name, last_name, age, birth, person_list, person_id):
    new_person = {"id" : person_id, "first_name" : first_name, "last_name" : last_name, "age" : age, "birth" : birth}
    person_list.append(new_person)
    return person_id + 1


def print_person_list(person_list):
    for person in person_list:
        birth_date =    str(person["birth"][0]) + "/" + person["birth"][1] + "/" + person["birth"][2]
        data = "id: {0}, first_name: {1}, last_name: {2}, age: {3}, birth: {4}".format(
            person["id"], person["first_name"], person["last_name"], person["age"], birth_date
         )
        print data

def handle_add_new_person(person_list, person_id):
    print "Person information format: First Name, Last Name, Age, Birth Month, Birth Day, Birth Year"
    person_info = raw_input("Enter the person information: ")
    person_data = person_info.split(",")
    birth_date = (person_data[3], person_data[4], person_data[5])
    upd_person_id = add_person(person_data[0], person_data[1], person_data[2], birth_date, person_list, person_id)
    return upd_person_id

def handle_view_all_person(person_list, person_id):
    print_person_list(person_list)
    return person_id


###########################################################

def print_program_menu():
    print "\n"
    print "Welcome to person database program. Please, choose an option:"
    print "1. Add new person"
    print "2. View existing person by Id"
    print "3. View existing person by full name "
    print "4. Update existing person"
    print "5. Delete existing person"
    print "6. View all persons"
    print "7. Exit"

def identify_option(option):
    if option.isdigit() :  # Verify if this is a number
        numeric_option = int(option)
        # check if in range
        if numeric_option >= 1 and numeric_option <= 7:
            return (0, numeric_option)
        else:
            return (-1, 0) # invalid option
    else:
        return (-1, 0) # invalid option

def process_operation(numeric_option, person_list, person_id):
    if (numeric_option == 1):
        return handle_add_new_person(person_list, person_id)
    elif (numeric_option == 6):
        return handle_view_all_person(person_list, person_id)


def main():
    person_list = []
    person_id = 1
    done = False
    while not done:
        print_program_menu()
        user_option = raw_input("Enter option: ")
        option_info_tuple = identify_option(user_option)
        if option_info_tuple[0] == 0:
            #option was valid
            if option_info_tuple[1] == 7:
                done = True
                print "Thanks for using the person database program"
            else:
                person_id = process_operation(option_info_tuple[1], person_list, person_id)
        else:
            #option invalid
            print "Invalid Option\n"

# This line makes python start the program from the main function
if __name__ == "__main__":
    main()
    sys.exit()





