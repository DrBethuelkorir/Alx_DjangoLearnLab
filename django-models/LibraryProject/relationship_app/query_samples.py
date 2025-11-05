author = Author.objects.get(name="J.K. Rowling")
books = Book.objects.filter(author=author)

# Get a specific library
library = Library.objects.get(name="City Central Library")

# Get all books in that library
books = library.books.all()

print(f"Books in {library.name}:")
for book in books:
    print(f"- {book.title} by {book.author.name}")


library = Library.objects.get(name="City Central Library")
librarian = Librarian.objects.get(library=library)

print(f"Librarian for {library.name}: {librarian.name}")