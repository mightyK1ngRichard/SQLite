# SQLite
<img src="https://img.shields.io/github/license/DimaPermyakov/IU5?color=brightgreen" alt="MIT License"> <img src="https://img.shields.io/badge/language-Python-blue.svg" alt="Python Language"> <img src="https://img.shields.io/badge/language-SQLite-red.svg" alt="SLQ">

* [Class implementation](https://github.com/mightyK1ngRichard/SQLite/blob/main/SQL_class.py)

# Methods of the class:
```python
def add_data(self, *args) -> bool:
    """
    Добавляет пользователя в таблицу, если его ещё нет.
    :param args: Новые данные таблицы.
    :return: Добавил ли он пользователя? Да, нет.
    """

def update_param_of_data(self, title_for_search: str, param_for_search, new_titles_and_params: list) -> bool:
    """ Пример использования: db.update_param_of_data('user_id', '2', [('user_id', 23), ('name', 'help')]).
    :param title_for_search: название заголовка в таблице для поиска.
    :param param_for_search: значение заголовка изначальное.
    Пример: найти пользователя с id = 2. user_id - title_for_replace, 2 - param_for_replace.
    :param new_titles_and_params: список картежей с данными.
    :return: Вышло или нет.
    """

def delete_all_data(self) -> bool:
    """ Удаляет всё содержимое таблицы. """

def delete_data_with_param(self, title_name: str, param_of_title):
    """ Удаляет по пользователя с определенным параметром для поиска.
    :param title_name: Заголовок таблицы.
    :param param_of_title: Параметр заголовка.
    """

def delete_table(self):
    """Удаляет файл таблицы."""

def presence(self, name_title, param_of_title) -> bool:
    """ Проверка присутствия в бд.
    :param name_title: Название заголовка таблицы.
    :param param_of_title: Аргумент поиска.
    :return: True / False
    """

def get_all_data_of_user(self, title_name: str, param_of_title) -> list:
    """Возвращает все данные.
    :param title_name: Имя заголовка.
    :param param_of_title: Параметр заголовка.
    :return: список данных.
    """

def get_data_with_param(self, title_for_search: str, param_of_title_for_search, title_expect: str) -> list:
    """ Получить данные заголовка, который просят.
    Пример: db.get_data_with_param('user_id', '0', 'name')
    :param title_for_search: заголовок для поиска.
    :param param_of_title_for_search: параметр заголовка для поиска.
    :param title_expect: заголовок, значение которого ожидаем.
    :return: Список данных.
    """

def get_table_data(self):
    """Возвращает содержимое таблицы."""
```
