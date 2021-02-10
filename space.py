import requests
import json


def get_data():
    response = requests.get("http://api.open-notify.org/astros.json")

    try:
        assert(response.status_code == 200)
    except:
        print("Failed to get response")

    data = response.json()

    return data

def number_of_people(data):
    return data["number"]

def print_json(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text)

def print_data(data):
    number = data["number"]

    if number == 0:
        print("There is nobody currently in space")
    else:
        if number == 1:
            print("There is 1 person currently in space")
        else:
            people = data["people"]
            
            print("There are", number, "people currently in space:")
            print()

            for i in range(len(people)):
                person = people[i]
                
                print("\t" + str(i+1) + ")", person["name"], "(" + person["craft"] + ")")
            
    
def people_with_name(data, name):
    people = data["people"]
    result = []

    for i in range(len(people)):
        person = people[i]
        person_first_name = person["name"].split()[0]
    
        if person_first_name.lower() == name:
            result.append(person["name"])

    return result

def people_in_spacecraft(data, craft_name):
    people = data["people"]
    result = []

    for i in range(len(people)):
        person = people[i]

        if person["craft"].lower() == craft_name:
            result.append(person["name"])

    return result

    
# main
data = get_data()
run = True

print()
print("Enter 1 to search by name")
print("Enter 2 to search by spacecraft")
print("Enter 3 to print data")
print()

option = input().strip()
print()

if option == "1":
    while run:
        name = input("Enter first name or q to quit: ").strip()
        print()
        
        if name.lower() == "q":
            run = False
        else:
            people = people_with_name(data, name.lower())
            length = len(people)

            if length == 1:
                print("There is 1 person in space with the first name", name + ":")
                print()
            else:
                if length == 0:
                    print("There are 0 people in space with the first name", name)
                else:
                    print("There are", length, "people in space with the first name", name + ":")
                    print()

            for i in range(len(people)):
                print("\t" + str(i+1) + ")", people[i])

            print()
elif option == "2":
    while run:
        craft = input("Enter name of spacecraft or q to quit: ").strip()
        print()

        if craft.lower() == "q":
            run = False
        else:
            people = people_in_spacecraft(data, craft)
            length = len(people)

            if length == 1:
                print("There is 1 person aboard the spacecraft", craft + ":")
                print()
            else:
                if length == 0:
                    print("There are 0 people aboard the spacecraft", craft)
                else:
                    print("There are", len(people), "people aboard the spacecraft", craft + ":")
                    print()

            for i in range(len(people)):
                print("\t" + str(i+1) + ")", people[i])

            print()
elif option == "3":
    print_data(data)

        
    
    
