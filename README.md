# docker-fastapi-opencv-tesseract

[FastAPI](https://fastapi.tiangolo.com/)
[Docker](https://www.docker.com/)
[Heroku](https://www.heroku.com/)

API ocr on electricity meter for dormitory (result is roomcode , unit of used) // deploy on Heroku

* URL : https://ocrxfastapi.herokuapp.com/

# setup step for heroku 




# Deploying dockerized fastAPI to Heroku 



1. Clone this repo. Set up and push to heroku.

```bash
git clone https://github.com/xkritti/docker-fastapi-opencv-tesseract.git
cd docker-fastapi-opencv-tesseract
heroku login
heroku container:login
heroku create <your-app-name>
heroku container:push web -a <your-app-name>
heroku container:release web -a <your-app-name>
```

2.  Enjoy your fastAPI at https://your-app-name.herokuapp.com
