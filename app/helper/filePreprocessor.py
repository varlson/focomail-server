import pdfplumber
import io
import re
from fastapi import UploadFile,HTTPException
MAX_FILE_SIZE = 5 * 1024 * 1024  



def extract_pdf_text(file: UploadFile):

    file_bytes = file.file.read()

    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"Arquivo '{file.filename}' excede o limite de 5MB."
        )

    file_stream = io.BytesIO(file_bytes)

    text = ""
    with pdfplumber.open(file_stream) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_txt_text(file:UploadFile):
    file_bytes = file.file.read()

    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"Arquivo '{file.filename}' excede o limite de 5MB."
        )

    text = file_bytes.decode("utf-8", errors="ignore")
    return text

def basic_cleaning(text: str) -> str:
    """Limpeza básica: remove excesso de espaços, quebras de linha, etc."""
    
    # Remove múltiplas quebras de linha
    text = re.sub(r'\n+', '\n', text)
    
    # Remove múltiplos espaços
    text = re.sub(r'\s+', ' ', text)
    
    # Remove espaços no início e fim
    text = text.strip()
    
    return text

def remove_email_metadata(text: str) -> str:
    """Remove metadados comuns de emails (headers, footers)"""
    
    # Remove linhas com padrão de email
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove números de telefone (padrão brasileiro)
    text = re.sub(r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}', '', text)
    
    return text



def fileDataPreProcessorDrive(file: UploadFile, isPDF = True) -> str:
    text = extract_pdf_text(file) if isPDF else extract_txt_text(file)
    return text


def inputDataPreProcessorDrive(text) -> str:
    text = basic_cleaning(text)
    text = remove_email_metadata(text)
    return text

