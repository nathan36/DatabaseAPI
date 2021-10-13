FROM python:3.9-buster
ENV PORT=3131
# make ssh dir
RUN mkdir /root/.ssh/
# copy over private key and set permission
ADD id_rsa /root/.ssh/
RUN chmod 700 /root/.ssh/id_rsa
RUN chown -R root:root /root/.ssh
# create known_hosts file
RUN ssh-keyscan -t rsa -H github.com >> /root/.ssh/known_hosts
# clone repo to local
RUN git clone git@github.com:nathan36/DatabaseAPI_fastAPI.git
# set working directory
WORKDIR /DatabaseAPI_fastAPI
# install requirements
RUN pip3 install -r requirements.txt
EXPOSE 3131
# run app
CMD ["python", "main.py"]
