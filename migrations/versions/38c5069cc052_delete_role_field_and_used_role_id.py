"""delete role field and used role_id

Revision ID: 38c5069cc052
Revises: e31880808be7
Create Date: 2024-08-08 08:46:47.007234

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '38c5069cc052'
down_revision = 'e31880808be7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', mysql.VARCHAR(length=20), nullable=False))

    # ### end Alembic commands ###
