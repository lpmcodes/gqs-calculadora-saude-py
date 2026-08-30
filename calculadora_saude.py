# calculadora_saude.py

def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    # IMC = peso dividido pela altura ao quadrado
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Faixas contínuas: todo valor de IMC cai em alguma classificação
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

def calcular_agua_diaria(peso):
    # 35 ml de água por kg de peso, convertidos de ml para litros
    litros = (peso * 35) / 1000
    return litros

def calcular_frequencia_cardiaca_maxima(idade):
    # Fórmula: 220 menos a idade
    fc_max = 220 - idade
    return fc_max

def ler_numero(mensagem, tipo=float):
    # Pergunta de novo enquanto o usuário não digitar um número válido
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = tipo(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if valor <= 0:
            print("Valor inválido! Digite um número maior que zero.")
            continue

        return valor

def menu():
    print("\n" + "="*30)
    print("  SISTEMA DE SAÚDE E BEM-ESTAR  ")
    print("="*30)
    print("1. Calcular IMC")
    print("2. Calcular Recomendação de Água")
    print("3. Calcular Frequência Cardíaca Máxima")
    print("4. Sair")

    # input() sempre devolve texto, entao usamos strip() e comparamos com strings no main()
    opcao = input("Escolha uma opção (1-4): ").strip()
    return opcao

def main():
    while True:
        opcao = menu()

        if opcao == "1":
            peso = ler_numero("Digite seu peso (kg): ")
            altura = ler_numero("Digite sua altura (m): ")
            imc = calcular_imc(peso, altura)
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificar_imc(imc)}")

        elif opcao == "2":
            peso = ler_numero("Digite seu peso (kg): ")
            qtd_agua = calcular_agua_diaria(peso)
            print(f"Sua meta diária de água é: {qtd_agua:.2f} Litros")

        elif opcao == "3":
            idade = ler_numero("Digite sua idade: ", tipo=int)
            fc = calcular_frequencia_cardiaca_maxima(idade)
            print(f"Sua Frequência Cardíaca Máxima estimada é: {fc} bpm")

        elif opcao == "4":
            print("Encerrando o sistema...")
            print("Obrigado por usar nosso sistema!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()