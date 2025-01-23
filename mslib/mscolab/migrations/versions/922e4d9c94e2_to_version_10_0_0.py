"""To version 10.0.0

Revision ID: 922e4d9c94e2
Revises: c171019fe3ee
Create Date: 2024-07-24 15:28:42.009581

"""
from alembic import op
import sqlalchemy as sa
import mslib.mscolab.custom_migration_types as cu


# revision identifiers, used by Alembic.
revision = '922e4d9c94e2'
down_revision = 'c171019fe3ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_image_path', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('fullname', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('profile_image_path')
        batch_op.drop_column('fullname')

     # ### end Alembic commands ###
