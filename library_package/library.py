#Do not have IDs -> Do not support same book/member names!

from library_package.book import Book
from library_package.member import Member

class Library:
    def __init__(self, lib_name):
        self.__lib_name = lib_name
        self.__books = []
        self.__members = []
    

    #member API
    def addMember(self, member_name):
        if self.__member_exists(member_name) == True:
            print(f"Failed. Member {member_name} already exists")
            return False
        member = Member(member_name)
        self.__members.append(member)
        print(f"Success. Added member {member_name}")
        return True

    def removeMember(self, member_name):  
        for member in self.__members[:]:
            if  member.get_name() == member_name:
                if len(member.get_books()) > 0:
                    print(f"Failed. Member {member_name} has books")
                    return False
                self.__members.remove(member)
                print(f"Success. Removed member {member_name}")
                return True
        print(f"Failed. Member {member_name} does not exist")
        return False
        

    def lendBookToMember(self, book_name, member_name):
        if self.__member_exists(member_name) == False:
            print(f"Failed. Member {member_name} does not exist")
            return False
        for book in self.__books:
            if book.get_name() == book_name:
                if book.get_owner() is not None:
                    print(f"Failed. Book {book_name} already has owner")
                    return False
                book.set_owner(member_name)
                for member in self.__members:
                    if  member.get_name() == member_name:
                        member.add_book(book_name)
                print(f"Success. Lent book {book_name} to member {member_name}")
                return True
        print(f"Failed. Book {book_name} does not exist")
        return False

    def receiveBookFromMember(self, book_name, member_name):
        if self.__member_exists(member_name) == False:
            print(f"Failed. Member {member_name} does not exist")
            return False
        if self.__member_has_book(member_name, book_name) == False:
            print(f"Failed. Member {member_name} does not have a {book_name} book")
            return False
        for book in self.__books:
            if book.get_name() == book_name:
                book.set_owner(None)
                for member in self.__members:
                    if  member.get_name() == member_name:
                        member.remove_book(book_name) 
                print(f"Success. Received book {book_name} from member {member_name}")
                return True
        print(f"Failed. Book {book_name} does not exist") #Dead code!
        return False


    #Book API
    def addBook(self, book_name, author, year):
        if self.__book_exists(book_name) == True:
            print(f"Failed. Book {book_name} already exists")
            return False
        book = Book(book_name, author, year)
        self.__books.append(book)
        print(f"Success. Added book {book_name}")
        return True
    
    def removeBook(self, book_name):
        for book in self.__books[:]:
            if book.get_name() == book_name:
                if book.get_owner() is None:
                    self.__books.remove(book)
                    print(f"Success. Removed book {book_name}")
                    return True
                print(f"Failed. Book {book_name} has an owner")
                return False
        print(f"Failed. Book {book_name} does not exists")
        return False


    #Display API
    def printBooksInfo(self):
        print("BOOKS INFO")
        for book in self.__books:
            print(book.get_info())

    def printMembersInfo(self):
        print("MEMBERS INFO")
        for member in self.__members:
            name = member.get_name()
            books = member.get_books()
            print({"name":name, "books":books})

    
    #Tools
    def __book_exists(self, book_name):
        for book in self.__books:
            if book.get_name() == book_name:
                return True
        return False
    
    def __member_exists(self, member_name):
        for member in self.__members:
            if member.get_name() == member_name:
                return True
        return False

    def __member_has_book(self, member_name, book_name):
        for member in self.__members:
            if member.get_name() == member_name:
                member_books = member.get_books()
                for book in member_books:
                    if book == book_name:
                        return True
        return False
