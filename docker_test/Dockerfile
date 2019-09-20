FROM centos
MAINTAINER wind9 <yunwei@ruitone.com.cn>
RUN mkdir -p /home/python_dir
COPY ./test_docker.py /home/python_dir
WORKDIR /home/python_dir
CMD ["python","test_docker.py"]