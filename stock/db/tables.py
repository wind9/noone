from sqlalchemy import Table, Column, INTEGER, String, DateTime, DATE, Float
from .basic import metadata

stock_info = Table("stock_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("coop_code", String(100)),
                   Column("coop_name", String(100)),
                   Column("stock_code", String(100), unique=True),
                   Column("stock_name", String(100)),
                   Column("reg_date", DATE),
                   Column("total_share", INTEGER),
                   Column("circulating_share", INTEGER),
                   Column("industry", String(100), default='', server_default=''),
                   Column("security_type", String(100), default='', server_default=''),
                   Column("market", String(100), default='', server_default=''),
                   Column("other1", String(100), default='', server_default=''),
                   Column("other2", String(100), default='', server_default=''),
                   Column("other3", String(100), default='', server_default=''),
                   Column("other4", String(100), default='', server_default=''),
                   Column("other5", String(100), default='', server_default=''),
                   )

stock_day_price = Table("stock_day_price", metadata,
                        Column("id", INTEGER, primary_key=True, autoincrement=True),
                        Column("trade_date", DATE),
                        Column("stock_code", String(100)),
                        Column("open", Float),
                        Column("high", Float),
                        Column("close", Float),
                        Column("low", Float),
                        Column("chg", Float),
                        Column("percent", Float),
                        Column("volume", String(100), default='', server_default=''),
                        Column("lot_volume", String(100), default='', server_default=''),
                        Column("other1", String(100), default='', server_default=''),
                        Column("other2", String(100), default='', server_default=''),
                        Column("other3", String(100), default='', server_default=''),
                        Column("other4", String(100), default='', server_default=''),
                        Column("other5", String(100), default='', server_default=''),
                        )

__all__ = ['stock_info', 'stock_day_price']
