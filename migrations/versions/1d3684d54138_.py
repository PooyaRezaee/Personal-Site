"""empty message

Revision ID: 1d3684d54138
Revises: 
Create Date: 2021-04-20 05:44:44.375945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d3684d54138'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Admin',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('UserName', sa.String(length=128), nullable=False),
    sa.Column('Password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('UserName')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Admin')
    # ### end Alembic commands ###