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


print_all_cars()
