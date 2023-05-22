"""create initial tables

Revision ID: e1cdecb15bf1
Revises:
Create Date: 2023-05-22 22:11:36.143896

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "e1cdecb15bf1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "workflow",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_workflow_id"), "workflow", ["id"], unique=False)
    op.create_table(
        "node",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("key", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("workflow_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["workflow_id"],
            ["workflow.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_node_id"), "node", ["id"], unique=False)
    op.create_table(
        "edge",
        sa.Column("src_id", sa.Integer(), nullable=False),
        sa.Column("target_id", sa.Integer(), nullable=False),
        sa.Column("workflow_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["src_id"],
            ["node.id"],
        ),
        sa.ForeignKeyConstraint(
            ["target_id"],
            ["node.id"],
        ),
        sa.ForeignKeyConstraint(
            ["workflow_id"],
            ["workflow.id"],
        ),
        sa.PrimaryKeyConstraint("src_id", "target_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("edge")
    op.drop_index(op.f("ix_node_id"), table_name="node")
    op.drop_table("node")
    op.drop_index(op.f("ix_workflow_id"), table_name="workflow")
    op.drop_table("workflow")
    # ### end Alembic commands ###
