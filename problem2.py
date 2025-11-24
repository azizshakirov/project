def find_product_by_id(products: list, product_id: str):
    for product in products:
        if product[0] == product_id:
            return product
    return 

products = [("ID123", "Olma", 10), ("ID101", "Banan", 5), ("ID150", "Anor", 8)]
print(find_product_by_id(products, "ID111"))
# Output: ('ID101', 'Banan', 5)
