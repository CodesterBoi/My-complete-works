
import sys
class Library:
      def __init__(self,listofbooks): 
            self.availablebooks=listofbooks
#Creating the library and necessary objects.
      def displayAvailablebooks(self):
            print('The books we have in our library are as follows:')
            for book in self.availablebooks:
                         print(book)

      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print('The book you requested has now been borrowed.')
                  self.availablebooks.remove(requestedBook)
            else:
                  print('Sorry the requested book is currently not in the library.')
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print('Thank you for returning your borrowed book.')

#Student class created to borrow and return the book.
class Student:
      def requestBook(self):
            print('Enter the name of the book you would like to borrow:')
            self.book = input()
            return self.book

      def returnBook(self):
            print('Enter the name of the book you would like to return:')
            self.book = input()
            return self.book

def main():            
      library=Library(['The 10X rule', 'The Wolf of Wall Street', 'The Fifth Vital'])
      #Available books currently at library.
      student = Student()
      done = False
      while done == False:
            print('''==========LIBRARY MENU==========
                1. Display all available books.
                2. Request a book.
                3. Return a book.
                4. Exit.
                ''')
#This is for entering the desired option.
            choice=int(input("Enter Choice:"))
            if choice==1:
                     library.displayAvailablebooks()
            elif choice==2:
                    library.lendBook(student.requestBook())
            elif choice==3:
                    library.addBook(student.returnBook())
            elif choice==4:
                sys.exit()
                  
main()
