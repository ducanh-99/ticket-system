"""

Message: empty message
Revision ID: 38e7014badb4
Revises: 4ceea3a8f35c
Create Date: 2023-07-21 23:55:41.760768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38e7014badb4'
down_revision = '4ceea3a8f35c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
    alter table tutor_subject
        drop primary key;

    alter table tutor_subject
        add primary key (tutor_id, subject_id, grade_id);
    """)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###