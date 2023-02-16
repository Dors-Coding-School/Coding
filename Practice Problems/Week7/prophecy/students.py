from cs50 import SQL
import csv

def main():
    # Open database
    db = SQL("sqlite:///roster.db")

    # Create empty dictionaries to store data of each new table
    students = []
    houses = []
    relationships = []

    # Open CSV file
    with open("./students.csv", "r") as file:
        # Create DictReader
        reader = csv.DictReader(file)

        for row in reader:
            house = row["house"]
            head = row["head"]
            student_name = row["student_name"]
            create_house(house, head, houses)
            create_student(student_name, students)
            create_relationship(student_name, house, relationships)

    # Add data into new_students table
    for student in students:
        db.execute("INSERT INTO new_students (student_name) VALUES (?)", student["student_name"])

    # Add data into houses table
    for house in houses:
        db.execute("INSERT INTO houses (house, head) VALUES (?,?)", house["house"], house["head"])

    # Add data into house_assignments table
    for relationship in relationships:
        db.execute("INSERT INTO house_assignments (student_name, house) VALUES (?,?)", relationship["student_name"], relationship["house"])

def create_house(house, head, houses):
    count = 0
    for h in houses:
        if h["house"] == house:
            count += 1
    if count == 0:
        houses.append({"house":house,"head":head})

def create_student(student_name, students):
    students.append({"student_name": student_name})

def create_relationship(student_name, house, relationships):
    relationships.append({"student_name": student_name, "house": house})

main()
