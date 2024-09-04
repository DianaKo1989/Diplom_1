import pytest
from typing import List
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDataBase:
    @pytest.mark.parametrize('bun, price, id', [
        ('black bun', 100, 0),
        ('white bun', 200, 1), 
        ('red bun', 300, 2)
    ])
    def test_get_available_buns(self, bun: str, price: int, id: int):
        database: Database = Database()
        buns: List[Bun] = database.available_buns()
        assert buns[id].get_name() == bun
        assert buns[id].get_price() == price

    @pytest.mark.parametrize('ingredient, price, id', [
        ('hot sauce', 100, 0),
        ('sour cream', 200, 1),
        ('chili sauce', 300, 2),
        ('cutlet', 100, 3),
        ('dinosaur', 200, 4),
        ('sausage', 300, 5)
    ])
    def test_get_available_ingredient(self, ingredient: str, price: int, id: int):
        database: Database = Database()
        ingredients: List[Ingredient] = database.available_ingredients()
        assert ingredients[id].get_name() == ingredient
        assert ingredients[id].get_price() == price
