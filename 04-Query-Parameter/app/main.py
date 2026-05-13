from fastapi import FastAPI, status, HTTPException
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


@app.get("/shipment")
def getShipment(id: int | None = None) -> dict[str, Any]:
    if not id:
        id = max(shipments.keys())
        return shipments[id]
    if id not in shipments.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Provided id doesn't exist!"
        )
    return shipments[id]

@app.post("/shipment")
def submit_shipment(weight: float, data: dict[str, Any]) -> dict[str, int]:
    content = data["content"]

    if (weight > 25):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit reached!"
        )

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed"
    }

    return {"id": new_id}

@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    return shipments[id][field]


@app.get("/scalar", include_in_schema=False)
def getScalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")
