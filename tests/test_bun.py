import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [
        ('Ржаная', 200),
        ('Кунжут', 1000),
        ('Бао', 20.5)
    ])
    def test_bun_get_name_method(self, name: str, price: int):
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price


    @pytest.mark.parametrize('name, price', [
        ('Ржаная', 200),
        ('Кунжут', 1000),
        ('Бао', 20.5)
    ])
    def test_bun_get_price_method(self, name: str, price: int):
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price        
