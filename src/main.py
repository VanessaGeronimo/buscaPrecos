from repository.ProductsRepository import ProductRepository
from tests.ProductSearcher import ProductSearcher

def main():
    buscador = ProductSearcher()
    galaxy_products = buscador.search('smartphone samsung galaxy a70')
    one_vision_products = buscador.search('smartphone motorola one vision')
    xiaomi_products = buscador.search('smartphone xiaomi redmi note 7')

    product_repository = ProductRepository()
    product_repository.build_header()
    product_repository.save_many(
        galaxy_products+
        one_vision_products+
        xiaomi_products
    )

if __name__ == '__main__':
    main()
