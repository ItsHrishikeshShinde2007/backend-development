import sqlite3

def printallcars(cursor):
    cursor.execute("SELECT * FROM cars;")
    return cursor.fetchall()

def addnewcar(connection, cursor, car_id, name, company, type, manufacturing_year, horsepower):
    cursor.execute("INSERT INTO cars (car_id, name, company, type, manufacturing_year, horsepower) VALUES (?, ?, ?, ?, ?, ?);", (car_id, name, company, type, manufacturing_year, horsepower))
    connection.commit()

def deletecar(connection, cursor, car_id):
    cursor.execute("DELETE FROM cars WHERE car_id = ?;", (car_id,))
    connection.commit()

def updatecar(connection, cursor, car_id, name, company, type, manufacturing_year, horsepower):
    cursor.execute("UPDATE cars SET name = ?, company = ?, type = ?, manufacturing_year = ?, horsepower = ? WHERE car_id = ?;", (name, company, type, manufacturing_year, horsepower, car_id))
    connection.commit()

if __name__ == "__main__":
    connection = sqlite3.connect("database/backend.db")
    print("Database connected successfully.")

    cursor = connection.cursor()

    print("---List of all cars---")
    cars = printallcars(cursor)
    print("The Output of the data table is as follows:")
    for car in cars:
        print(car)

    print("---Adding a car---")
    addnewcar(connection, cursor, 14, 'Koenigsegg One', 'Koenigsegg', 'Hypercar', 2014, 1360)
    cursor.execute("SELECT * FROM cars WHERE car_id = 14;")
    print("Ok so, ", cursor.fetchone()[1], " car added successfully.")

    print("---Deleting a car---")

    cursor.execute("SELECT * FROM cars WHERE car_id = 12;")
    car = cursor.fetchone()

    if car is not None:
        deletecar(connection, cursor, 12)
        print("Car", car[1], "deleted successfully.")
    else:
        print("Car not found.")

    print("---Updating a car---")

    cursor.execute("SELECT * FROM cars WHERE car_id = 13;")
    car = cursor.fetchone()

    if car is not None:
        old_name = car[1]

        updatecar(
            connection, cursor, 13,
            'McLaren P1', 'McLaren', 'Hypercar', 2013, 903
        )

        cursor.execute("SELECT * FROM cars WHERE car_id = 13;")
        updated_car = cursor.fetchone()

        print("Car updated from", old_name, "to", updated_car[1])
    else:
        print("Car not found.")

    print("---Final list of all cars---")
    cars = printallcars(cursor)
    print("The Output of the data table is as follows:")
    for car in cars:
        print(car)

    connection.close()