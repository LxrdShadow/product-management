class ProductNotFound(Exception):
    def __init__(self, number: str, message: str | None = None):
        self.message = message or f"Produit avec le numéro '{number}' not found."
        super().__init__(self.message)
