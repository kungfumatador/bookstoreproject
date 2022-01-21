Read Me For Bookstore Database

A database for storing information about bookstores, bookstore managers, books that the bookstore may have in stock, and details about the authors.

API Table:
| Name   | Method    | URL                                  | Description                                      |
|:------:|:---------:|:------------------------------------:|:------------------------------------------------:|
| index  | GET       | http://localhost:5000/bookstores     | Gets a sample of rows from the bookstores table  |
| show   | GET       | http://localhost:5000/bookstores/:id | Gets a specific row from the bookstores table    |
| create | POST      | http://localhost:5000/bookstores     | Creates a new row for the bookstores table       |
| delete | DELETE    | http://localhost:5000/bookstores/:id | Deletes a row from the bookstores table          |
| update | PATCH PUT | http://localhost:5000/bookstores/:id | Replaces data in a row/s in the bookstores table |

Retrospective answering of the following questions:
How did the project's design evolve over time?
Since the project called for a one-to-one, many-to-one, and many-to-many relationship between tables I decided four tables would cover all three types of relation.  I chose managers to bookstores for the one-to-one relation since there would only be one manager for one bookstore.  I chose a books to authors relation for the many-to-one relation.  I realize that books can have more than one author but I took liberties with reality for the purposes of this project.  I chose books to bookstores for the many-to-many relation because many bookstores can be have the same book title in stock.

Did you choose to use an ORM or raw SQL? Why?
I went with ORM because I felt it was the most challenging for me and I wanted to get some practice using it.

What future improvements are in store, if any?
I originally created the authors table so I could have a many to one relation with books.  Since this was meant to be more focused on bookstores I realized late into the project that I should have included an employees table with a many to one relation with the bookstores table instead.# bookstoreproject
