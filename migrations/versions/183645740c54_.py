from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183645740c54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_name', 'last_name', 'number')
    )


def downgrade():
    op.drop_table('contact')
