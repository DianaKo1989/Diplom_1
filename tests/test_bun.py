import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [
        ('Ржаная', 200),
        ('Кунжут', 1000),
        ('Бао', 20.5)
    ])
    def test_get_bun_methods(self, name: str, price: int):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name
        assert bun.get_price() == price
