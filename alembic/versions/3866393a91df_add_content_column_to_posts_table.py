"""add content column to posts table

Revision ID: 3866393a91df
Revises: 8e60925ad019
Create Date: 2023-05-31 21:49:00.027111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3866393a91df'
down_revision = '8e60925ad019'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
