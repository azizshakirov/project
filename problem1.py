def find_most_abundant(products: dict) -> str:
    return max(products, key=lambda x: products[x])

products = {"olma": 15, "banan": 30, "sut": 10}
print(find_most_abundant(products))
# Output: "sut"
