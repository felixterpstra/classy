"""empty message

Revision ID: e249188620d6
Revises: 
Create Date: 2018-01-26 15:15:37.129937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e249188620d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classy_jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('s3bucket', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('classy_labels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('classy_job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classy_job_id'], ['classy_jobs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classy_texts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=1000), nullable=True),
    sa.Column('file_created', sa.DateTime(), nullable=True),
    sa.Column('classification_text', sa.Text(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('classy_job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classy_job_id'], ['classy_jobs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classy_training_items',
    sa.Column('classy_text_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('classy_label_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['classy_label_id'], ['classy_labels.id'], ),
    sa.ForeignKeyConstraint(['classy_text_id'], ['classy_texts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('classy_text_id', 'user_id', 'classy_label_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('classy_training_items')
    op.drop_table('classy_texts')
    op.drop_table('classy_labels')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('classy_jobs')
    # ### end Alembic commands ###
