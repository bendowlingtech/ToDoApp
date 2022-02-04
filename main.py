from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/todo")
async def get_lists():
    return {"It Works"}

@app.get("/api/todo/{id}")
async def get_list(id: str):
    return {f"It Works {id}"}

@app.post("/api/todo/{name}")
async def create_list(name: str):
    return f"list named {name} created"

@app.delete("/api/todo/{id}")
async def delete_list(id: str):
    return f"list with id: {id} deleted"

@app.patch("/api/todo/{id}")
async def update_list(name: str, data:str):
    return f"list named {name} updated"



