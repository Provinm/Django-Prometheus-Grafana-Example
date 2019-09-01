FROM python:3.7
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /server/
RUN pip install -r /server/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple