#Do not have IDs. Do not support same book/member names!

from library_package.library import Library

mcr_lib = Library("Manchester Library")

mcr_lib.addBook("To Kill a Mockingbird",  "Harper Lee",       1960)
mcr_lib.addBook("1984",                   "George Orwell",    1949)
mcr_lib.addBook("Pride and Prejudice",    "Jane Austen",      1813)
mcr_lib.addBook("The Great Gatsby",       "Scott Fitzgerald", 1925)
mcr_lib.addBook("The Catcher in the Rye", "J.D. Salinger",    1951)
mcr_lib.addBook("War and Peace",          "Leo Tolstoy",      1869)

mcr_lib.removeBook("War is Peace") #FAIL
mcr_lib.removeBook("War and Peace")

mcr_lib.addMember("Alice Johnson")
mcr_lib.addMember("Robert Smith")
mcr_lib.removeMember("Non Exist")  #FAIL

mcr_lib.lendBookToMember("1984", "Alice Johnson")
mcr_lib.lendBookToMember("1984", "Robert Smith") #FAIL
mcr_lib.lendBookToMember("1984", "Non Exist") #FAIL

mcr_lib.receiveBookFromMember("1984", "Robert Smith") #FAIL
mcr_lib.receiveBookFromMember("1984", "Alice Johnson")

mcr_lib.lendBookToMember("The Great Gatsby", "Alice Johnson")
mcr_lib.lendBookToMember("To Kill a Mockingbird", "Alice Johnson")

mcr_lib.printBooksInfo()
mcr_lib.printMembersInfo()
