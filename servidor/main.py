from typing import Union
import uvicorn
from fastapi import FastAPI
from routers import agendamento

app = FastAPI()
app.include_router(agendamento.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)