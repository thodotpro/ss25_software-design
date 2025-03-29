from abc import ABC
import unittest

class Application(ABC):
    pass

class Iterator(ABC):
    pass

class Database(ABC):
    pass

class Search:
    def __init__(self):
        self.search_method = None
        self.search_area = None

    def select_search_method(self, method):
        self.search_method = method
        return self.search_method

    def select_search_area(self, area):
        self.search_area = area
        return self.search_area
    
    ### todo ####
    def search(self, query: str):
        pass

class ForwardSearch(Iterator):
    def forward_search(self):
        return "searching from start"
    
class BackwardSearch(Iterator):
    def backward_search(self):
        return "searching from end"
    
class Customer(Database):
    def __init__(self):
        self.customer = {}

class Sales(Database):
    def __init__(self):
        self.sales = {}

class TestSearch(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == "__main__":
    pass