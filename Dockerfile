FROM python

EXPOSE 80

WORKDIR /cvforyou_2

COPY requirements.py /cvforyou_2

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /cvforyou_2

ENTRYPOINT ["python3"] 

CMD ["manage.py", "runserver", "0.0.0.0:80"]
