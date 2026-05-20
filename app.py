from fastapi import FastAPI, HTTPException, Depends
#py -m fastapi dev nomearquivo.py
from pydantic import BaseModel
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.orm import sessionmaker, Session, declarative_base

app = FastAPI()
security = HTTPBasic()
usuario = "adm"
senha = "adm"
database_url = "sqlite:///./tarefas.db"
engine = create_engine(database_url, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)
base = declarative_base()

class TarefaDB(base):
    __tablename__ = "Tarefas"
    nome_tarefa = Column(String, primary_key = True)
    descricao_tarefa = Column(String, index = True)
    concluir_tarefa = Column (Boolean, default = False)

class Tarefa(BaseModel):
    nome_tarefa: str
    descricao_tarefa: str
    concluir_tarefa: bool = False

base.metadata.create_all(bind = engine)

def sessao_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def autenticacao(credentials: HTTPBasicCredentials = Depends(security)):
    usuario_correto = secrets.compare_digest(credentials.username, usuario)
    senha_correta = secrets.compare_digest(credentials.password, senha)

    if not (usuario_correto and senha_correta):
        raise HTTPException(
            status_code=401,
            detail="Usuario ou senha incorretos.",
            headers={"WWW-Authenticate": "Basic"}
        )

@app.post("/adiciona")
def post_tarefa(tarefa: Tarefa, db: Session = Depends(sessao_db),credentials: HTTPBasicCredentials = Depends(autenticacao)):
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.nome_tarefa == tarefa.nome_tarefa, TarefaDB.descricao_tarefa == tarefa.descricao_tarefa).first()
    if db_tarefa:
        raise HTTPException (status_code=400, detail= "Tarefa já está na lista")
    nova_tarefa = TarefaDB(nome_tarefa = tarefa.nome_tarefa, descricao_tarefa = tarefa.descricao_tarefa, concluir_tarefa=tarefa.concluir_tarefa)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return {"message": "Tarefa adiciona com sucesso"} 

@app.get("/exibir")
def listar_tarefa(db: Session = Depends(sessao_db),page: int = 1, size: int = 5,ordem: str = "nome",credentials: HTTPBasicCredentials = Depends(autenticacao)):
    if page < 1:
        raise HTTPException(status_code=400, detail="Página invalida")

    query = db.query(TarefaDB)

    if ordem == "descricao":
        query = query.order_by(TarefaDB.descricao_tarefa)
    else:
        query = query.order_by(TarefaDB.nome_tarefa)

    tarefas = query.offset((page-1)*size).limit(size).all()
    total = query.count()

    if not tarefas:
        return {"message": "Lista de tarefas vazia"}

    return {
        "pagina": page,
        "size": size,
        "total de tarefas": total,
        "ordem de tarefas": ordem,
        "tarefas": [{"nome_tarefa":teste.nome_tarefa,"descricao_tarefa":teste.descricao_tarefa,"concluir_tarefa":teste.concluir_tarefa}
        for teste in tarefas]
    }

@app.put("/atualizar")
def atualizar_tarefa(tarefa:Tarefa, db : Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(autenticacao)):
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.nome_tarefa == tarefa.nome_tarefa).first()
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Erro, tarefa não encontrada")
    
    db_tarefa.nome_tarefa = tarefa.nome_tarefa
    db_tarefa.descricao_tarefa = tarefa.descricao_tarefa
    db.commit()
    db.refresh(db_tarefa)

    return {"message": "Informações da tarefa atualizada com sucesso"}

@app.put("/concluir/{nome_tarefa}")
def concluir_tarefa(nome_tarefa:str, db : Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(autenticacao)):
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.nome_tarefa == nome_tarefa).first()

    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Erro, tarefa não encontrada")
    
    db_tarefa.concluir_tarefa = True
    db.commit()
    db.refresh(db_tarefa)

    return {"message": "Tarefa concluida com sucesso"}

@app.delete("/delete/{nome_tarefa}")
def deletar_tarefa(nome_tarefa:str, db : Session = Depends(sessao_db),credentials: HTTPBasicCredentials = Depends(autenticacao)):
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.nome_tarefa == nome_tarefa).first()
    
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Erro, tarefa não encontrada")
    
    db.delete(db_tarefa)
    db.commit()
    return {"message": "Tarefa removida com sucesso"}
