import pytest
from ..main import app, test
from httpx import AsyncClient
from .repository import AlunasRepository
from ..database import engine, Base, get_db 
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

NOME = 'Maria das Dores de Souza'
NOME_SOCIAL = 'Mariela'
CPF = '50070792003'
RG = '2154992'
DATA_NASC = '12/02/1970'
NOME_PAI = 'Joao'
NOME_MAE = 'Joana'
DEFICIENCIA = False
ENDERECO_ID = 1

GLOBAL_RESPONSE = []
HTTPS_ALUNAS = "https://alunas"

TOKEN = test

# CREATE
@pytest.mark.asyncio
async def test_create_aluna():
    '''Função para testar a criação de uma aluna'''
    data = {
        "nome": NOME,
        "nomeSocial": NOME_SOCIAL,
        "cpf": CPF,
        "rg": RG,
        "dNascimento": DATA_NASC,
        "nomePai": NOME_PAI,
        "nomeMae": NOME_MAE,
        "deficiencia": DEFICIENCIA,
        "idEndereco": ENDERECO_ID
    }
    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.post("/alunas/", json=data, headers=headers)
        global GLOBAL_RESPONSE
        GLOBAL_RESPONSE = response
    assert response.status_code == 201

# GET ALL
@pytest.mark.asyncio
async def test_read_all_alunas():
    '''Função para testar exibição de todas alunas (ainda sem paginação)'''
    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.get("/alunas/", headers=headers)
    assert response.status_code == 200

# GET BY CPF
@pytest.mark.asyncio
async def test_read_by_cpf_alunas():
    '''Função para testar pesquisa de aluna por CPF'''
    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.get(f"/alunas/{CPF}", headers=headers)
    assert response.status_code == 200

# UPDATE BY ID
@pytest.mark.asyncio
async def test_update_by_id_aluna():
    '''Função para testar modificação de objeto aluna por ID'''
    data = {
        "nome": NOME,
        "nomeSocial": 'Felipe',
        "cpf": CPF,
        "rg": RG,
        "dNascimento": '00/00/00',
        "nomePai": NOME_PAI,
        "nomeMae": NOME_MAE,
        "deficiencia": DEFICIENCIA,
        "idEndereco": ENDERECO_ID
    }

    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.put(f"/alunas/{GLOBAL_RESPONSE.json()['id']}", json = data, headers=headers)
    assert response.status_code == 200

# DELETE BY CPF
@pytest.mark.asyncio
async def test_delete_by_id_alunas():
    '''Função para testar apagar aluna por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.delete(f"/alunas/{GLOBAL_RESPONSE.json()['id']}", headers=headers)
    assert response.status_code == 204

# GET COUNT
@pytest.mark.asyncio
async def test_count_alunas(database: Session = get_db()):
    '''Função para testar o count de alunas'''
    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.get("/alunas/count/", headers=headers)
        response = response.json()
    assert response["count"] == AlunasRepository.count_all(database)


# GET COUNT FORMADAS
@pytest.mark.asyncio
async def test_count_alunas_formadas(database: Session = get_db()):
    '''Função para testar o count de alunas formadas'''
    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.get("/alunas/count/formada", headers=headers)
        response = response.json()
    assert response["count"] == AlunasRepository.count_formada(database)