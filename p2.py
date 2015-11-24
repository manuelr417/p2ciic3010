##!/usr/bin/python
# Filename: p2.py
import sys

##### ADD YOUR NAME, Student ID, and Section number #######
# NAME:
# STUDENT ID:
# SECTION:
###########################################################


###########  ADD YOUR CODE HERE ###############################

person_list = []
person_id = 1

def add_person(first_name, last_name, age, birth, person_list, person_id):
    new_person = {"id" : person_id, "first_name" : first_name, "last_name" : last_name, "age" : age, "birth" : birth}
    person_list.append(new_person)
    return person_id + 1

def find_person_by_id(person_list, id):
    for person in person_list:
        if person["id"] == id:
            return person

    return None

def find_person_by_name(first_name, last_name, person_list):
    for person in person_list:
        if (person["first_name"] == first_name) and (person["last_name"] == last_name):
            return person
    return None

def update_person (id, first_name, last_name, age, birth, person_list):
    for person in person_list:
        if person["id"] == id:
            person["first_name"] = first_name
            person["last_name"]  = last_name
            person["age"]  = age
            person["birth"]  = birth
            return person

    return None

def delete_person(id, person_list):
    position = 0
    for person in person_list:
        if person["id"] == id:
            del person_list[position]
            return True
        else:
            position +=1

    return False

def print_person_list(person_list):
    for person in person_list:
        #person_info = (person[id], person)
        #data = "id: {0}, first_name: {1}, last_name: {2}, age: {3}, birth: {4}".format()





