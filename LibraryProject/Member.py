class Member:
    ''' A class with performs the operations related to an members'''
    
    def __init__(self, member_name : str , member_id : int , member_address = None):
        
        #initializing variables
        
        self.member_name = member_name
        self.member_id = member_id
        self.member_address = member_address
        
        #creating a list for borrowed books
        
        self.Borrowed_Books = []
        
    def borrow_books(self,book):
        ''' A function manages a borrow operation '''
        
        if book.is_available:
            book.is_available = False
            self.Borrowed_Books.append(book)
            print(f"The book {book.Book_name} 'Borrowed' by {self.member_name}")
        else:
            print(f"The book {book.Book_name} is Unavailable")
            
    def return_book(self,book):
        ''' A function manages a return operation of books '''
        
        for book in self.Borrowed_Books:
            if book.is_available == False:
                book.is_available = True 
                print(f"The {self.member_name} 'Returned' {book.Book_name}")
            else:
                print(f"The book {book.Book_name} is not Borrowed by {self.member_name}")
             
    def __str__(self):
        
        ''' A magic function that return object as a string representation'''
        
        Borrowed_Books = "\n".join([book.title for book in self.Borrowed_Books]) or "No books Borrowed"
        return f"member: {self.member_name} id: {self.member_id}| Borrowed:{Borrowed_Books}" # return list of books borrowed by an member
            
            
        
        
    
    
    
    
    