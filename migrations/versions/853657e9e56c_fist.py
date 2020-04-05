"""Fist

Revision ID: 853657e9e56c
Revises: 
Create Date: 2020-04-05 17:37:58.597873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '853657e9e56c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('microblog_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(length=350), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microblog_posts_id'), 'microblog_posts', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_microblog_posts_id'), table_name='microblog_posts')
    op.drop_table('microblog_posts')
    # ### end Alembic commands ###
