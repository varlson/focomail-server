from fastapi import UploadFile
from fastapi.responses import JSONResponse
from app.helper.filePreprocessor import fileDataPreProcessorDrive, inputDataPreProcessorDrive
from app.helper.geminiAI import classifyEmailContent
from app.helper.deepSeekApi import deepSeekClassifyEmailContent
from fastapi import HTTPException




class EmailClassifierController:
    @staticmethod
    def emailClassifierByFile(file: UploadFile):
        
        try:

            if not (file.filename.endswith(".pdf") or file.filename.endswith(".txt")):
                raise HTTPException(
                status_code=400,  # 400 é mais adequado para "Bad Request"
                detail="Formato de arquivo não permitido. Apenas PDF ou TXT são aceitos."
                )

            isPDF = True if file.filename.endswith(".pdf") else False
            text = fileDataPreProcessorDrive(file, isPDF)
            # response = deepSeekClassifyEmailContent(text)
            response = classifyEmailContent(text)

            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "data": {"customMessage": response.get("automatic_response"), "classification": response.get("classification")},
                    "error": None
                }
            )

        except HTTPException as e:
            return JSONResponse(
                status_code=500,
                content = {
                    "success": False,
                    "data":None,
                    "error":f"Houve um erro interno {str(e)}"
                } )


        

        
        
        
        

    @staticmethod
    def emailClassifierByText(emailTextContent: str):
        try:
            text = inputDataPreProcessorDrive(emailTextContent)
            response = classifyEmailContent(text)
        
            return JSONResponse(
                    status_code=200,
                    content = {
                        "success": True,
                        "data": {
                            "customMessage": response.get("automatic_response"),
                            "classification":response.get("classification")
                        }
                    })

        except HTTPException as e:
            JSONResponse(
                status_code=500,
                content = {
                    "success": True,
                    "data":None,
                    "error": f"Houve um erro interno {str(e)}"
                })

