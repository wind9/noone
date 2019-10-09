from sqlalchemy import Column, String, Integer, Table, BLOB, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from db import metadata

article = Table('article', metadata,
                Column("id", Integer, primary_key=True),
                Column("article_id", Integer, unique=True),
                Column("poster", String(100)),
                Column("title", String(500)),
                Column("post_time", DateTime),
                #Column("modify_time", DateTime),
                Column("access_time", DateTime),
                Column("read_num", String(500)),
                Column("follow_num", String(500)),
                Column("content", LONGTEXT)
                )

comment = Table('comment', metadata,
                Column("id", Integer, primary_key=True),
                Column("comment_id", Integer, unique=True),
                Column("comment_type", Integer), #1:一级评论 2:二级评论
                Column("poster", String(100)),
                Column("post_time", DateTime),
                Column("content", LONGTEXT)
                )

praise = Table('praise', metadata,
               Column("id", Integer, primary_key=True),
               Column("praise_type", Integer), #1:一级点赞 2:二级点赞
               Column("refer_id", String(100)),
               Column("praise_user", String(100)),
               )

poster = Table('poster', metadata,
               Column("id", Integer, primary_key=True),
               Column("poster_id", Integer, unique=True),
               Column("poster_type", String(100)),
               Column("home_access_num", Integer),
               Column("self_desc", String(500)),
               Column("weiwang", Integer),
               Column("praise_num", Integer),
               Column("thanks_num", Integer),
               Column("gold_num", Integer),
               )

follow = Table('follow', metadata,
               Column("id", Integer, primary_key=True),
               Column("poster_id", Integer),
               Column("follow_type", Integer), #1:用户 2:article
               Column("follow_id", Integer),
               )

