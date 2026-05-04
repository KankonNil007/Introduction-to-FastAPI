from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Any

app = FastAPI()

shipments = {
    12701: {"weight": 4.5, "content": "glassware", "status": "placed"},
    12702: {"weight": 2.8, "content": "books", "status": "shipped"},
    12703: {"weight": 6.1, "content": "electronics", "status": "in transit"},
    12704: {"weight": 3.3, "content": "clothing", "status": "delivered"},
    12705: {"weight": 5.0, "content": "kitchenware", "status": "pending"},
    12706: {"weight": 7.4, "content": "furniture", "status": "placed"},
}


@app.get("/shipment/latest")
def get_latest_shipment():
    id = max(shipments.keys())
    return shipments[id]


@app.get("/shipment/{id}")
def getShipment(id: int) -> dict[str, Any]:
    if id not in shipments.keys():
        return {"detail": "Given id doesn't exist!"}
    return shipments[id]


@app.get("/scalar", include_in_schema=False)
def getScalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")
