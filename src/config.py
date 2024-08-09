from click import password_option
from pydantic import BaseSettings

# connect_url para uso com o docker compose: mysql+pymysql://root:password@db/db
class Settings(BaseSettings):
    #engine://user:password@host(nome do serviço do container no caso do docker-compose):port/database
    db_connect_url: str = "postgresql://docker:docker@db/gis" 
    #db_connect_url: str = "mysql+pymysql://amisroot:vgHNQB0HVxP07iFd3YFO@amis.mysql.database.azure.com/amisdb"
    #user_name: str 
    #password: str
    #class Config:
    #    env_file = ".env"

settings = Settings()