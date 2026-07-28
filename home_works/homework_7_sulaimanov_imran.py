import sqlite3

connect = sqlite3.connect("store.db")

cursor = connect.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )       
        """)

connect.commit()


def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products(name, price, quantity) VALUES(?, ?, ?)",
        (name, price, quantity),
    )
    connect.commit()
    print(f"Товар '{name}' создан")


def read_products():
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    print("\n---- ТЕКУЩИЙ СПИСОК ТОВАРОВ ----")
    for i in data:
        print(f"ID: {i[0]} | Название: {i[1]} | Цена: {i[2]} |  Количество: {i[3]} шт")

    print("===============================\n")


def update_product(id, price):
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))
    connect.commit()
    print(f"Цена товара с ID {id} успешно обновлена!")


def delete_product(id):
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    connect.commit()
    print(f"Товар с ID {id} удален")


create_product("Пиджак женский", 7500, 20)
create_product("Брюки женские", 3490, 15)
create_product("Юбка женская", 3000, 33)

read_products()

# update_product(2, 3500)

# delete_product(3)
