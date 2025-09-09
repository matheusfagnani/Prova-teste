# função para classificar o triângulo:
def classificar_triangulo(a, b, c):
    # Verifica se os lados formam um triângulo válido
    if a <= 0 or b <= 0 or c <= 0:
        return "Não é um triângulo"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"

    # Classifica o triângulo
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"
    
# Exemplo de uso:
if __name__ == "__main__":
    lado1 = float(input("Digite o comprimento do lado 1: "))
    lado2 = float(input("Digite o comprimento do lado 2: "))
    lado3 = float(input("Digite o comprimento do lado 3: "))
    
    resultado = classificar_triangulo(lado1, lado2, lado3)
    print(f"O triângulo é: {resultado}")
# função para classificar o triângulo:
def classificar_triangulo(a, b, c):
    # Verifica se os lados formam um triângulo válido
    if a <= 0 or b <= 0 or c <= 0:
        return "Não é um triângulo"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"

    # Classifica o triângulo
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

    