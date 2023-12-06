"""changing created_at to modified_at

Revision ID: f6f087bed26b
Revises: 
Create Date: 2023-11-29 15:08:53.704222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6f087bed26b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('project_category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('user_category_permission', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    with op.batch_alter_table('user_project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('user_category_permission', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('project_category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), autoincrement=False, nullable=True))
        batch_op.drop_column('modified_at')

    # ### end Alembic commands ###
