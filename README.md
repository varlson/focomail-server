# Focomail Server - FastAPI

## Requisitos

- Python 3.8+
- `pip`

## Instalação

```bash
git clone git@github.com:varlson/focomail-server.git
cd focomail-server
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Variaveis de ambiente

crie um arquivo `.env`
copie de `env.example` nomes das variaveis
preencha os valores de acordo com suas informações

## Executando a API

Para execuatar este projeto, digite seguintes comandos:

```bash
- cd focomail-server
- uvicorn app.main:app --reload

```

- Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Observações

- Edite o arquivo `requirements.txt` para adicionar/remover dependências.
- Use variáveis de ambiente para configurações sensíveis.
