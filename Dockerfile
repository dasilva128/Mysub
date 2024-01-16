FROM python:3.10.0

RUN python -m pip install --upgrade pip
RUN python -m pip install requests
RUN python -m pip install beautifulsoup4

CMD python3 main.py
