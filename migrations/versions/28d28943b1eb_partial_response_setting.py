"""partial response setting

Revision ID: 28d28943b1eb
Revises: 48c96bd323c6
Create Date: 2019-03-25 16:50:19.958684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28d28943b1eb'
down_revision = '48c96bd323c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deployment', sa.Column('enable_partial_response_for_messages', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('deployment', 'enable_partial_response_for_messages')
    # ### end Alembic commands ###