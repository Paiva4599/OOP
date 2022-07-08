class Animais:
    def __init__(self, animal, vertebrado, nutricao):
        self.animal = animal
        self.vertebrado = vertebrado
        self.nutricao = nutricao

    def __str__(self):
        s = f"Animal: {self.animal}\nVertebrado: {self.vertebrado}\nNutricao: {self.nutricao}\n"
        return s

    def get_animal(self):
        return self.animal

    def get_vertebrado(self):
        return self.vertebrado

    def get_nutricao(self):
        return self.nutricao

    def set_animal(self, novo_animal):
        self.animal = novo_animal

    def traducao(self):
        if self.nutricao == 'Carnivoro':
            print("Come carne")
        if self.nutricao == 'Herbivoro':
            print("Come vegetais")
        if self.nutricao == 'Onivoro':
            print("Come tanto carne quanto vegetal")

class Mamifero(Animais):
    def __init__(self, animal, vertebrado, nutricao, grupo, patas = "Quadrupede"):
        super().__init__(animal, vertebrado, nutricao)
        self.grupo = grupo
        self.patas = patas

    def get_grupo(self):
        return self.grupo

    def get_patas(self):
        return self.patas

    def set_patas(self, numero_patas):
        self.patas = numero_patas

    def __str__(self):
        x = super().__str__()
        s = f"{x}Grupo: {self.grupo}\nPatas: {self.patas}\n"
        return s

if __name__ == '__main__':
    animal1 = Animais("Abelha", "Não", "Herbivoro")
    animal2 = Animais("Avestruz", "Sim", "Onivoro")
    animal3 = Mamifero("Canguru", "Sim", "Herbivoro", "Marsupial", "Bípede")
    animal4 = Mamifero("Cachorro", "Sim", "Carnivoro", "Euterio")

    print(animal1)
    print(animal2)
    print(animal3)
    print(animal4)

    Animais.set_animal(animal1, "Borboleta")
    print("Animal 1: ", Animais.get_animal(animal1))
    print("Animal 2: ", Animais.get_vertebrado(animal2))
    print("Animal 3: ", Animais.get_nutricao(animal3))
    Mamifero.set_patas(animal4, "Bípede")
    print("Animal 4: ", Mamifero.get_patas(animal4), "\n")

    Animais.traducao(animal1)
    Animais.traducao(animal2)
    Animais.traducao(animal3)
    Animais.traducao(animal4)
