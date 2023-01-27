From deepnox/python-ta-lib-pandas:1.4.3_talib0.4.24_python3.10.6_alpine3.16
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install -r  requirements.txt
CMD sh

