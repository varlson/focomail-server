import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

def deepSeekClassifyEmailContent(emailContent):
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
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Você é um especialista em classificação de emails corporativos. Sempre retorne APENAS JSON válido sem nenhum texto adicional."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            max_tokens=1000
        )
        
        # Extrai o conteúdo da resposta
        result_text = response.choices[0].message.content.strip()
        
        # Tenta fazer parse do JSON
        try:
            result_json = json.loads(result_text)
            
            content = {
                "classification": str(result_json.get('classificacao', 'ERRO')),
                "automatic_response": str(result_json.get('resposta_automatica', 'Obrigado pelo seu email.')),
                "reason": str(result_json.get('motivo', 'Classificação não disponível')),
            }

            return content
        except json.JSONDecodeError:
            # Fallback caso a resposta não seja JSON válido
            return {
                "classificacao": "ERRO",
                "resposta_automatica": "Obrigado pelo seu email. Encontramos um problema técnico e nossa equipe já foi notificada.",
                "confianca": 0.0,
                "motivo": "Falha ao processar a classificação do email"
            }
            
    except Exception as e:
        # Tratamento de erro para falhas na API
        return {
            "classificacao": "ERRO",
            "resposta_automatica": "Obrigado pelo seu email. Estamos com problemas técnicos momentâneos e retornaremos em breve.",
            "confianca": 0.0,
            "motivo": f"Erro na API: {str(e)}"
        }