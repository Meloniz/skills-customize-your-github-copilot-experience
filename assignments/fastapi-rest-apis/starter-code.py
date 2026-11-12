from fastapi import FastAPI

app = FastAPI(title="Item API")

items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


# TODO: Add an endpoint to get a single item by id
# TODO: Add an endpoint to create a new item
# TODO: Add an endpoint to update an item
