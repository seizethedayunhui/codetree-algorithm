class ProductInfo:
    def __init__(self, name = "codetree", code = 50):
        self.name = name
        self.code = code

product1 = ProductInfo();

name, code = input().split()
code = int(code)

product2 = ProductInfo(name, code)

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")