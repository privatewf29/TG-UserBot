# We're using Ubuntu 20.10
FROM w29f/docker:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b TG-UserBot https://github.com/W29F/TG-UserBot/root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.github.com/W29F/TG-UserBot/TG-UserBot/requirements.txt

CMD ["python3","-m","userbot"]
