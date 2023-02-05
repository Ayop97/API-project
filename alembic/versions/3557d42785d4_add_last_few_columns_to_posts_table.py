"""add last few columns to posts table

Revision ID: 3557d42785d4
Revises: 88e34a9b9500
Create Date: 2023-02-04 23:07:27.943019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3557d42785d4'
down_revision = '88e34a9b9500'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass