"""empty message

Revision ID: d8eaba83c8dd
Revises: 4996e60176be
Create Date: 2022-01-11 17:43:52.715243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8eaba83c8dd'
down_revision = '4996e60176be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('author_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('number_of_books_written', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.create_table('books',
    sa.Column('isbn', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('author_name', sa.String(length=128), nullable=False),
    sa.Column('genre', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('bookstore_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors.author_id'], ),
    sa.ForeignKeyConstraint(['bookstore_id'], ['bookstores.bookstore_id'], ),
    sa.PrimaryKeyConstraint('isbn')
    )
    op.create_table('bookstores',
    sa.Column('bookstore_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('city', sa.VARCHAR(length=255), nullable=True),
    sa.Column('net_yearly_revenue', sa.Integer(), nullable=True),
    sa.Column('number_of_books_in_stock', sa.Integer(), nullable=True),
    sa.Column('isbn', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['isbn'], ['books.isbn'], ),
    sa.PrimaryKeyConstraint('bookstore_id')
    )
    op.create_table('books_bookstores',
    sa.Column('isbn', sa.BigInteger(), nullable=False),
    sa.Column('bookstore_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bookstore_id'], ['bookstores.bookstore_id'], ),
    sa.ForeignKeyConstraint(['isbn'], ['books.isbn'], ),
    sa.PrimaryKeyConstraint('isbn', 'bookstore_id')
    )
    op.create_table('managers',
    sa.Column('manager_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('years_employed', sa.Integer(), nullable=True),
    sa.Column('bookstore_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bookstore_id'], ['bookstores.bookstore_id'], ),
    sa.PrimaryKeyConstraint('manager_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('managers')
    op.drop_table('books_bookstores')
    op.drop_table('bookstores')
    op.drop_table('books')
    op.drop_table('authors')
    # ### end Alembic commands ###
