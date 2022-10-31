from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from models import Product
from database import engine, Base, get_db
from repositories import ProductRepository
from schemas import ProductRequest, ProductResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Liberação da API para consumo do Front-End.
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#---------------------------------------------

# Rota para fazer a requisição POST - Criação do Registro
@app.post("/api/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create(request: ProductRequest, db: Session = Depends(get_db)):
    product = ProductRepository.save(db, Product(**request.dict()))
    return ProductResponse.from_orm(product)
#--------------------------------------------------------------------------------------------------

# Rota para a requisição GET - Buscar todos os registros
@app.get("/api/products", response_model=list[ProductResponse])
def find_all(db: Session = Depends(get_db)):
    products = ProductRepository.find_all(db)
    return [ProductResponse.from_orm(product) for product in products]
#----------------------------------------------------------------------

# Rota para a requisição GET - Buscar registro por ID
@app.get("/api/products/{id}", response_model=ProductResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    product = ProductRepository.find_by_id(db, id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    return ProductResponse.from_orm(product)
#----------------------------------------------------------------------------------

# Rota para a requisição DELETE - Deletar por ID
@app.delete("/api/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    ProductRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
#-------------------------------------------------------------------------------------

# Rota para fazer a requisição PUT - Atulização do Registro
@app.put("/api/products/{id}", response_model=ProductResponse)
def update(id: int, request: ProductRequest, db: Session = Depends(get_db)):
    if not ProductRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    product = ProductRepository.save(db, Product(id=id, **request.dict()))
    return ProductResponse.from_orm(product)
#-------------------------------------------------------------------------------------














