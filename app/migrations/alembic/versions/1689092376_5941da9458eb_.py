"""

Message: empty message
Revision ID: 5941da9458eb
Revises: 69cbc3863a6b
Create Date: 2023-07-11 23:19:36.726580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5941da9458eb'
down_revision = '69cbc3863a6b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booking', sa.Column('price_per_lesson_tutor', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('booking', 'price_per_lesson_tutor')
    # ### end Alembic commands ###
