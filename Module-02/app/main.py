from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/shipment")
def getShipment():
    return {
        "content": "wooden_table",
        "status": "in transit"
    }

@app.get("/scalar", include_in_schema=False)
def getScalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )