
import sqlite3

# variable declarations
invalid_input_response = "That is not a valid option. Try again."


# functions


def print_all_cars():
    # can print all car stats
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    # option of whether it should be ordered or not, and if so how
    user_input_order = input("""Ordered by:
        1. Car name
        2. Horsepower
        3. Races competed in
        4. Races won
        5. Disregard
                """)
    if user_input_order == '1':
        sql = 'SELECT * FROM cars ORDER BY car_name;'
    elif user_input_order == '2':
        sql = 'SELECT * FROM cars ORDER BY horsepower DESC;'
    elif user_input_order == '3':
        sql = 'SELECT * FROM cars ORDER BY races DESC;'
    elif user_input_order == '4':
        sql = 'SELECT * FROM cars ORDER BY wins DESC;'
    elif user_input_order == '5':
        sql = 'SELECT * FROM cars;'
    else:
        # catches invalid options and returns the user back to the main menu
        print(invalid_input_response)
        return
    # printing the results
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""Car ID   Car name                             HP  Races  Wins""")
    for car in results:
        print(f"{car[0]:<3}{car[1]:<38} {car[2]:<6} {car[3]:<4} {car[4]:<4}")
    db.close()


def print_car_names():
    # printing car names
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    # option of whether it should be ordered or not and if so how
    user_input_order = input("""Ordered by:
        1. YES
        2. NO
                """)
    if user_input_order == '1':
        sql = 'SELECT * FROM cars ORDER BY car_name;'
    elif user_input_order == '2':
        sql = 'SELECT * FROM cars;'
    else:
        # catches invalid options and returns the user back to the main menu
        print(invalid_input_response)
        return
    # printing the results
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Car ID   Car name")
    for car in results:
        print(f"{car[0]:<3} {car[1]}")
    db.close()


def print_cars_and_hp():
    # printing car names and horsepower
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    # option of whether it should be ordered or not and if so how
    user_input_order = input("""Ordered by:
        1. Car name
        2. Horsepower
        3. Disregard
                """)
    if user_input_order == '1':
        sql = 'SELECT * FROM cars ORDER BY car_name;'
    elif user_input_order == '2':
        sql = 'SELECT * FROM cars ORDER BY horsepower DESC;'
    elif user_input_order == '3':
        sql = 'SELECT * FROM cars;'
    else:
        # catches invalid options and returns the user back to the main menu
        print(invalid_input_response)
        return
    # printing the results
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""Car ID   Car name                             HP""")
    for car in results:
        print(f"{car[0]:<3} {car[1]:<38} {car[2]:<6}")
    db.close()


def print_cars_and_win_race_ratio():
    # printing car name & the ratio of races to races won
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    # option of whether it should be ordered or not and if so how
    user_input_order = input("""Ordered by:
        1. Car name
        2. Races competed in
        3. Races won
        4. Disregard
                """)
    if user_input_order == '1':
        sql = 'SELECT * FROM cars ORDER BY car_name;'
    elif user_input_order == '2':
        sql = 'SELECT * FROM cars ORDER BY races DESC;'
    elif user_input_order == '3':
        sql = 'SELECT * FROM cars ORDER BY wins DESC;'
    elif user_input_order == '4':
        sql = 'SELECT * FROM cars;'
    else:
        # catches invalid options and returns the user back to the main menu
        print(invalid_input_response)
        return
    # printing the stuff
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""Car ID   Car name                             Races  Wins""")
    for car in results:
        print(f"{car[0]:<3} {car[1]:<38} {car[3]:<3}: {car[4]:<4}")
    db.close()


# Main body of code + user interface AKA main menu
while True:
    user_input = input("""
What would you like to do?
    1. Print all racecar stats
    2. Print only car names
    3. Print only car names and horsepower
    4. Print only car names and races and wins ratio
    5. Exit

    """)
    if user_input == '1':
        print_all_cars()
    elif user_input == '2':
        print_car_names()
    elif user_input == '3':
        print_cars_and_hp()
    elif user_input == '4':
        print_cars_and_win_race_ratio()
    elif user_input == '5':
        print("""
              Goodbye

            （￣︶￣）↗""")
        break
    # Catches invalid inputs and brings user back to start of 'while true' loop
    else:
        print(invalid_input_response)
