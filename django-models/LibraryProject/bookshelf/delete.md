from bookshelf.models import Book
print(f"Before: {Book.objects.count()} books")
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(f"After: {Book.objects.count()} books")