import sqlite3

# functions


def print_all_cars():
    # printing car name, hp, races competed in + won & maker
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    sql = 'SELECT * FROM cars;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""   Cars                                 HP  Races  Wins""")
    for car in results:
        print(f"{car[1]:<38} {car[2]:<6} {car[3]:<4} {car[4]:<4}")
    db.close()


def print_car_names():
    # printing car names
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    sql = 'SELECT * FROM cars;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""    Cars""")
    for car in results:
        print(f"{car[1]}")
    db.close()


def print_cars_and_hp():
    # printing car names and horsepower
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    sql = 'SELECT * FROM cars;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""   Cars                                 HP""")
    for car in results:
        print(f"{car[1]:<38} {car[2]:<6}")
    db.close()


def print_cars_and_race_ratio():
    # printing car name &  races competed in + won & maker
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    sql = 'SELECT * FROM cars;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""   Cars                               Races  Wins""")
    for car in results:
        print(f"{car[1]:<38} {car[3]:<3}: {car[4]:<4}")
    db.close()


while True:
    user_input = input("""
What would you like to do?
    1. Print all racecar stats
    2. Print car names
    3. Print car names and horsepower
    4. Print car names and races and wins ratio
    5. Exit

    """)
    if user_input == '1':
        print_all_cars()
    elif user_input == '2':
        print_car_names()
    elif user_input == '3':
        print_cars_and_hp()
    elif user_input == '4':
        print_cars_and_race_ratio()
    elif user_input == '5':
        break
    else:
        print()
