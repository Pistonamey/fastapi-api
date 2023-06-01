"""add last few columns to posts table

Revision ID: feb5f3b9f7e6
Revises: fc181f01259e
Create Date: 2023-05-31 22:09:31.156322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feb5f3b9f7e6'
down_revision = 'fc181f01259e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'),
    )
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
