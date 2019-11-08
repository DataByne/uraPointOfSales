"""users table

Revision ID: e4b79529c734
Revises: 9add67dccc03
Create Date: 2019-11-08 15:46:18.235327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4b79529c734'
down_revision = '9add67dccc03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('creation_date', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'creation_date')
    # ### end Alembic commands ###
