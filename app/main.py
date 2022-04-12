from fastapi import FastAPI, File, UploadFile
import os
import sys
sys.path.insert(1, os.path.abspath("app"))
from ocr import read_image
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://psu-e-dorm.vercel.app",
    "https://psu-e-dorm.vercel.app",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def server_status():
    return {
        "msg": "Server is online"
    }


@app.post("/upload_to_orc")
async def upload_to_orc(file: UploadFile = File(...)):
    # check dir images if not create new if have pass to next method
    try:
        os.mkdir("images")
        print(os.getcwd())
    except Exception as e:
        print(e)

    # Create path of image
    file_path = os.getcwd()+"/images/"+file.filename.replace(" ", "-")

    # Save image at file_path
    with open(file_path, "wb+") as f:
        f.write(file.file.read())

    # send image to OCR Process
    # result = await read_image(file_path)
    result = await read_image(file_path)

    print(result)

    # Delete image from Post Method
    os.remove(file_path)
    if result['error'] != True:
        # {"filename": file.filename, "data": result}
        return {"msg": "success!!", "data": result['res']}
    elif result['error'] == False:
        return {"msg": "error!!"}
    else:
        return {"msg": "not found text in picture"}
