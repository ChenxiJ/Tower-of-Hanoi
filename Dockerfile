FROM python:3

MAINTAINER Chenxi Whitehouse <chenxi.whitehouse@hotmail.com>

ADD hanoi.py /

CMD [ "python", "./hanoi.py" ]



