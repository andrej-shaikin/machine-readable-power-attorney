"""Initial

Revision ID: 18e9db654a11
Revises: 
Create Date: 2023-08-22 18:35:41.347524+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18e9db654a11'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reference_region',
    sa.Column('name', sa.String(length=440), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=2), nullable=False),
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.Uuid(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_reference_region_code'), 'reference_region', ['code'], unique=True)
    op.create_index(op.f('ix_reference_region_name'), 'reference_region', ['name'], unique=True)
    op.create_index(op.f('ix_reference_region_number'), 'reference_region', ['number'], unique=True)
    op.create_index(op.f('ix_reference_region_pk'), 'reference_region', ['pk'], unique=False)
    op.create_table('user_users',
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('is_email_confirmed', sa.Boolean(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('patronymic', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.Uuid(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_user_users_email'), 'user_users', ['email'], unique=True)
    op.create_index(op.f('ix_user_users_first_name'), 'user_users', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_users_pk'), 'user_users', ['pk'], unique=False)
    op.create_index(op.f('ix_user_users_username'), 'user_users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_users_username'), table_name='user_users')
    op.drop_index(op.f('ix_user_users_pk'), table_name='user_users')
    op.drop_index(op.f('ix_user_users_first_name'), table_name='user_users')
    op.drop_index(op.f('ix_user_users_email'), table_name='user_users')
    op.drop_table('user_users')
    op.drop_index(op.f('ix_reference_region_pk'), table_name='reference_region')
    op.drop_index(op.f('ix_reference_region_number'), table_name='reference_region')
    op.drop_index(op.f('ix_reference_region_name'), table_name='reference_region')
    op.drop_index(op.f('ix_reference_region_code'), table_name='reference_region')
    op.drop_table('reference_region')
    # ### end Alembic commands ###