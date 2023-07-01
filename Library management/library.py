

class User:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.password = password
        self.borrowbook = []
        self.ruturnbook = []
class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def borrow_book(self, book_name, user):
        for book in self.book_list:
            if book == book_name:
                if book == user.borrowbook:
                    print("Fast return the book")
                    return
                if self.book_list[book] == 0:
                    print("Book not available")
                    return
                self.book_list[book] -= 1
                user.borrowbook.append(book_name)
                print("You have borrowed the book")
                return
        print("Book not available in library")

    def return_book(self, book_name, user):
        for book in self.book_list:
            if book == book_name:
                if book == user.borrowbook:
                    self.book_list[book] += 1
                    user.borrowbook.remove(book_name)
                    user.ruturnbook.append(book_name)
                    print("book return successful")
                    return
                else: print("Thanks but onner boi nibona")
        print("ata amader library boi na!")
    
    def available_books(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book)

    def donate_book(self, book_name, amount):
        for book in self.book_list:
            if book == book_name:
                self.book_list[book] += amount
                return
        self.book_list[book_name] = amount
        print("Thanks for donating! You")

        






library = Library({"Bangla": 3, "English": 5, "Math": 4 })
alluser = []
currentUser = None


while True:
    if currentUser is None:
        print("Not logged in \n please log in or create a new(L/C)")
        command = input()
        if command == 'L':
            roll = int(input("Roll :"))
            password = input("Password :")
            match = False
            for user in alluser:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("Uset not found")
        else:
            name = input("Name :")
            roll = int(input("Roll :"))
            password = input("Password")
            found = False
            for user in alluser:
                if user.roll == roll and user.password == password:
                    found = True
            if found == True:
                print("vai koibar accoutn khulba")
                continue 
            else:      
                newUser = User(name, roll, password)
                alluser.append(newUser)
                currentUser = newUser

    else:
        print("Borrow Book")
        print("___________")
        print("1.Borrow Book")
        print("2.Return book")
        print("3.Borrowed Book list")
        print("4.Return book list")
        print("5.Available book ")
        print("6.Donet book")
        print("7.log out")

        choice = int(input("Please enter your choice :"))

        if choice == 1:
            bookname = input("Enter book name :")
            library.borrow_book(bookname, currentUser)
        elif choice == 2:
            bookname = input("Enter book name :")
            library.return_book(bookname, currentUser)
        elif choice == 3:
            print(currentUser.borrowbook)
        elif choice == 4:
            print(currentUser.ruturnbook)
        elif choice == 5:
            library.available_books()
        elif choice == 6:
            bookname = input("Enter book name :")
            amount = input("Enter amount :")
            library.donate_book(bookname,amount)
        elif choice == 7:
            currentUser = None


        
        

        
       


        




    