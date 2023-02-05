"""create psots table

Revision ID: 86774c04398d
Revises: 
Create Date: 2023-02-04 21:50:08.862551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86774c04398d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
