"""empty message

Revision ID: cabba036e1e9
Revises: be28ddb959b4
Create Date: 2022-05-15 11:44:40.318041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cabba036e1e9'
down_revision = 'be28ddb959b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_blog_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'blog_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('blogs_blog_id_fkey', 'blogs', 'blogs', ['blog_id'], ['id'])
    # ### end Alembic commands ###
