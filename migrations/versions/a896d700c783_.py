"""empty message

Revision ID: a896d700c783
Revises: 4a9956ef0bb1
Create Date: 2024-04-21 15:32:33.526911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a896d700c783'
down_revision = '4a9956ef0bb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=80), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('rotational_period', sa.Integer(), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.Column('terrain', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
