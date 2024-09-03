from typing import List

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestBurger:

    @pytest.mark.parametrize('name, price', [
        ('Ржаная', 200),
        ('Кунжут', 1000),
        ('Бао', 20.5)
    ])
    def test_burger_set_buns_method(self, name, price):
        bun = Bun(name=name, price=price)
        burger: Burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize('name, type, price', [
        ('Кетчуп', 'cоус', 200),
        ('Майонез', 'начинка', 1000),
        ('Гуляш', 'гарнир', 20.5)
    ])
    def test_burger_add_ingredient_method(self, name, type, price):
        ingredient = Ingredient(name=name, price=price, ingredient_type=type)
        burger: Burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    def test_get_recipe(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        assert burger.get_recipe() == (
            '(==== black bun ====)\n'
            '= sauce sour cream =\n'
            '= sauce chili sauce =\n'
            '(==== black bun ====)\n\n'
            'Price: 700'
        )

    def test_get_change_ingredient(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        burger.move_ingredient(1, 0)
        assert burger.get_recipe() == (
            '(==== black bun ====)\n'
            '= sauce chili sauce =\n'
            '= sauce sour cream =\n'
            '(==== black bun ====)\n\n'
            'Price: 700'
        )

    def test_remove_ingredient(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        burger.remove_ingredient(1)
        assert burger.get_recipe() == (
            '(==== black bun ====)\n'
            '= sauce sour cream =\n'
            '(==== black bun ====)\n\n'
            'Price: 400'
        )        

    def test_get_price(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.set_buns(buns[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])
        assert burger.get_price() == 700