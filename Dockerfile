FROM python:3.7

# Initialize
WORKDIR /root
COPY requirements.txt /root/

# Setup
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000
