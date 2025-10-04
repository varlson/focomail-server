from pydantic import BaseModel

class BaseResponse:
    staCode:int
    success:bool


class  EmailClassiferResponse(BaseModel, BaseResponse):
    emailClassification:str | None
    customMessage: str | None




# class  EmailClassiferInput(BaseModel):
#     content : "o tipo pode ser texto ou um ficheiro (pdf ou .txt)"