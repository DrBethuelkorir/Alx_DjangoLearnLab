#Query all books by a specific author.
from models.py import Book,Library
def run:

    byspecifautho = Book.objects.filter(name="kiptoo")
    print(byspecifautho)

    #to lst all books in a library
    name = Library.object.get(name="library")
    allbooks = Library.objects.all()
    print(allbooks)

