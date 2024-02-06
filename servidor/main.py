from typing import Union
import uvicorn
from fastapi import FastAPI
from routers import agendamento
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(agendamento.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001)