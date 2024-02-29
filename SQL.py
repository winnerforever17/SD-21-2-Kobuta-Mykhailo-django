import sqlite3
from contextlib import closing


def create_tables():
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as c:
            c.execute('''
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    text TEXT NOT NULL
                )
            ''')


def add_article(title, text):
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as c:
            c.execute('''
                INSERT INTO articles (title, text) VALUES (?, ?)
            ''', (title, text))
            connection.commit()


def view_articles():
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as c:
            c.execute('''
                SELECT * FROM articles
            ''')
            articles = c.fetchall()
            for article in articles:
                print(article)


def delete_article(article_id):
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as c:
            c.execute('''
                DELETE FROM articles WHERE id=?
            ''', (article_id,))
            connection.commit()


create_tables()

while True:
    print("\nМеню:")
    print("1. Додати нову статтю")
    print("2. Переглянути статі")
    print("3. Видалити статтю")
    print("0. Вийти")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        title = input("Введіть заголовок статті: ")
        text = input("Введіть текст статті: ")
        add_article(title, text)
        print("Стаття додана!")

    elif choice == "2":
        print("\nУсі статі:")
        view_articles()

    elif choice == "3":
        article_id = int(input("Введіть ідентифікатор статті, яку ви хочете видалити: "))
        delete_article(article_id)
        print("Стаття видалена!")

    elif choice == "0":
        print("Програма завершена.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
