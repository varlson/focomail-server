from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import UploadFile, File 
from app.controllers.emailClassifier import EmailClassifierController


emailClassifierRouter = APIRouter(prefix="/email-classifier", tags=["EmailClassifier"])

class DataModel(BaseModel):
    customMessage: str 
    classification: str

class ResponseModel(BaseModel):
    success: bool
    data: DataModel | None = None
    error:str | None = None


@emailClassifierRouter.post("/file", response_model=ResponseModel)
def classifyFile(file: UploadFile = File(...)):
    return EmailClassifierController.emailClassifierByFile(file)




class TextRequest(BaseModel):
    emailTextContent: str

@emailClassifierRouter.post("/text", response_model=ResponseModel)
def classifyText(req: TextRequest):
    return EmailClassifierController.emailClassifierByText(req.emailTextContent)

@emailClassifierRouter.post("/upload", )
def uploadFile(file: UploadFile = File(...)):
    return EmailClassifierController.upload_file(file)
