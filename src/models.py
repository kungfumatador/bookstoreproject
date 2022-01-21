from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships

class Employees(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    salary = db.Column(db.Integer)
    years_employed = db.Column(db.Integer)
    bookstore_id = db.Column(db.Integer, db.ForeignKey(
        'bookstores.bookstore_id'), nullable=False)

    def __init__(self, name: str, salary: int, years_employed: int):
        self.name = name
        self.salary = salary
        self.years_employed = years_employed

    def serialize(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'salary': self.salary,
            'years_employed': self.years_employed,
        }


class Books(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    author_name = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.String(128))
    price = db.Column(db.Float)

    def __init__(self, title: str, author_name: str, genre: str, price: int, author_id: int):
        self.title = title
        self.author_name = author_name
        self.genre = genre
        self.price = price
        self.author_id = author_id

    def serialize(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author_name': self.author_name,
            'genre': self.genre,
            'price': self.price,
            'author_id': self.author_id
        }


books_bookstores = db.Table(
    'books_bookstores',
    db.Column(
        'isbn', db.BigInteger,
        db.ForeignKey('books.isbn'),
        primary_key=True
    ),
    db.Column(
        'bookstore_id', db.Integer,
        db.ForeignKey('bookstores.bookstore_id'),
        primary_key=True
    )
)


class Bookstores(db.Model):
    __tablename__ = 'bookstores'
    bookstore_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(255))
    net_yearly_revenue = db.Column(db.Integer)
    number_of_books_in_stock = db.Column(db.Integer)

    def __init__(self, name: str, city: str, net_yearly_revenue: int, number_of_books_in_stock: int):
        self.name = name
        self.city = city
        self.net_yearly_revenue = net_yearly_revenue
        self.number_of_books_in_stock = number_of_books_in_stock

    def serialize(self):
        return {
            'bookstore_id': self.bookstore_id,
            'name': self.name,
            'city': self.city,
            'net_yearly_revenue': self.net_yearly_revenue,
            'number_of_books_in_stock': self.number_of_books_in_stock,
        }


class Managers(db.Model):
    __tablename__ = 'managers'
    manager_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    years_employed = db.Column(db.Integer)
    bookstore_id = db.Column(
        db.Integer, db.ForeignKey('bookstores.bookstore_id'))
    bookstore = db.relationship(
        "Bookstores", backref=db.backref("managers", uselist=False))

    def __init__(self, name: str, age: int, salary: int, years_employed: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.years_employed = years_employed

    def serialize(self):
        return {
            'manager_id': self.manager_id,
            'name': self.name,
            'age': self.age,
            'salary': self.salary,
            'years_employed': self.years_employed,
            'bookstore_id': self.bookstore_id
        }
