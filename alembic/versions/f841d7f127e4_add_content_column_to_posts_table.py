"""add content column to posts table

Revision ID: f841d7f127e4
Revises: 86774c04398d
Create Date: 2023-02-04 22:02:58.769446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f841d7f127e4'
down_revision = '86774c04398d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
