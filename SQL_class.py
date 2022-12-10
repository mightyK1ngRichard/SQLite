# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import sqlite3
import os


class DataBase:
    """Класс для работы с SQL таблицами."""
    def __init__(self, filename: str, titles: list, path: str = None):
        """ Пример вызова: DataBase('boss', [('user_id', 'integer'), ('name', 'text')]).
        :param filename: имя файла.
        :param titles: заголовки файла и формат. Пример: [('id', 'integer'), ('name', 'text')]
        :param path: Путь к файлу.
        """
        self._filename = filename
        self._path = path if path is not None else f'{filename}.db'
        self._titles = titles
        db = sqlite3.connect(self._path)
        cursor = db.cursor()
        try:
            cursor.execute(f'CREATE TABLE {filename} (' + ', '.join(f'{el[0]} {el[1]}' for el in titles).strip() + ')')

        except:
            print(' >> Table is created')
        db.commit()
        db.close()

    def add_data(self, *args) -> bool:
        """
        Добавляет пользователя в таблицу, если его ещё нет.
        :param args: Новые данные таблицы.
        :return: Добавил ли он пользователя? Да, нет.
        """
        try:
            if not self.presence(self._titles[0][0], args[0]):
                db = sqlite3.connect(self._path)
                cursor = db.cursor()
                data = ', '.join(
                    map(lambda el: str(el) if type(el) in [int, float] else f'\'{el.lower()}\'', args)).strip()
                try:
                    cursor.execute(f"INSERT INTO {self._filename} VALUES (" + data + ')')

                except:
                    print(f' >> ERROR FROM {DataBase.add_data.__name__}')

                db.commit()
                db.close()
                return True

            else:
                print(f' >> METHOD "{DataBase.add_data.__name__}": user already is created')
                return False

        except:
            print(f' >> ERROR FROM METHOD "{DataBase.add_data.__name__}"')
            return False

    def update_param_of_data(self, title_for_search: str, param_for_search, new_titles_and_params: list) -> bool:
        """ Пример использования: db.update_param_of_data('user_id', '2', [('user_id', 23), ('name', 'help')]).
        !! ВАЖНО !! ОТСЛЕЖИВАЙТЕ, ЧТОБЫ ВЫ НЕ ПОМЕНЯЛИ id на уже существующий.
        :param title_for_search: название заголовка в таблице для поиска.
        :param param_for_search: значение заголовка изначальное.
        Пример: найти пользователя с id = 2. user_id - title_for_replace, 2 - param_for_replace.
        :param new_titles_and_params: список картежей с данными.
        :return: Вышло или нет.
        """
        if title_for_search not in [el[0] for el in self._titles]:
            print(' >> TITLE NOT FOUND')
            return False

        for title, data in new_titles_and_params:
            if title in self._titles[0] and self.presence(title, data):
                print(f'ID {data} ALREADY EXISTS')
                return False

        try:
            for title, new_data in new_titles_and_params:
                db = sqlite3.connect(self._path)
                cursor = db.cursor()
                try:
                    cursor.execute(f"""UPDATE {self._filename} 
                    SET {title} = {new_data if type(new_data) in [int, float] else f"'{new_data.lower()}'"} 
                    WHERE {title_for_search} = {param_for_search if type(param_for_search) in [int, float] else f"'{param_for_search.lower()}'"}""")
                    if title == title_for_search:
                        param_for_search = new_data

                except:
                    print(f' >> ERROR FROM METHOD {DataBase.update_param_of_data.__name__}')

                db.commit()
                db.close()
            return True

        except:
            print(f' >> ERROR FROM METHOD "{DataBase.add_data.__name__}"')
            return False

    def delete_all_data(self) -> bool:
        """ Удаляет всё содержимое таблицы. """
        try:
            db = sqlite3.connect(self._path)
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM {self._filename}")
            db.commit()
            db.close()
            return True

        except:
            print(f' >> ERROR FROM METHOD "{DataBase.add_data.__name__}"')
            return False

    def delete_data_with_param(self, title_name: str, param_of_title):
        """ Удаляет по пользователя с определенным параметром для поиска.
        :param title_name: Заголовок таблицы.
        :param param_of_title: Параметр заголовка.
        :return:
        """
        if title_name not in [el[0] for el in self._titles]:
            print(' >> TITLE NOT FOUND')
            return False

        try:
            if self.presence(title_name, param_of_title):
                db = sqlite3.connect(self._path)
                cursor = db.cursor()
                cursor.execute(f"""DELETE FROM {self._filename} 
                WHERE {title_name} = {param_of_title if type(param_of_title) in [int, float] else f"'{param_of_title.lower()}'"}""")
                db.commit()
                db.close()
                return True
            else:
                print(f' >> METHOD "{DataBase.delete_data_with_param.__name__}", user not found')
                return False

        except:
            print(f' >> ERROR FROM METHOD "{DataBase.delete_data_with_param.__name__}"')
            return False

    def delete_table(self):
        """Удаляет файл таблицы."""
        try:
            os.remove(self._path)

        except:
            print(f' >> ERROR FROM METHOD "{DataBase.delete_table.__name__}"')

    def presence(self, name_title, param_of_title) -> bool:
        """
        :param name_title: Название заголовка таблицы.
        :param param_of_title: Аргумент поиска.
        :return: True|False
        """
        try:
            db = sqlite3.connect(self._path)
            cursor = db.cursor()
            cursor.execute(f"""SELECT {name_title} FROM {self._filename} 
            WHERE {name_title} = {param_of_title if type(param_of_title) in [int, float] else f"'{param_of_title.lower()}'"}""")
            res = cursor.fetchall()
            db.commit()
            db.close()
            return True if len(res) != 0 else False

        except:
            print(f' >> ERROR FROM {DataBase.presence.__name__} WITH {name_title}')
            return False

    def get_all_data_of_user(self, title_name: str, param_of_title) -> list:
        """Возвращает все данные.
        :param title_name: Имя заголовка.
        :param param_of_title: Параметр заголовка.
        :return: список данных.
        """
        if title_name not in [el[0] for el in self._titles]:
            print(f' >> TITLE NOT FOUND. METHOD {DataBase.get_all_data_of_user.__name__}')
            return []

        if not self.presence(title_name, param_of_title):
            print(f' >> PERSON NOT FOUND. METHOD {DataBase.get_all_data_of_user.__name__} WITH {param_of_title}')
            return []

        try:
            db = sqlite3.connect(self._path)
            cursor = db.cursor()
            cursor.execute(f"""SELECT * FROM {self._filename} 
            WHERE {title_name} = {param_of_title if type(param_of_title) in [int, float]
            else f"'{param_of_title.lower()}'"}""")
            res = cursor.fetchall()
            db.commit()
            db.close()
            return list(*res)

        except:
            print(f' >> ERROR FROM {DataBase.get_all_data_of_user.__name__} WITH {param_of_title}')
            return []

    def get_data_with_param(self, title_for_search: str, param_of_title_for_search, title_expect: str):
        """ Получить данные заголовка, который просят.
        Пример: db.get_data_with_param('user_id', '0', 'name')
        :param title_for_search: заголовок для поиска.
        :param param_of_title_for_search: параметр заголовка для поиска.
        :param title_expect: заголовок, значение которого ожидаем.
        :return:
        """
        if title_for_search not in [el[0] for el in self._titles]:
            print(f' >> TITLE NOT FOUND. METHOD {DataBase.get_data_with_param.__name__}')
            return []

        try:
            db = sqlite3.connect(self._path)
            cursor = db.cursor()
            cursor.execute(f"""SELECT {title_expect} FROM {self._filename} 
            WHERE {title_for_search} = {param_of_title_for_search if type(param_of_title_for_search) in [int, float]
            else f"'{param_of_title_for_search.lower()}'"}""")
            res = cursor.fetchall()
            db.commit()
            db.close()
            return list(*res)

        except:
            print(f' >> ERROR FROM {DataBase.get_all_data.__name__} WITH {param_of_title_for_search}')
            return []

    def get_table_data(self):
        """Возвращает содержимое таблицы."""
        try:
            db = sqlite3.connect(self._path)
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM {self._filename}")
            # cursor.execute(f"""-- SELECT * FROM {self._filename}""")
            res = cursor.fetchall()
            db.commit()
            db.close()

            return [el for el in res]

        except:
            print(f' >> ERROR FROM {DataBase.get_table_data.__name__}')
            return []


