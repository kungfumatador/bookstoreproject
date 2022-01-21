"""empty message

Revision ID: a0ecee6343c2
Revises: cce5a5a12ba6
Create Date: 2022-01-14 10:21:39.481712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0ecee6343c2'
down_revision = 'cce5a5a12ba6'
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
    op.drop_table('bookstores')
    op.drop_table('books')
    op.drop_table('authors')
    # ### end Alembic commands ###
