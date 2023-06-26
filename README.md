# solid_principles
Repositório destinado à atividade de Aplicação de Princípios SOLID - Webster

# PT
  Projeto básico feito em python utilizando os princípios SOLID.
  - Princípio da Responsabilidade Única: definir uma responsabidade única para cada classe, como as classes "Animal" e "AnimalObserver".

  - Princípio Aberto/Fechado: permite estender o comportamento adicionando novos observadores (AnimalObserver) sem modificar
a classe "AnimalSubject". A classe está aberta para extensão, mas fechada para modificação.

  - Princípio de Substituição de Liskov: classes derivadas devem poder ser substituídas por suas classes base e que classes base podem ser
substituídas por suas subclasses.

  - Princípio da Segregação de Interface: nenhum cliente deve ser forçado a depender dos métodos que não usa.
Ou seja, interfaces maiores devem ser divididas em menores.

  - Princípio da Inversão de Dependência: possui duas definições: (1) módulos de alto nível não devem depender de módulos de baixo nível
e ambos devem depender de abstrações; e (2) abstrações não devem depender de detalhes, mas detalhes devem depender de abstrações.
A classe "AnimalSubject" depende da abstração "AnimalObserver", ou seja, depende de uma interface em vez de uma implementação concreta.
Isso permite que diferentes implementações de observadores sejam injetadas na classe AnimalSubject sem modificar seu código.

# EN

Basic project done in python using SOLID principles.
  - Single Responsibility Principle (SRP): define a single responsibility for each class, such as "Animal" and "AnimalObserver" classes.

  - Open/Closed principle (OCP): allows extending the behavior by adding new observers (AnimalObserver) without modifying
an AnimalSubject class. The class is open for extension, but closed for modification.

  - Liskov Substitution Principle (LSP): Derived classes must be able to be substituted for their base classes and what base classes can be
replaced by their subclasses.

  - Interface Segregation Principle (ISP): no client should be forced to depend on methods it does not use.
That is, larger interfaces must be divided into smaller ones.

  - Dependency Inversion Principle (DIP): it has two definitions: (1) high-level modules should not depend on low-level modules
and both must depend on abstractions; and (2) abstractions must not depend on details, but details must depend on abstractions.
The "AnimalSubject" class depends on the "AnimalObserver" abstraction, that is, it depends on an interface instead of a concrete implementation.
This allows different implementations of observers to be injected into the AnimalSubject class without modifying your code.
