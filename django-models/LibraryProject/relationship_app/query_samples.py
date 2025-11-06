# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    """
    This function contains sample queries demonstrating the relationships
    """
    
    print("=== Sample Queries for Relationship App ===\n")
    
    # Query 1: Query all books by a specific author
    print("1. Query all books by a specific author:")
    try:
        # Get an author (assuming at least one exists)
        author = Author.objects.first()
        if author:
            books_by_author = Book.objects.filter(author=author)
            print(f"   Books by {author.name}:")
            for book in books_by_author:
                print(f"   - {book.title}")
        else:
            print("   No authors found in database")
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    # Query 2: List all books in a library
    print("2. List all books in a library:")
    try:
        # Get a library (assuming at least one exists)
        library = Library.objects.first()
        if library:
            books_in_library = library.books.all()
            print(f"   Books in {library.name}:")
            for book in books_in_library:
                print(f"   - {book.title}")
        else:
            print("   No libraries found in database")
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    # Query 3: Retrieve the librarian for a library
    print("3. Retrieve the librarian for a library:")
    try:
        # Get a library (assuming at least one exists)
        library = Library.objects.first()
        if library:
            try:
                librarian = Librarian.objects.get(library=library)
                print(f"   Librarian for {library.name}: {librarian.name}")
            except Librarian.DoesNotExist:
                print(f"   No librarian found for {library.name}")
        else:
            print("   No libraries found in database")
    except Exception as e:
        print(f"   Error: {e}")
    print()

if __name__ == "__main__":
    sample_queries()