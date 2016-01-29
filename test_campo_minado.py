
from campo_minado import resolve_campo_minado

def test_uma_mina_retorna_uma_mina():
    assert resolve_campo_minado(["*"]) == ["*"]

def test_um_ponto_retorna_zero():
    assert resolve_campo_minado(["."]) == ["0"]

def test_dois_pontos_retorna_zeros():
    assert resolve_campo_minado([".."]) == ["00"]

def test_ponto_mina_retorna_um_mina():
    assert resolve_campo_minado([".*"]) == ["1*"]

def test_linha_sem_mina_retorna_zeros():
    assert resolve_campo_minado(["..."]) == ["000"]

def test_linha_com_mina_retorna_mina():
    assert resolve_campo_minado(["***"]) == ["***"]

def test_linha_com_duas_minas_retorna_campo():
    assert resolve_campo_minado(["*.*"]) == ["*2*"]
