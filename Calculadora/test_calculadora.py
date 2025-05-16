import pytest
from calculadora import Calculadora

@pytest.fixture
def calcular():
    return Calculadora();

def testSoma(calcular):
    assert calcular.somar(5, 25) == 30;

def testSubtrair(calcular):
    assert calcular.subtrair(12, 6) == 6;

def testMultiplicar(calcular):
    assert calcular.multiplicar(5, 25) == 125;

def testDividir(calcular):
    assert calcular.dividir(6, 2) == 3;

def testDividirPorZero(calcular):
    with pytest.raises(ZeroDivisionError)  as mensagemdeerro:
        calcular.dividir(5, 0);
    assert "Não é possivel dividir por zero" in str(mensagemdeerro.value);

def testSomarNumerosNegativos(calcular):
    assert calcular.somar(-2, -10) == -12;

def testSubtrairResultadoNegativo(calcular):
    assert calcular.subtrair(5, 10) == -5;

def testMultiplicacaoPorZero(calcular):
    assert calcular.multiplicar(0, 100) == 0;

def testSomaComZero(calcular):
    assert calcular.somar(0, 10) == 10;

def testSomarFloats(calcular):
    assert calcular.somar(2.5, 3.2) == pytest.approx(5.7);

def testDividirFloats(calcular):
    assert calcular.dividir(5.0, 2.0) == 2.5;

#OBS: Feito orientada por IA
def testSomaIntFloat(calcular):
    assert calcular.somar(3, 2.5) == pytest.approx(5.5);

#OBS: Feito orientada por IA
def testDivisaoResultado_decimal(calcular):
    assert calcular.dividir(7, 2) == 3.5;

#OBS: Feito orientada por IA
def testSomaComLetras(calcular):
    with pytest.raises(TypeError):
        calcular.somar("a", 2);

def testSubtrairString(calcular):
    with pytest.raises(TypeError):
        calcular.subtrair(10, "dez");

def testSomaStringMensagem(calcular):
    with pytest.raises(TypeError) as erro:
        calcular.somar("a", "b");
    assert "Os valores devem ser números" in str(erro.value);

def testNumerosGrandes(calcular):
    assert calcular.multiplicar(10**10, 10**5) == 10**15

 
# OBS
# Usei inteligência artificial (ChatGPT) para obter novas ideias de testes e entender funcionamento de classes, métodos e o conceito de Test-Driven Development (TDD).
# Além disso, assisti videos YouTube para entender mais a sintaxe de classes em Python.
# Durante o processo, tive dificuldades na instalação do pytest devido a problemas de ambiente (uso o linux). Com a ajuda do ChatGPT, fui orientada a configurar um ambiente virtual (venv), e tive sucesso ao instalar o pytest


