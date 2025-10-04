from fastapi import FastAPI
from app.routes.emailClassifier import emailClassifierRouter
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",  # frontend local
    "http://127.0.0.1:3000",
    "https://meusite.com",    # produção
]

app = FastAPI(title= "This is a server for FocoMail application")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # quem pode acessar
    allow_credentials=True,
    allow_methods=["*"],          # pode restringir ex: ["GET", "POST"]
    allow_headers=["*"],          # headers permitidos
)


app.include_router(emailClassifierRouter, prefix="/api")