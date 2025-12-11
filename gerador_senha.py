"""Projeto de gerador de senhas."""

from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import shuffle


def gerar_senha(
    tamanho: int,
    usar_maiusculas: bool,
    usar_minusculas: bool,
    usar_numeros: bool,
    usar_simbolos: bool,
) -> str:
    """
    Gera uma senha com base nas escolhas de caracteres e tamanho.
    Uso da biblioteca secret para maior grau de segurança
    na geração de novas senhas.

    :param tamanho: Comprimento da senha
    :type tamanho: int
    :param usar_maiusculas: Incluir letras maiúsculas
    :type usar_maiusculas: bool
    :param usar_minusculas: Incluir letras minúsculas
    :type usar_minusculas: bool
    :param usar_numeros: Incluir números
    :type usar_numeros: bool
    :param usar_simbolos: Incluir símbolos
    :type usar_simbolos: bool
    :return: Senha gerada
    :rtype: string
    """

    if tamanho <= 3:
        raise ValueError("O tamanho da senha deve ser maior que 3.")

    maiusculas = ascii_uppercase
    minusculas = ascii_lowercase
    numeros = digits
    simbolos = punctuation

    senha = ""
    todos_caracteres = ""
    # Garantir que pelo menos um caractere de cada tipo selecionado seja incluído na senha.
    if usar_maiusculas:
        senha += "".join(choice(maiusculas))
        todos_caracteres += maiusculas
    if usar_minusculas:
        senha += "".join(choice(minusculas))
        todos_caracteres += minusculas
    if usar_numeros:
        senha += "".join(choice(numeros))
        todos_caracteres += numeros
    if usar_simbolos:
        senha += "".join(choice(simbolos))
        todos_caracteres += simbolos

    if not todos_caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
    while len(senha) < tamanho:
        senha += "".join(choice(todos_caracteres))
    # Transforma a string senha em lista para embaralhar com Shuffle
    list_senha = list(senha)
    shuffle(list_senha)
    senha.join(list_senha)

    return senha


if __name__ == "__main__":
    # Exemplo de uso
    senha_gerada = gerar_senha(
        tamanho=12,
        usar_maiusculas=True,
        usar_minusculas=True,
        usar_numeros=True,
        usar_simbolos=True,
    )
    print(f"Senha gerada: {senha_gerada}")
