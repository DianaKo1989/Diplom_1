import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('name, type, price', [
        ('Кетчуп', 'cоус', 200),
        ('Майонез', 'начинка', 1000),
        ('Гуляш', 'гарнир', 20.5)
    ])
    def test_ingridient_get_name_method(self, name, type, price):
        ingredient = Ingredient(name=name, price=price, ingredient_type=type)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('name, type, price', [
        ('Кетчуп', 'cоус', 200),
        ('Майонез', 'начинка', 1000),
        ('Гуляш', 'гарнир', 20.5)
    ])
    def test_ingridient_get_type_method(self, name, type, price):
        ingredient = Ingredient(name=name, price=price, ingredient_type=type)
        assert ingredient.get_type() == type     

    @pytest.mark.parametrize('name, type, price', [
        ('Кетчуп', 'cоус', 200),
        ('Майонез', 'начинка', 1000),
        ('Гуляш', 'гарнир', 20.5)
    ])
    def test_ingridient_get_price_method(self, name, type, price):
        ingredient = Ingredient(name=name, price=price, ingredient_type=type)
        assert ingredient.get_price() == price