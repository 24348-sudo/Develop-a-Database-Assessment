import sqlite3

# functions


def print_all_cars():
    # printing car name, hp, races competed in + won & maker
    db = sqlite3.connect('best_racecars.db')
    cursor = db.cursor()
    sql = 'SELECT * FROM cars;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print("""Car""")
    for car in results:
        print(car)
    db.close()


while True:
    user_input = input("""What would you like to do?
    1. Print all racecar stats
    2. Print car names
    3. Print car names and their horsepower
    4. Print car names and the races competed in
    5. Exit

    """)
    if user_input == '1':
        print_all_cars()
    elif user_input == '5':
        break