if __name__ == '__main__':
    pass

'''
db = sqlite3.connect('../data/users.db')
cursor = db.cursor()
--- Создание.
db = sqlite3.connect('../data/users.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE users (
    id_user integer,
    name text,
    age integer,
    place text,
    university text,
    department text,
    description text,
    photo text
)""")
db.commit()
db.close()
--- Добавление данных.
cursor.execute("INSERT INTO users VALUES (0, 'Richard', 19, 'Moscow', 'IU5', 'I like only two things: coffee and my GitHub: https://github.com/mightyK1ngRichard')")
--- Выборка данных.
ИЛИ cursor.execute("SELECT * FROM users")
cursor.execute("SELECT rowid, name FROM users")
cursor.execute("SELECT rowid, * FROM users")
for el in cursor.fetchall():
    print(el)
--- Условия выборки.
cursor.execute("SELECT rowid, * FROM users WHERE id_user = 0")
for el in cursor.fetchall():
    print(el)
--- Удаление данных.
cursor.execute("DELETE FROM users") - Удалить всё.
cursor.execute("DELETE FROM users WHERE id_user = 1 ") - Удалить по условию.
--- Обновление данных.
cursor.execute("UPDATE users SET name = 'mightyRichard' WHERE id_user = 0")
db.commit()
db.close() 
'''
