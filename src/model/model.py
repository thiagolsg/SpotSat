'''Importando parâmetros da orm'''

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum, DateTime
from sqlalchemy.orm import Mapped
from datetime import datetime
from ..database import Base
from geoalchemy2 import Geometry, WKBElement
from sqlalchemy.orm import mapped_column

class Amostras(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "amostras"

    # UTILIZAR PARA TESTES LOCAIS
    id: int = Column(Integer, primary_key = True, index = True)
    idLulcn: str = Column(String(11), nullable = True)
    geom: Mapped[WKBElement] = mapped_column(
        Geometry(geometry_type="POLYGON", srid=4326, spatial_index=True)
    )
