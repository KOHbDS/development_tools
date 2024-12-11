import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from http import HTTPStatus
from typing import Dict, List, Union

app = FastAPI(
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)


class FitRequest(BaseModel):
    config: Dict[str, str]
    train_data: Dict[str, List[float]]

class ModelListResponse(BaseModel):
    # Список словарей
    models:


class ApiResponse(BaseModel):
    message: str
    data: Union[Dict, None] = None


models = {}


  

# API endpoints
@app.post("/fit", response_model=ApiResponse, status_code=HTTPStatus.CREATED)
async def fit(request:FitRequest):
    # Реализуйте логику обучения и сохранения модели.
    # Обратите внимание на формат входных данных.
    # Обучать линейную регрессию.
    return ApiResponse()

@app.post("/load", response_model='')
async def load(request: ''):
    # Реализуйте загрузку обученной модели для инференса.
    return

@app.post("/predict")
async def predict(request:):
    # Реализуйте инференс загруженной модели
    return

@app.get("/list_models", response_model='')
async def list_models():
    # Реализуйте получения списка обученных моделей
    return  ModelListResponse(models='')


# Реализуйте Delete метод remove_all

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)