from sqlalchemy.orm import Session

from models import Product

class ProductRepository:
    
    # Método GET
    # find_all -> responsável por buscar todos os produtos cadastrados.
    @staticmethod
    def find_all(db: Session) -> list[Product]:
        return db.query(Product).all()
    # ------------------------------------------------------------
    
    # Método GET
    # find_by_id -> responsável por buscar um produto no banco de dados com base no id.
    @staticmethod
    def find_by_id(db: Session, id: int) -> Product:
        return db.query(Product).filter(Product.id == id).first()
    #-----------------------------------------------------------------------------------
    
    # Método GET
    # exists_by_id -> responsável por verificar se existe algum produto cadastrado com base no id.
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Product).filter(Product.id == id).first() is not None
    #---------------------------------------------------------------------------------------------
    
    # Método POST e PUT
    # save -> responsável por salvar um produto no banco de dados.
    # Também serve para editar um produto existente no banco de dados. 
    @staticmethod
    def save(db: Session, product: Product) -> Product:
        if product.id:
            db.merge(product)
        else:
            db.add(product)
        db.commit()
        return product
    #------------------------------------------------------------------

    # Método DELETE
    # delete_by_id -> responsável por excluir um curso com base no seu id.
    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        product = db.query(Product).filter(Product.id == id).first()
        if product is not None:
            db.delete(product)
            db.commit()
