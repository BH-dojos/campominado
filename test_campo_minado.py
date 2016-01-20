
from campo_minado import resolve_campo_minado

def test_uma_mina_retorna_uma_mina():
    assert resolve_campo_minado(["*"]) == ["*"]

def test_um_ponto_retorna_zero():
    assert resolve_campo_minado(["."]) == ["0"]

def test_linha_sem_mina_retorna_zeros():
    assert resolve_campo_minado(["..."]) == ["000"]

def test_linha_com_mina_retorna_mina():
    assert resolve_campo_minado(["***"]) == ["***"]

