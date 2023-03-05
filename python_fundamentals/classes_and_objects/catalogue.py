class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products_name = product_name
        self.products.append(self.products_name)

    def get_by_letter(self, first_letter: str):
        return [item for item in self.products if item.startswith(first_letter)]

    def __repr__(self):
        string_with_output = f"Items in the {self.name} catalogue:\n"
        string_with_output += '\n'.join(sorted(self.products))
        return string_with_output


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

