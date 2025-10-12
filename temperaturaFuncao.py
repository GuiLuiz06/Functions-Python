def mensagemInicial():
    return "Seja bem-vindo ao conversor de temperatura!"
def coletaDados():
    return str(input("Você quer converter para celsius ou fahrenheit? ").lower().strip())
def converterParaFahrenheit():
    tempCelsius = float(input("Digite a temperatura em celsius: "))
    calcC = ((tempCelsius * 1.8) + 32)
    return print(tempCelsius, "graus celsius em fahrenheit é:", round(calcC, 2))
def converterParaCelsius():
    tempFahrenheit = float(input("Digite a temperatura em fahrenheit: "))
    calcF = ((tempFahrenheit - 32) * 5 / 9)
    return print(tempFahrenheit, "graus fahrenheit em celsius é:", round(calcF, 2))
def mensagemDeErro():
    return print("Não existe essa conversão. Escolha entre 'Celsius' ou 'Fahrenheit'")

def main():
    Inicial = mensagemInicial()
    print(Inicial)
    dados = coletaDados()
    print("você escolheu:", dados)
    if dados == "celsius":
        converterParaCelsius()
    elif dados == "fahrenheit":
       converterParaFahrenheit()
    else:
       mensagemDeErro()
if __name__ == '__main__':
    main()
