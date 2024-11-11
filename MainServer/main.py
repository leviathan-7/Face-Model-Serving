from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/new_person/")
def new_person(name, img):
    if False: #Если имя или изображение есть в базе или какое-то из значений пустое
        return JSONResponse({}, status_code=500)
    #Добавить изображение в базу
    return JSONResponse({}, status_code=200)

@app.post("/api/get_person/")
def get_person(img):
    name = "Иван Иванов"
    if False: #Если изображения нету в базе
        return {"name": ""}
    return {"name": name}