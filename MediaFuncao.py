def boasVindas():
    return print("Seja Bem-Vindo ao sistema que calcula média de notas!!")
def coletaDados():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    return print(f"A média entre {n1} | {n2} | {n3}  é: {round(media, 1)}")
def main():
    boasVindas()
    coletaDados()

if __name__ == '__main__':
    main()
