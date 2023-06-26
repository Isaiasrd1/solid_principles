from abc import ABC, abstractmethod


# CLASSE QUE DEFINE UM ANIMAL E OS ATRIBUTOS(NOME, PESO E IDADE)
class Animal:
    def __init__(self, name, peso, age):
        self.name = name
        self.peso = peso
        self.age = age


# CLASSE BASE PARA OBSERVADORES COM O MÉTODO DE NOTIFICACAO
class AnimalObserver(ABC):
    @abstractmethod
    def notificar_adicao(self, animal):
        pass

    def notificar_mudanca(self, animal):
        pass


# CLASSE PARA O SUJEITO/ANIMAL ATUAL CONTENDO OBSERVADORES
class AnimalSubject:
    def __init__(self):
        self.animal = None
        self.observers = []

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        self.observers.remove(observer)

    def notificar_adicao_observers(self):
        for observer in self.observers:
            observer.notificar_adicao(self.animal)

    def notificar_mudanca_observers(self):
        for observer in self.observers:
            observer.notificar_mudanca(self.animal)

    def set_animal(self, name, peso, age):
        if self.animal is None:
            self.animal = Animal(name, peso, age)
        else:
            self.animal.name = name
            self.animal.peso = peso
            self.animal.age = age
        self.notificar_adicao_observers()

    def mud_animal(self, name, peso, age):
        if self.animal is None:
            self.animal = Animal(name, peso, age)
        else:
            self.animal.name = name
            self.animal.peso = peso
            self.animal.age = age
        self.notificar_mudanca_observers()


class AnimalNotificacaoObserver(AnimalObserver):
    def notificar_adicao(self, animal):
        print(f"O animal {animal.name} foi ADICIONADO. Peso: {animal.peso}, Idade: {animal.age}")

    def notificar_mudanca(self, animal):
        print(f"O animal {animal.name} foi ALTERADO. Peso: {animal.peso}, Idade: {animal.age}")


# VALIDADOR DE PESO (CASO O VALOR INFORMADO NAO SEJA COMPATÍVEL)
class PesoValidator:
    @staticmethod
    def validar_peso(peso):
        try:
            float(peso)
            return True
        except ValueError:
            return False


class AgeValidator:
    @staticmethod
    def validar_idade(age):
        try:
            float(age)
            return True
        except ValueError:
            return False


class WordValidator:
    @staticmethod
    def validar_letra(option):
        try:
            return option.upper() in ["S", "N"]
        except ValueError:
            return False


class ECCService:
    @staticmethod
    def calcular_ecc(peso, idade):
        if idade <= 2:
            if peso < 1.5:
                ecc = 1  #EMACIADO
            elif peso < 2.5:
                ecc = 2  # MUITO MAGRO
            else:
                ecc = 3  # MAGRO
        elif idade <= 7:
            if peso < 2.5:
                ecc = 4  # MAGRO
            elif peso < 4.5:
                ecc = 5  # IDEAL
            else:
                ecc = 6  # SOBREPESO
        else:
            if peso < 4.5:
                ecc = 7  # SOBREPESO
            elif peso < 6.5:
                ecc = 8  # OBESIDADE
            else:
                ecc = 9  # OBESIDADE GRAVE

        return ecc


def main():
    subject = AnimalSubject()
    notificacao_observer = AnimalNotificacaoObserver()
    subject.adicionar_observer(notificacao_observer)

    name = input("Digite o nome do animal: ")
    peso = None

    while peso is None or not PesoValidator.validar_peso(peso):
        peso = input("Digite o peso do animal: ")
        if not PesoValidator.validar_peso(peso):
            print("Valor inválido para peso. Digite um número válido.")

    age = None
    while age is None or not AgeValidator.validar_idade(age):
        age = input("Digite a idade do animal: ")
        if not AgeValidator.validar_idade(age):
            print("Insira uma idade válida!")

    subject.set_animal(name, peso, age)

    print("---------------------------------------")

    option = input(f"Deseja alterar os dados do animal {subject.animal.name}? (S/N): ")
    while not WordValidator.validar_letra(option):
        print("---------------------------------------")
        print("Resposta inválida!")
        print("---------------------------------------")
        option = input(f"Deseja alterar os dados do animal {subject.animal.name}? (S/N): ")
        if option.upper() == "N":
            print("Encerrando programa....")

    if option.upper() == "S":
        name = input("Digite o novo nome do animal: ")
        peso = None

        while peso is None or not PesoValidator.validar_peso(peso):
            peso = input("Digite o novo peso do animal: ")
            if not PesoValidator.validar_peso(peso):
                print("Valor inválido para peso. Digite um número válido.")

        age = input("Digite a nova idade do animal: ")
        while not AgeValidator.validar_idade(age):
            print("Insira uma idade válida!")
            age = input("Digite a nova idade do animal: ")

        subject.mud_animal(name, peso, age)

    print("---------------------------------------")
    print("Encerrando programa...")



if __name__ == '__main__':
    main()