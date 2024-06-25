class Book:
    def __init__(self, name, author, year):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__owner = None

    def get_info(self):
        return {
            "name":   self.__name,
            "author": self.__author,
            "year":   self.__year,
            "owner":  self.__owner,
        }

    def get_name(self):
        return self.__name
    
    def get_owner(self):
        return self.__owner

    def set_owner(self, name):
        self.__owner = name
