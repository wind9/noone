from sqlalchemy import Table, Column, INTEGER, String, DateTime, DATE
from .basic import metadata


stock_info = Table("stock_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("coop_code", String(100)),
                   Column("coop_name", String(100)),
                   Column("stock_code", String(100), unique=True),
                   Column("stock_name", String(100)),
                   Column("reg_date", DATE),
                   Column("other1", String(100), default='', server_default=''),
                   Column("other2", String(100), default='', server_default=''),
                   Column("other3", String(100), default='', server_default=''),
                   Column("other4", String(100), default='', server_default=''),
                   Column("other5", String(100), default='', server_default=''),
                   )

__all__ = ['stock_info']
