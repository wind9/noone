from sqlalchemy import Column, INTEGER, String, MetaData, Table
from .basic import metadata

wb_user_info = Table("user_info",metadata,
                     Column("id", INTEGER, primary_key=True, autoincrement=True),
                     Column("userid", INTEGER, unique=True),
                     Column("name", String),
                     Column("description", String),

                     Column("wb_count", INTEGER),
                     Column("fans_count", INTEGER),
                     Column("follower_count", INTEGER)
                     )
