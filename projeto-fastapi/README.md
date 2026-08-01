Projeto FastAPI — Setup e migrações

Instalação (usar o venv do projeto):

Windows PowerShell:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Gerar e aplicar migrations com Alembic:

```powershell
# criar uma revision (autogenerate) quando houver mudanças nos modelos
.venv\Scripts\alembic revision --autogenerate -m "mensagem"

# aplicar todas as migrations
.venv\Scripts\alembic upgrade head
```

Se o banco já existir (ex.: você já criou as tabelas com `create_all`) e quiser sincronizar o estado do Alembic sem reaplicar SQL, rode:

```powershell
.venv\Scripts\alembic stamp head
```

Rodar o servidor de desenvolvimento:

```powershell
.venv\Scripts\uvicorn main:app --reload
```

Observações:
- Use Alembic para controlar alterações no schema em ambiente de produção.
- Durante desenvolvimento rápido, `Base.metadata.create_all(bind=db)` pode ser usado, mas não é recomendado para controle de versões do schema.
