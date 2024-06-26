class Member:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def add_book(self, name):
        self.__books.append(name)

    def remove_book(self, name):
        self.__books.remove(name)

    def get_name(self):
        return self.__name

    def get_books(self):
        return self.__books.copy()
