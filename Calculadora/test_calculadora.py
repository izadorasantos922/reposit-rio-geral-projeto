import pytest 
from calculadora import Calculadora 

@pytest.fixture 
def calcular(): 
    return Calculadora(); 

def test_soma(calcular): 
    assert calcular.somar(5,25) == 30; 

def test_subtrair(calcular): 
    assert calcular.subtrair(12,6) == 6; 
    
def test_multiplicar(calcular): 
    assert calcular.multiplicar(5,25) == 125; 

def test_dividir(calcular): 
    assert calcular.dividir(6,2) == 3;

def test_dividir_por_zero(calcular):
    with pytest.raises(ZeroDivisionError) as mensagemdeerro:
        calcular.dividir(2, 0)
    assert "Não é possivel dividir por zero" in str(mensagemdeerro.value)
