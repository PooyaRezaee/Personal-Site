"""empty message

Revision ID: bfe0c4b4e44f
Revises: 1d3684d54138
Create Date: 2021-04-21 01:29:46.450606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfe0c4b4e44f'
down_revision = '1d3684d54138'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_way',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('url_image', sa.String(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('text')
    )
    op.create_table('documents',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('url_image', sa.String(length=256), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('settings',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('FullName', sa.String(length=64), nullable=True),
    sa.Column('AboutME', sa.Text(), nullable=True),
    sa.Column('url_background', sa.String(length=256), nullable=True),
    sa.Column('url_profile', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('skills',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=32), nullable=True),
    sa.Column('Value_skill', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('Name')
    )
    op.create_table('work samples',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('url_image', sa.String(length=256), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work samples')
    op.drop_table('skills')
    op.drop_table('settings')
    op.drop_table('documents')
    op.drop_table('contact_way')
    # ### end Alembic commands ###
