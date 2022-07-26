from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_page = 0

    def __next__(self):
        product = self.data[self.current_page]
        if not product:
            raise StopIteration()
        self.current_page += 1
        return product
