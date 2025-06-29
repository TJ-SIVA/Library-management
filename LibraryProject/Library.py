from Member import Member
from book import Books 
class Library:
    
    """ A class is perfoming add,remove of member and books operations and finding books 
        and members of an library"""
        
    def __init__(self):
        
        """  initializing list of books and members """
        
        self.books = []
        self.members = [] 
        
    def add_member(self,member_name :str ,member_id : int,member_address = None ) -> str :
        
        """ A funtion that add member of an library with the details of name,id,address of an member
        """
        self.member_name=member_name
        member = Member(member_name,member_id,member_address) #object cration of member class
        self.members.append(member) # adding members
        return f"The member {self.member_name} was added..." 
        
    def remove_member(self,member_name,member_id):
        
        ''' A function that remove user form an library '''
        self.member_name = member_name
        self.member_id = member_id
        
        for member in self.members:
            if member.member_id == self.member_id :
                if member.Borrowed_Books == [] :
                    self.members.remove(member) #remvoes member form an member list
                    print(f"The member {self.member_name} removed ")
                else:
                    print(f"The member {self.member_name} is not returned {member.Borrowed_books} thus, he/she should return those books before removel ")
            else:
                print(f"The member not found")
                
    def find_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return f"{member.member_name}"
            else:
                print(f"the member {member.member_id} is not found ")
                print("Enter valid member id....")
                
    def add_book(self,Book_name,Book_sno,Author):
        ''' A funtion for adding books '''
        book = Books(Book_name,Book_sno,Author)
        self.books.append(book) # adding book in books list
        
    def remove_book(self,Book_sno):
        ''' A funtion for remove books from library'''
        self.Book_sno = Book_sno
        for book in self.books:
            if book.Book_sno == Book_sno:
                if book.is_available:
                    self.books.remove(book)
                    print(f"The book {self.Book_sno} was removed from library")
                else:
                    print(F"The Book {self.Book_sno} was borrowed it should not be removed " )  
            else:
                print("The book was not found...")  
                
    def find_book(self,book_sno):
        
        ''' A function responsible for findig books'''
        for book in self.books:
            if book.Book_sno == book_sno:
                if book.is_available:
                    print(f"The book {book.Book_title} by {book.Author} was available")
                else:
                    print(f"The book {book.Book_title} by {book.Author} was available")  
            else:
                print("The require book is not available")          
                
    def __str__(self):
        books = "\n".join([str(book) for book in self.books]) or "No books in library."
        members = "\n".join([str(member) for member in self.members]) or "No members registered."
        return f"Library Books:\n{books}\n\nLibrary Members:\n{members}"
    
            
    
        
        
