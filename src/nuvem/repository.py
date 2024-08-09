from sqlalchemy.orm import Session
from ..model.model import Amostras
# from .model import Amostras

class AmostrasRepository:
    @staticmethod
    def find_all(database: Session) -> list[Amostras]:
        '''Função para fazer uma query de todas as Amostras da DB'''
        return database.query(Amostras).all()
    
    @staticmethod
    def find_by_id(database: Session, id: int) -> Amostras:
        '''Função para fazer uma query por ID de um objeto aluna na DB'''
        return database.query(Amostras).filter(Amostras.id == id).first()

    @staticmethod
    def exists_by_id(database: Session, id: int) -> bool:
        '''Função que verifica se o ID dado existe na DB'''
        return database.query(Amostras).filter(Amostras.id == id).first() is not None

    @staticmethod
    def delete_by_id(database: Session, id: str) -> None:
        '''Função para excluir um objeto aluna da DB dado o ID'''
        amostras = database.query(Amostras).filter(Amostras.id == id).first()
        if amostras is not None:
            database.delete(amostras)
            database.commit()

    @staticmethod
    def count_all(database: Session) -> int:
        '''Função para fazer uma query de todas as alunas da DB'''
        return database.query(Amostras).count()
        
    