"""create table products

Revision ID: 1b5a1bfd664b
Revises: 7d31dcb95d00
Create Date: 2022-11-07 21:26:05.534465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b5a1bfd664b'
down_revision = '7d31dcb95d00'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('price', sa.Float(precision=2, asdecimal=True), nullable=False),
    sa.Column('description', sa.String(length=225), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###