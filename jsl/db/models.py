from .basic import Base
from .tables import question, answer, agree, people, follow, answer_comment


class Question(Base):
    __table__ = question

    def __repr__(self):
        return "文章title:{},发布时间:{},浏览数:{},最后访问时间:{},关注数:{}".format(
            self.title, self.post_time, self.read_num, self.access_time, self.follow_num
        )


class Answer(Base):
    __table__ = answer

    def __repr__(self):
        return "评论id:{},评论内容:{}".format(self.answer_id, self.content)


class AnswerComment(Base):
    __table__ = answer_comment

    def __repr__(self):
        return "评论id:{},评论内容:{}".format(self.comment_id, self.content)


class Agree(Base):
    __table__ = agree

    def __repr__(self):
        return "赞来自:{}".format(self.agree_user)


class People(Base):
    __table__ = people

    def __repr__(self):
        return "id:{},用户名:{},个人说明:{}".format(self.people_id, self.people_name, self.people_desc)


class Follow(Base):
    __table__ = follow

    def __repr__(self):
        return "关注者id:{},被关注者id:{}".format(self.follower_id, self.refer_id)


