from models.Product import Product
from typing import List
import xlsxwriter

class ProductRepository:

    workbook = xlsxwriter.Workbook('Products.xlsx')
    worksheet = workbook.add_worksheet()
    
    def save_many(self, products: List[Product]):
        for product in products:
            self.worksheet.write(products.index(product)+1, 0, 'Magazine Luiza')
            self.worksheet.write(products.index(product)+1, 1, product.name)
            self.worksheet.write(products.index(product)+1, 2, product.price)
            self.worksheet.write(products.index(product)+1, 3, product.old_price)

        self.workbook.close()

    def build_header(self):
        self.worksheet.write(0, 0, 'Site')
        self.worksheet.write(0, 1, 'Nome')
        self.worksheet.write(0, 2, 'Preço')
        self.worksheet.write(0, 3, 'Preço com desconto')
