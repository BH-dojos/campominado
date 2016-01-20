
from campo_minado import resolve_campo_minado

def test_uma_mina_retorna_uma_mina():
    assert resolve_campo_minado("*") == "*"

def test_um_ponto_retorna_zero():
    assert resolve_campo_minado(".") == "0"
