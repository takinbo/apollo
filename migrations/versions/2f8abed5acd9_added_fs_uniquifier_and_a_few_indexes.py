"""added fs_uniquifier and a few indexes

Revision ID: 2f8abed5acd9
Revises: 14d0310ab80f
Create Date: 2024-09-17 21:45:23.534306

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2f8abed5acd9'
down_revision = '14d0310ab80f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fs_uniquifier', sa.String(length=64), nullable=True))
        batch_op.create_unique_constraint('user_fs_uniquifier_key', ['fs_uniquifier'])

    # update existing records with a unique fs_uniquifier
    import uuid
    user_table = sa.Table('user', sa.MetaData(), sa.Column('id', sa.Integer, primary_key=True),
                            sa.Column('fs_uniquifier', sa.String(64)))

    conn = op.get_bind()
    for row in conn.execute(sa.select(user_table.c.id)):
        conn.execute(user_table.update().values(fs_uniquifier=uuid.uuid4().hex).where(user_table.c.id == row.id))

    # finally - set nullable to False
    op.alter_column('user', 'fs_uniquifier', nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('user_fs_uniquifier_key', type_='unique')
        batch_op.drop_column('fs_uniquifier')

    # ### end Alembic commands ###
