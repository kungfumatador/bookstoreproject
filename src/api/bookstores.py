from flask import Blueprint, jsonify, abort, request
from ..models import Bookstores, db

bp = Blueprint('bookstores', __name__, url_prefix='/bookstores')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    bookstores = Bookstores.query.all()  # ORM performs SELECT query
    result = []
    for bookstore in bookstores:
        # build list of Authors as dictionaries
        result.append(bookstore.serialize())
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    bookstore = Bookstores.query.get_or_404(id)
    return jsonify(bookstore.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain name
    if 'name' not in request.json:
        return abort(400)
    # construct Bookstore entry
    bookstore = Bookstores(
        name=request.json['name'],
        city=request.json['city'],
        net_yearly_revenue=request.json['net_yearly_revenue'],
        number_of_books_in_stock=request.json['number_of_books_in_stock']
    )
    db.session.add(bookstore)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(bookstore.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    bookstore = Bookstores.query.get_or_404(id)
    try:
        db.session.delete(bookstore)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    bookstore = Bookstores.query.get_or_404(id)
    if 'name' in request.json:
        bookstore.name = request.json['name']
    if 'city' in request.json:
        bookstore.city = request.json['city']
    if 'net_yearly_revenue' in request.json:
        bookstore.net_yearly_revenue = request.json['net_yearly_revenue']
    if 'number_of_books_in_stock' in request.json:
        bookstore.number_of_books_in_stock = request.json['number_of_books_in_stock']
    db.session.commit()
    return jsonify(bookstore.serialize())
