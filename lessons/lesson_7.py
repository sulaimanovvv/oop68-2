import sqlite3

# A4
connect = sqlite3.connect("users.db")

# Карандаш с рукой
cursor = connect.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT 
    )
""")

connect.commit()


# CRUD Create-Read-Update-Delete


def create_user(name, age, hobby):
    # cursor.execute("""
    #         INSERT INTO user(name, age, hobby)
    #         VALUES ("{name}", "{age}", "{hobby}")
    #     """)
    cursor.execute(
        "INSERT INTO user(name, age, hobby) VALUES(?,?,?)", (name, age, hobby)
    )
    connect.commit()
    print("пользователь создан")


# create_user("Ardager", 20, "Горы-лыжы")
# create_user("Faruh", 21, "Горы")
# create_user("Imran", 22, "Sleep")
# create_user("Oleg", 23, "Play")
# create_user("Petya", 24, "tennis")


def read_users():
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    print(data)
    for i in data:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")


read_users()


def update_user(new_name, old_name):
    cursor.execute("UPDATE user SET name = ? WHERE name = ?", (new_name, old_name))
    connect.commit()
    print("user update!")


# update_user("Ардагер", "Ardager")


def delete_user(id):
    cursor.execute("DELETE FROM user WHERE id = ?", (id,))
    connect.commit()
    print("user deleted")


delete_user(3)
