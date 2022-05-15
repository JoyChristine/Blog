"""empty message

Revision ID: e0dd063dd652
Revises: 4e3acc649e20
Create Date: 2022-05-15 09:28:46.696442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0dd063dd652'
down_revision = '4e3acc649e20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###
