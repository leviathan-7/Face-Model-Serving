from typing import Union

from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/new_person/")
def new_person(name, img: UploadFile):
    try:
        contents = img.file.read()
    except Exception:
        return JSONResponse({}, status_code=500)
    finally:
        img.file.close()
    if False: #Если имя или изображение есть в базе
        return JSONResponse({}, status_code=404)
    #Добавить изображение в базу
    return JSONResponse({}, status_code=200)

@app.post("/api/get_person/")
def get_person(img: UploadFile):
    try:
        contents = img.file.read()
    except Exception:
        return JSONResponse({}, status_code=500)
    finally:
        img.file.close()
    name = "ИМЯ"
    if False: #Если изображения нету в базе
        return {"name": ""}
    return {"name": name}