# Calculadora de Saúde

Trabalho da disciplina de Garantia da Qualidade de Software (Lista de Exercícios IV).
Grupo: 
Lucas Paiva Magalhães - RA: 4251925101
Anthony Rafael Braga Magalhães - RA: 4251924039
Guilherme de Oliveira Navais - RA: 4251923674
Luca Fernandes - RA: RA 4251924436

## Sobre o projeto

É um programa em Python que roda no terminal e faz três contas relacionadas a saúde:

- **IMC** — você digita seu peso e altura e ele calcula o índice, dizendo se você está abaixo do peso, no peso normal, com sobrepeso ou obesidade.
- **Água por dia** — calcula quantos litros de água você deveria beber por dia com base no seu peso (a conta usa 35 ml para cada quilo).
- **Frequência cardíaca máxima** — estima os batimentos máximos usando a fórmula 220 menos a sua idade.

Tem também uma opção 4 para sair do programa.

O código que recebemos estava cheio de erros de propósito. A ideia do exercício era rodar o programa, descobrir o que estava quebrado e arrumar.

## Bugs que encontrei

Quando rodei o programa pela primeira vez, ele nem funcionava direito: qualquer número que eu digitasse no menu caía em "Opção inválida" e ficava repetindo o menu pra sempre. Depois que arrumei isso, consegui testar as outras opções e achar o resto dos problemas.

| Onde estava o bug | O que acontecia de errado | O que eu fiz pra corrigir |
|---|---|---|
| `main()`, nos `if opcao == 1` | O menu lê a opção com `input()`, que devolve texto, mas a comparação era com número. Então `"1" == 1` dava falso e nenhuma opção funcionava. | Coloquei as aspas nas comparações: `if opcao == "1"`. |
| `main()`, na opção 4 | Ao escolher "Sair", ele imprimia as mensagens de despedida mas voltava pro menu de novo. Não tinha como fechar o programa. | Adicionei o `break` no final, pra sair do `while True`. |
| `calcular_imc()` | A altura estava sendo multiplicada por 2 em vez de elevada ao quadrado. Com 70 kg e 1,75 m dava IMC 20, sendo que o certo é 22,86. | Troquei `altura * 2` por `altura ** 2`. |
| `classificar_imc()` | As faixas tinham buracos. Um IMC de exatamente 18.5, ou 24.95, não entrava em nenhum `if`, e aí aparecia "Classificação: None". | Reescrevi as faixas de forma contínua (`< 18.5`, `< 25.0`, `< 30.0`, `else`), assim todo valor cai em alguma categoria. |
| `calcular_agua_diaria()` | Estava dividindo o peso por 35 em vez de multiplicar por 35 ml. Com 100 kg dava 2,86 L, mas o correto é 3,5 L. | Mudei para `(peso * 35) / 1000`, multiplicando por 35 ml e convertendo pra litros. |
| `calcular_frequencia_cardiaca_maxima()` | Estava somando a idade em vez de subtrair. Pra 30 anos dava 250 bpm, que não faz sentido nenhum. | Troquei o `+` por `-`: `220 - idade`. |
| `menu()` e leitura de peso/altura/idade | Se eu digitasse uma letra ou apertasse Enter sem escrever nada, o programa quebrava com erro. E se colocasse altura 0, dava divisão por zero. | Criei a função `ler_numero()` que verifica se o que foi digitado é número mesmo e pergunta de novo quando não é. Também aceita vírgula no lugar do ponto (1,75). |

## Como executar

Você precisa ter o Python 3 instalado. Pra conferir, digite no terminal:

```bash
python --version
```

O programa não usa nenhuma biblioteca externa, então não precisa instalar mais nada.

Depois é só clonar o repositório e rodar:

```bash
git clone https://github.com/SEU-USUARIO/gqs-calculadora-saude-py.git
cd gqs-calculadora-saude-py
python calculadora_saude.py
```

(No Linux ou no Mac, use `python3` no lugar de `python`.)

Quando o menu aparecer, digite o número da opção que você quer e aperte Enter.

## Exemplo rodando

```
==============================
  SISTEMA DE SAÚDE E BEM-ESTAR
==============================
1. Calcular IMC
2. Calcular Recomendação de Água
3. Calcular Frequência Cardíaca Máxima
4. Sair
Escolha uma opção (1-4): 1
Digite seu peso (kg): 70
Digite sua altura (m): 1.75
Seu IMC é: 22.86
Classificação: Peso normal
```

## Testes que fiz

Depois de arrumar tudo, testei as quatro opções do menu. Usei 70 kg e 1,75 m no IMC (deu 22,86, peso normal), 70 kg na água (2,45 L) e 30 anos na frequência cardíaca (190 bpm) — conferi as contas na calculadora e bateram. Também testei digitar uma opção que não existe (o programa avisa e mostra o menu de novo), digitar letra no lugar do peso (ele pede de novo em vez de quebrar) e a opção 4, que agora encerra de verdade.