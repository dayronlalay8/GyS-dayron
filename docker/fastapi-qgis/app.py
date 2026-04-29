from fastapi import FastAPI
from src.app.routes.qgis_route import router as qgis_router


app = FastAPI(
    title="Procesamiento con QGIS",
    version= "1.0.0",
    contact={
        "name": "USAL",
        "url": "https://usal.github.io/",
        "email": "usal@usal.es"
    },
    description="APIs para ejecutar algoritmos de procesamiento con QGIS"
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


app.include_router(qgis_router, prefix="/api", tags=["Items de procesamiento"])