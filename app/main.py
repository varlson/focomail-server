from fastapi import FastAPI
from app.routes.emailClassifier import emailClassifierRouter
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",  # frontend local
    "http://127.0.0.1:3000",
    "https://focomail.vercel.app",    # produção
]

app = FastAPI(title= "This is a server for FocoMail application")
@app.get("/")
def helloWorld():
    return {"hello": "Hello world"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # quem pode acessar
    allow_credentials=True,
    allow_methods=["*"],          # pode restringir ex: ["GET", "POST"]
    allow_headers=["*"],          # headers permitidos
)
app.include_router(emailClassifierRouter, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)