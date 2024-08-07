from sqlalchemy.orm import Session
from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status, HTTPException, Response, Depends
from ..model.model import Amostras
# from .model import Alunas
from .repository import AmostrasRepository
from .schema import AmostrasCountResponse, AmostrasRequest, AmostrasResponse

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
    '''Faz uma query de todos os objetos aluna na DB (sem paginação)'''
    Amostras = AmostrasRepository.find_all(database)
    print(Amostras)
    return [AmostrasResponse.from_orm(amostra) for amostra in Amostras]


# GET COUNT ALL
@router.get("/count/")
def count_all(database: Session = Depends(get_database)):
    '''Faz uma query de contagem de Amostras na DB (sem paginação)'''
    count = AmostrasRepository.count_all(database)
    return {"count":count} #[ImpactadasResponse.from_orm(impactada) for impactada in impactadas]

# GET COUNT ALL FORMADAS
#@router.get("/count/formada")
#def count_formada(database: Session = Depends(get_database)):
#    '''Faz uma query de contagem de Amostras formadas na DB (sem paginação)'''
#    count_formada = AmostrasRepository.count_formada(database)
#    return {"count":count_formada} #[ImpactadasResponse.from_orm(impactada) for impactada in impactadas]