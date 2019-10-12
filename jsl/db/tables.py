from sqlalchemy import Column, String, Integer, Table, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from db import metadata

question = Table('question', metadata,
                 Column("id", Integer, primary_key=True),
                 Column("question_id", Integer),
                 #Column("question_id", Integer, unique=True),
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
               Column("question_id", Integer),
               Column("answer_id", Integer),
               Column("people_id", String(100)),
               Column("post_time", DateTime),
               Column("content", LONGTEXT)
               )

answer_comment = Table('answer_comment', metadata,
                       Column("id", Integer, primary_key=True),
                       Column("answer_id", Integer),
                       Column("comment_id", Integer),
                       Column("people_id", Integer),
                       Column("post_time", DateTime),
                       Column("content", LONGTEXT)
                       )

agree = Table('agree', metadata,
              Column("id", Integer, primary_key=True),
              Column("question_id", Integer, default=-1),  # 1:question点赞 2:awnswer点赞
              Column("answer_id", Integer, default=-1),
              Column("people_id", Integer),
              )

people = Table('people', metadata,
               Column("id", Integer, primary_key=True),
               Column("people_id", Integer),
               #Column("people_id", Integer, unique=True),
               Column("name", String(100)),
               Column("user_type", String(100), default=''),
               Column("province", String(100), default=''),
               Column("city", String(100), default=''),
               Column("post", String(100), default=''),
               Column("home_visit_num", Integer, default=0),
               Column("desc", String(500), default=''),
               Column("weiwang_num", Integer, default=0),
               Column("agree_num", Integer, default=0),
               Column("thanks_num", Integer, default=0),
               Column("gold_num", Integer, default=0),
               Column("last_active_time", DateTime),
               )

follow = Table('follow', metadata,
               Column("id", Integer, primary_key=True),
               Column("follower_id", Integer),
               Column("follow_type", Integer), #1:用户 2:question
               Column("refer_id", Integer),
               )

