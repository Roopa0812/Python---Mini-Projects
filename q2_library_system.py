# Q2 - Library Book Management System
# Demonstrates using the right data structure for the right job:
#   dict  -> catalog (fast lookup by book_id)
#   tuple -> book details (immutable, shouldn't change once added)
#   list  -> borrowed_books (order of borrowing matters)
#   set   -> members (no duplicate member IDs allowed)


def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    # only allow borrowing if the book exists and is not already borrowed
    if book_id not in catalog:
        print(f"Book ID {book_id} does not exist in catalog.")
        return

    if book_id in borrowed_books:
        print(f"Book ID {book_id} is already borrowed.")
        return

    borrowed_books.append(book_id)
    print(f"Borrowed: {catalog[book_id][0]}")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Returned book ID {book_id}.")
    else:
        print(f"Book ID {book_id} was not marked as borrowed.")


def register_member(members, member_id):
    # set automatically ignores duplicates
    if member_id in members:
        print(f"Member {member_id} already registered. Skipping.")
    else:
        members.add(member_id)
        print(f"Member {member_id} registered.")


def show_available(catalog, borrowed_books):
    print("Available books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"  [{book_id}] {title} by {author} ({year})")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # add 4 books
    add_book(catalog, 1, "Atomic Habits", "James Clear", 2018)
    add_book(catalog, 2, "The Alchemist", "Paulo Coelho", 1988)
    add_book(catalog, 3, "Deep Work", "Cal Newport", 2016)
    add_book(catalog, 4, "Sapiens", "Yuval Noah Harari", 2011)

    # register 3 members, try adding one twice
    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")
    register_member(members, "M001")  # duplicate, should be ignored

    print("Members:", members)

    # borrow 2 books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    # try borrowing an already borrowed book, to show the check works
    borrow_book(catalog, borrowed_books, 1)

    # return 1 book
    return_book(borrowed_books, 1)

    # what's left available
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()
