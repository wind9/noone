FROM centos:latest

MAINTAINER ResolveWang <w1796246076@sina.com>

RUN yum install which python3 python3-pip -yq
RUN which python3|xargs -i ln -s {} /usr/bin/python
RUN which pip3|xargs -i ln -s {} /usr/bin/pip
RUN mkdir /root/.pip
COPY . /home/jsl
COPY pip.conf /root/.pip/pip.conf
WORKDIR /home/jsl
RUN pip install -r requirements.txt
CMD ["celery", "-A", "tasks.workers", "worker", "-l", "info", "-c","50","-Q", "question_queue,people_queue,answer_comment_queue","-f","logs/jsl.log"]