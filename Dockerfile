# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


# RUN apt-get update
# RUN apt install -y libgl1-mesa-glx
# RUN apt-get install -y tesseract-ocr-all
# COPY ./app /app
# RUN pip install python-multipart
# RUN pip install pytesseract
# RUN pip install opencv-python

# CMD ["uvicorn","main:app","--host","0.0.0.0","--port","$PORT"]

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN apt-get install -y tesseract-ocr-all
# COPY ./app /app

COPY ./app /app
RUN pip install python-multipart numpy
RUN pip install pytesseract
RUN pip install opencv-python 

RUN chmod +x /start.sh

CMD ["bash","start.sh"]

