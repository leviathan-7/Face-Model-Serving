from __future__ import annotations

import json
import os
import typing as t
from pathlib import Path
import bentoml
from bentoml.validators import ContentType
from fastapi import FastAPI
from fastapi.responses import JSONResponse

Image = t.Annotated[Path, ContentType("image/*")]

# Возвращает наибольшее лицо (Face Detection)
def getFace(self, images: list[Image]):
    results = self.model.predict(source=images)
    arr = [json.loads(result.to_json()) for result in results]
    resFace = arr[0]
    if resFace.__len__() == 0:
        raise Exception()
    h = 0
    for item in arr:
        k = item[0]["box"]["y2"] - item[0]["box"]["y1"]
        if k > h:
            h = k
            resFace = item
    return resFace

@bentoml.service(resources={"gpu": 1})
class YoloV8:
    def __init__(self):
        from ultralytics import YOLO
        yolo_model = os.getenv("YOLO_MODEL", "yolov8m_200e_face.pt")
        self.model = YOLO(yolo_model)


    @bentoml.api(batchable=True)
    def predict(self, images: list[Image]):
        return getFace(self, images)

    @bentoml.api
    def render(self, image: Image):
        result = self.model.predict(image)[0]
        output = image.parent.joinpath(f"{image.stem}_result{image.suffix}")
        result.save(str(output))
        return output
