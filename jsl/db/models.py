from .basic import Base
from .tables import article, comment, praise, poster, follow


class Article(Base):
    __table__ = article

    def __repr__(self):
        return "文章title:{},发布时间:{},浏览数:{},最后访问时间:{},关注数:{}".format(
            self.title, self.post_time, self.read_num, self.access_time, self.follow_num
        )


class Comment(Base):
    __table__ = comment


class Praise(Base):
    __table__ = praise

    def __repr__(self):
        return "赞来自:{}".format(self.praise_user)


class Poster(Base):
    __table__ = poster


class Follow(Base):
    __table__ = follow

