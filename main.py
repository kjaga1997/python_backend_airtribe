# main.py
from models import Book,Magazine,DVD, Member  # TODO: also import Magazine, DVD
book = Book("Python 101", 1, "A. Rao")
# TODO: create one Magazine and one DVD
magazine = Magazine("test magazine", 2, 1)
dvd = DVD("test dvd", 3, 120)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)
# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)
# 2. TODO: trigger the borrow-limit error and the not-borrowed error, catching each
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)
    print("Bob borrowed:", dvd.describe())
except ValueError as e:
    print("Could not borrow:", e)
try:
    bob.return_item(dvd)
    print("Bob returned:", dvd.describe())
except ValueError as e:
    print("Could not return:", e)

# 3. Polymorphism: one loop, no type checks
items = [book,magazine,dvd]  # TODO: add the magazine and the DVD
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)