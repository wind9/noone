from sqlalchemy import Column, String, Integer, Table, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from db import metadata

question = Table('question', metadata,
                 Column("id", Integer, primary_key=True),
                 Column("question_id", Integer, unique=True),
                 Column("people_id", String(100)),
                 Column("title", String(500)),
                 Column("post_time", DateTime),
                 # Column("modify_time", DateTime),
                 Column("access_time", DateTime),
                 Column("read_num", String(500)),
                 Column("follow_num", String(500)),
                 Column("content", LONGTEXT)
                 )

answer = Table('answer', metadata,
               Column("id", Integer, primary_key=True),
               Column("answer_id", Integer, unique=True),
               Column("people_id", String(100)),
               Column("post_time", DateTime),
               Column("content", LONGTEXT)
               )

answer_comment = Table('answer_comment', metadata,
                       Column("id", Integer, primary_key=True),
                       Column("answer_id", Integer),
                       Column("comment_id", String(100)),
                       Column("post_time", DateTime),
                       Column("content", LONGTEXT)
                       )

agree = Table('agree', metadata,
              Column("id", Integer, primary_key=True),
              Column("agree_type", Integer),  # 1:question点赞 2:awnswer点赞
              Column("refer_id", String(100)),
              Column("agree_user", String(100)),
              )

people = Table('people', metadata,
               Column("id", Integer, primary_key=True),
               Column("people_id", Integer, unique=True),
               Column("people_name", String(100)),
               Column("people_type", String(100), default=''),
               Column("people_province", String(100), default=''),
               Column("people_city", String(100), default=''),
               Column("people_sex", String(100), default=''),
               Column("home_access_num", Integer, default=0),
               Column("people_desc", String(500), default=''),
               Column("weiwang_num", Integer, default=0),
               Column("agree_num", Integer, default=0),
               Column("thanks_num", Integer, default=0),
               Column("gold_num", Integer, default=0),
               )

follow = Table('follow', metadata,
               Column("id", Integer, primary_key=True),
               Column("people_id", Integer),
               Column("follow_type", Integer), #1:用户 2:question
               Column("follow_id", Integer),
               )

