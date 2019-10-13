FROM centos:latest

MAINTAINER ResolveWang <w1796246076@sina.com>

RUN yum install which python3 python3-pip -yq
RUN mv /usr/bin/python /usr/bin/python2 && which python3|xargs -i ln -s {} /usr/bin/python
RUN which pip3|xargs -i ln -s {} /usr/bin/pip
COPY . /home/jsl
WORKDIR /home/jsl
RUN pip install -r requirements.txt
CMD ["celery", "-A", "tasks.workers", "worker", "-l", "info", "-Q", "question_queue,people_queue,answer_comment_queue"]
