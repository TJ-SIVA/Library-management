class Books:

    ''' A class is contain a function and operation related with books '''
    def __init__(self,Book_title : str,Book_sno :int , Author : str,):
       #intializing variables
       self.Book_title = Book_title
       self.Book_sno = Book_sno
       self.Author = Author
       self.is_available = True 
    
    def __str__(self):
        
        status = "available" if self.is_available else "Borrowed"
        return f"The {self.Book_title} by {self.Author} is - {status}" 
        
    