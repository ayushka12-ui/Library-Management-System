# Library Management System

A command-line library management system built in Python as part of a structured Python fundamentals roadmap (Project 2 of 4).

## Features

- **Add a new book** — store title, author, genre, and ISBN
- **View all books** — see full details of every book in the library
- **Check book status** — look up a book by ISBN to see if it's available or issued, who it's issued to, and how many days remain (or how overdue it is)
- **Issue a book** — mark a book as borrowed by a specific person, with today's date recorded automatically
- **Return a book** — return an issued book, with automatic fine calculation for overdue returns

## Concepts Practiced

- Object-oriented programming — a Book class with its own attributes and methods
- Distinguishing methods (actions on one object's own data, e.g. issue()) from functions (actions across a whole collection, e.g. view_books())
- Dictionaries as a data store, keyed by ISBN for direct lookup
- The datetime module — capturing real dates and calculating elapsed time between two dates
- Menu-driven program flow using while True and if/elif

## Library Rules

- Loan period: 15 days
- Late fine: ₹50 per day overdue

## How to Run

python Library_Management_System.py

## Menu Options

1. Add a new Book
2. View all book details
3. Book status
4. Issue Book
5. Return book
6. Exit

## Project Status

Core functionality complete: add, view, issue, status check, and return (with fine calculation) are all implemented and tested.

Not yet implemented (intentionally scoped out for now):
- Search by title/author/genre — largely covered by existing view/status options
- Multiple copies per title (quantity tracking) — would require restructuring Book to track individual copies separately; noted as a possible future extension
