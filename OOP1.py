class Figura:
    def __init__(self, lados):
        self.lados = lados

    def get_lados(self):
        return self.lados

    def set_lados(self, nova_qtd):
        self.lados = nova_qtd

    def nome_ate_10_lados(self):
        if self.lados == 1 or self.lados == 2:
            print("Impossível\n")
        if self.lados == 3:
            print("Triângulo\n")
        if self.lados == 4:
            print("Quadrado\n")
        if self.lados == 5:
            print("Pentagono\n")
        if self.lados == 6:
            print("Hexagono\n")
        if self.lados == 7:
            print("Heptagono\n")
        if self.lados == 8:
            print("Octogono\n")
        if self.lados == 9:
            print("Eneagono\n")
        if self.lados == 10:
            print("Decagono\n")
        if self.lados > 10:
            print(f"Figura de {self.lados} lados\n")

    def print_dados(self):
        return f"Figura de {self.lados} lados\n"


class Triangulo(Figura):
    def __init__(self, lados, base_t, altura_t):
        super().__init__(lados)
        self.base = base_t
        self.altura = altura_t

    def get_base(self):
        return self.base

    def set_altura(self, nova_altura):
        self.altura = nova_altura

    def print_dados(self):
        return f"Triangulo\n"

    def area(self):
        return (self.base * self.altura)/2


class Retangulo(Figura):
    def __init__(self, lados, base_r, altura_r):
        super().__init__(lados)
        self.base = base_r
        self.altura = altura_r

    def get_altura(self):
        return self.altura

    def set_base(self, nova_base):
        self.base = nova_base

    def print_dados(self):
        return f"Retangulo"

    def area(self):
        return self.base * self.altura


if __name__ == '__main__':
    figura1 = Figura(1)
    figura2 = Triangulo(3,5,5)
    figura3 = Retangulo(4,6,4)

    figura1.nome_ate_10_lados()
    print(f"{figura1.get_lados()}\n")
    figura1.set_lados(4)
    figura1.nome_ate_10_lados()
    print(figura1.print_dados())
    figura2.set_altura(4)
    print(f"{figura2.get_base()}\n")
    print(f"{figura2.print_dados()}\n")
    print(f"Área: {figura2.area()}\n")
    figura3.set_base(8)
    print(f"{figura3.get_altura()}\n")
    print(f"{figura3.print_dados()}\n")
    print(f"Área: {figura3.area()}\n")
