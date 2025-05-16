class Calculadora:
# Obs: primeiro metodo foi feito orientada por chatgpt
    def verificarString(self, num1, num2):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Os valores devem ser números");

    def somar(self, num1, num2):
        self.verificarString(num1,num2);
        return num1 + num2;

    def subtrair(self, num1, num2):
        self.verificarString(num1,num2);
        return num1 - num2;

    def multiplicar(self, num1, num2):
        self.verificarString(num1,num2);
        return num1 * num2;

    def dividir(self, num1, num2):
        self.verificarString(num1,num2);
        if num2 == 0:
            raise ZeroDivisionError("Não é possivel dividir por zero");
        return num1/num2;

# OBS:
# Usei inteligência artificial (ChatGPT) para obter novas ideias de testes e entender funcionamento de classes, métodos e o conceito de Test-Driven Development (TDD).
# Além disso, assisti videos YouTube para entender mais a sintaxe de classes em Python.
# Durante o processo, tive dificuldades na instalação do pytest devido a problemas de ambiente (uso o linux). Com a ajuda do ChatGPT, fui orientada a configurar um ambiente virtual (venv), e tive sucesso ao instalar o pytest