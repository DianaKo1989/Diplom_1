import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('name, type, price', [
        ('Кетчуп', 'cоус', 200),
        ('Майонез', 'начинка', 1000),
        ('Гуляш', 'гарнир', 20.5)
    ])
    def test_get_ingridient_methods(self, name, type, price):
        ingredient = Ingredient(name=name, price=price, ingredient_type=type)
        assert ingredient.get_type() == type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price