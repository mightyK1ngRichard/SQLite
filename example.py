# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from SQL_class import DataBase


def main():
    db = DataBase('boss', [('user_id', 'integer'), ('name', 'text')])
    # -- Добавление и обновление.
    names = ['Dima', 'Vova', 'Stas', 'Nick', 'Tom']
    for count, el in enumerate(names):
        db.add_data(count, el)

    db.update_param_of_data('user_id', '1', [('user_id', 555), ('name', 'Messi')])
    db.update_param_of_data('name', 'Messi', [('user_id', 555), ('name', 'Messi')])

    # -- Получение данных.
    print(db.get_all_data_of_user('user_id', '2'))
    print(db.get_data_with_param('user_id', '2', 'name'))
    print(db.get_table_data())

    # -- Удаление данных.
    # db.delete_data_with_param('name', 'Dima')
    # db.update_param_of_data('user_id', '2', [('user_id', 23), ('name', 'help')])
    # db.delete_all_data()


if __name__ == '__main__':
    main()
