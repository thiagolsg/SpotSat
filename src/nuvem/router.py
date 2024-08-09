from sqlalchemy.orm import Session
from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status, HTTPException, Response, Depends
from ..model.model import Amostras
# from .model import Alunas
from .repository import AmostrasRepository
from .schema import AmostrasCountResponse, AmostrasRequest, AmostrasResponse
import folium

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix = '/Amostras',
    tags = ['Amostras'],
    responses = {404: {"description": "Not found"}},
)

#@router.post("/",
#    response_model = AmostrasResponse,
#    status_code = status.HTTP_201_CREATED
#)

#def create(request: AmostrasRequest, database: Session = Depends(get_database)):
#    '''Cria e salva um objeto amostra por meio do método POST'''
#    Amostras = AmostrasRepository.save(database, Amostras(**request.dict()))
#    return Amostras

get_session = get_database

# GET ALL
@router.get("/", response_model = list[AmostrasResponse])
def find_all(database: Session = Depends(get_database)):
    '''Faz uma query de todos os objetos amostra na DB (sem paginação)'''
    Amostras = AmostrasRepository.find_all(database)
    print(Amostras)
    return [AmostrasResponse.from_orm(amostra) for amostra in Amostras]

# GET COUNT ALL
@router.get("/count/")
def count_all(database: Session = Depends(get_database)):
    '''Faz uma query de contagem de Amostras na DB (sem paginação)'''
    count = AmostrasRepository.count_all(database)
    return {"count":count} #[ImpactadasResponse.from_orm(impactada) for impactada in impactadas]

@router.get("/{id}", response_model = AmostrasResponse)
def find_by_id(id: int, database: Session = Depends(get_database)):
    '''Dado o ID como parâmetro, encontra o poligono com esse ID'''
    amostras = AmostrasRepository.find_by_id(database, id)
    if not amostras:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "Localização não encontrada"
        )
    return AmostrasResponse.from_orm(amostras)

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_by_id(id: str, database: Session = Depends(get_database)):
    '''Dado o ID do poligono, deleta o objeto da DB por meio do método DELETE'''
    if not AmostrasRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="Aluna não encontrada"
        )
    AmostrasRepository.delete_by_id(database, id)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model = AmostrasResponse)
def update(id: str, request: AmostrasRequest, database: Session = Depends(get_database)):
    '''Dado o ID da poligono, atualiza os dados cadastrais na DB por meio do método PUT'''
    if not AmostrasRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Aluna não encontrada"
        )
    aluna = AmostrasRepository.save(database, Amostras(id = id, **request.dict()))
    return AmostrasResponse.from_orm(aluna)

# GET COUNT ALL FORMADAS
#@router.get("/count/formada")
#def count_formada(database: Session = Depends(get_database)):
#    '''Faz uma query de contagem de Amostras formadas na DB (sem paginação)'''
#    count_formada = AmostrasRepository.count_formada(database)
#    return {"count":count_formada} #[ImpactadasResponse.from_orm(impactada) for impactada in impactadas]