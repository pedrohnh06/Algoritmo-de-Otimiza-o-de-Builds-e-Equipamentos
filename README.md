# ⚔️ RPG Build Simulator & Arena

Projeto desenvolvido em Python com foco em arquitetura de software e Programação Orientada a Objetos (POO). O sistema simula mecânicas clássicas de RPG, incluindo gerenciamento de inventário dinâmico, cálculo estatístico de dano e um loop de combate por turnos.

## Novas Funcionalidades

- **Sistema de Combate em Arena:** Loop de batalha automatizado com log de combate em tempo real e controle de turnos.
- **Inventário Dinâmico (Slots):** Triagem inteligente de itens, equipando armas e armaduras em seus respectivos slots automaticamente.
- **Mitigação de Dano:** Cálculo de Dano Real baseado na defesa/esquiva percentual do alvo.
- **Herança de Equipamentos:** Separação lógica entre `Armas` (focadas em dano e crítico) e `Armaduras` (focadas em vida e esquiva).
- **Simulador Estatístico:** Motor de amostragem que simula 1000 ataques para calcular o DPS (Dano Por Segundo) médio de diferentes builds.

## Arquitetura do Projeto

O código foi refatorado e dividido em módulos para garantir fácil manutenção e escalabilidade:

* `main.py`: Ponto de entrada do sistema que orquestra os testes e a arena.
* `personagem.py`: Classe principal do herói, gerenciamento de status e lógica de RNG (Random Number Generation) para acertos críticos.
* `equipamento.py`: Implementação da superclasse `Equipamento` e suas filhas (`Arma` e `Armadura`).
* `inimigo.py`: Lógica independente de recebimento e causamento de dano.
* `arena.py`: Motor do loop de combate.
* `simulador.py`: Simula os ataques para encontrar a arma com melhor dano médio.

## Conceitos Avançados Aplicados

- **POO Avançada:** Herança, Encapsulamento genérico e delegação de funções (`super()`).
- **Tipagem Dinâmica:** Uso da função nativa `isinstance()` para controle de fluxo e validação de objetos no inventário.
- **Modularização:** Separação de responsabilidades (Clean Code) evitando "código espaguete".
- **Controle de Fluxo e Loop:** Aplicação de travas matemáticas (`max()`, `min()`) e manipulação de pausas temporais (`time.sleep`).

## Como executar

Certifique-se de ter o Python 3 instalado. Clone o repositório e execute o script principal no terminal:

```bash
python main.py
