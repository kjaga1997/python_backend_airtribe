# Library Manager

## Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

`LibraryItem` is an abstract base class because every item must have a `late_fee()` method, but books, magazines, and DVDs charge different rates. Marking `late_fee()` with `@abstractmethod` means Python will not allow a subclass to be created until that method is written. If `DVD` forgets `late_fee()`, creating a `DVD(...)` raises `TypeError` and the object is never made.

## What happens when you read item.__available from outside the class, and why do we use is_available() instead?

`__available` is a private member of the classes, so calling item.__available is not allowed and raises an error. `is_available()` is the method other code should call, so the class can check availability without letting callers change the private flag directly.

## What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is one class attribute shared by every book, magazine, and DVD. It goes up by one each time any item is created, so `Book.total_items` and `DVD.total_items` refer to the same count. `self.title` is an instance attribute, so each object keeps its own title and changing one item's title does not change the others.
