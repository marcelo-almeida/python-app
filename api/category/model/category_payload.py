class CategoryPayload:
    category_id: int
    name: str
    products: list

    def __init__(self, name, products, category_id=None):
        self.category_id = category_id
        self.name = name
        self.products = products

    def to_dict(self):
        return self.__dict__
