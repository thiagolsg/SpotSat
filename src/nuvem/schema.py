from typing import Union
from pydantic import BaseModel


class Amostras(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    # UTILIZAR PARA SUBIR PARA PRODUÇÃO
    id = int
   # geom = GeometryColumn(Polygon(2))


class AmostrasRequest(Amostras):
    '''...'''

class AmostrasResponse(Amostras):
    '''...'''
    class Config:
        orm_mode = True

class AmostrasCountResponse(BaseModel):
    count: int
    class Config:
        orm_mode = True