"""initial migration

Revision ID: 913cdc9bedde
Revises: 31f27d352966
Create Date: 2018-05-10 16:21:53.377389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '913cdc9bedde'
down_revision = '31f27d352966'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'last_seen')
    # ### end Alembic commands ###
