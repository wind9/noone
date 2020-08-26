from sqlalchemy import Table, String, Integer, DateTime, Column, Date
from db import metadata
import datetime

market_info = Table('market_info', metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("update_time", DateTime, default=datetime.datetime.now),
                    Column("date", Date),
                    Column("province", String(100)),
                    Column("city", String(100)),
                    Column("pinpai", String(100)),
                    Column("ptype", String(100)),
                    Column("price", String(100)),
                    Column("company", String(100)),
                    Column("ext1", String(100)),
                    Column("ext2", String(100))
                    )
