from google import genai
from dotenv import load_dotenv
import os
import json
from fastapi import HTTPException
        

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API")
client = genai.Client(api_key=GEMINI_API_KEY)



def classifyEmailContent(emailContent):

    generation_config = {
            "temperature": 0.3,  # Mais determinístico
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 1024,
            "response_mime_type": "application/json",  # Força resposta JSON
        }
    

    prompt = f"""Você é um assistente especializado em classificação e resposta automática de emails corporativos.

    **TAREFA:**
    Analise o email abaixo e forneça:
    1. Classificação (PRODUTIVO ou IMPRODUTIVO)
    2. Resposta automática apropriada

    **DEFINIÇÕES:**

    - PRODUTIVO: Emails que requerem ação ou resposta específica
    - Exemplos: solicitações de suporte, pedidos de documentos, abertura de chamados, pedidos de status, dúvidas técnicas, requisições de informação, envio de arquivos importantes, urgências

    - IMPRODUTIVO: Emails que NÃO necessitam de ação imediata
    - Exemplos: felicitações, agradecimentos gerais, saudações, confirmações simples, avisos informativos gerais

    **INSTRUÇÕES PARA RESPOSTA AUTOMÁTICA:**
    - Se PRODUTIVO: resposta formal, prestativa, que reconheça a solicitação e ofereça suporte/próximos passos
    - Se IMPRODUTIVO: resposta cordial, breve e gentil
    - Tom: profissional, respeitoso e objetivo
    - Tamanho: 3-5 linhas

    **OBSERVAÇÃO:** O email pode conter metadados, cabeçalhos ou informações ruidosas. Foque no conteúdo principal da mensagem.

    ---

    **EMAIL A SER ANALISADO:**
    {emailContent}

    ---

    **FORMATO DE RESPOSTA (retorne APENAS o JSON, sem texto adicional):**
    {{
    "classificacao": "PRODUTIVO" ou "IMPRODUTIVO",
    "resposta_automatica": "texto da resposta aqui",
    "confianca": 0.0 a 1.0,
    "motivo": "breve justificativa da classificação"
    }}"""


    try:
        response = client.models.generate_content (
                model="gemini-2.0-flash-exp",  # Modelo mais recente
                config=generation_config,
                contents=prompt
            )
        result = json.loads(response.text)
        return {"classification": result["classificacao"],
            "automatic_response": result["resposta_automatica"],"reason": result.get("motivo", "")}
    except HTTPException as e:
        raise(e)