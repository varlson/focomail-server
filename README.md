# Focomail Server - FastAPI

## Requisitos

- Python 3.8+
- `pip`

## Instalação

```bash
git clone https://github.com/seu-usuario/focomail-server.git
cd focomail-server
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Executando a API

```bash
uvicorn main:app --reload
```

- Acesse: [http://localhost:8000](http://localhost:8000)

## Estrutura básica

- `main.py`: Arquivo principal da aplicação FastAPI.
- `requirements.txt`: Dependências do projeto.

## Observações

- Edite o arquivo `requirements.txt` para adicionar/remover dependências.
- Use variáveis de ambiente para configurações sensíveis.
