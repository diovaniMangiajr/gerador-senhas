"""Interface de usuário para o gerador de senha."""

import customtkinter as ctk
from tkinter import messagebox
from gerador_senha import gerar_senha

# --- Configurações iniciais da interface ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
# Criação da janela principal
janela = ctk.CTk()
janela.title("Gerador de Senha")
janela.geometry("400x450")


# --- Lógica de geração de senha ---
#
def atuaizar_texto_slider(valor: int):
    """
    Essa função será chamada sempre que arrastar o slider

    :param valor: Description
    """
    valor_inteiro = int(valor)
    label_tamanho.configure(text=f"Tamanho da senha: {valor_inteiro}")


def acao_gerar():
    """Essa função será chamada para gerar a senha"""
    try:
        tamanho = int(slider.get())
        maiusc = check_maiusculas.get()
        minusc = check_minusculas.get()
        nums = check_numeros.get()
        simb = check_simbolos.get()

        nova_senha = gerar_senha(tamanho, maiusc, minusc, nums, simb)

        caixa_senha.delete(0, "end")
        caixa_senha.insert(0, nova_senha)

    except ValueError:
        caixa_senha.delete(0, "end")
        caixa_senha.insert(0, "Selecione ao menos uma opção")
        messagebox.showwarning("Aviso", "Selecione ao menos uma opção de caracter.")


# --- Elementos da interface ---
# Título da aplicação
titulo = ctk.CTkLabel(
    janela, text="Gerador de Senha", font=ctk.CTkFont(size=20, weight="bold")
)
titulo.pack(pady=20, padx=10)

# Mostrador do tamanho, começa com um valor padrão
label_tamanho = ctk.CTkLabel(janela, text="Tamanho da senha: 12")
label_tamanho.pack(pady=5)

# O slider
slider = ctk.CTkSlider(janela, from_=4, to=30, command=atuaizar_texto_slider)
slider.set(12)
slider.pack(pady=12)

# --- ÁREA DOS CHECKBOXES ---
# Cria um "Frame" (caixa invisível) para organizar os checkboxes
frame_opcoes = ctk.CTkFrame(janela)
frame_opcoes.pack(pady=20)

check_maiusculas = ctk.CTkCheckBox(frame_opcoes, text="A-Z (Maiúsculas)")
check_maiusculas.pack(pady=5, padx=10, anchor="w")
check_maiusculas.select()

check_minusculas = ctk.CTkCheckBox(frame_opcoes, text="a-z (Minúsculas)")
check_minusculas.pack(pady=5, padx=10, anchor="w")
check_minusculas.select()

check_numeros = ctk.CTkCheckBox(frame_opcoes, text="0-9 (Números)")
check_numeros.pack(pady=5, padx=10, anchor="w")
check_numeros.select()

check_simbolos = ctk.CTkCheckBox(frame_opcoes, text="$!@ (Símbolos)")
check_simbolos.pack(pady=5, padx=10, anchor="w")
check_simbolos.select()

# Caixa onde a senha vai ser exibida
caixa_senha = ctk.CTkEntry(janela, width=250, font=ctk.CTkFont(size=14))
caixa_senha.pack(pady=10, padx=10)

# O botão principal que vai gerar a senha
botao_gerar = ctk.CTkButton(janela, text="Gerar nova senha", command=acao_gerar)
botao_gerar.pack(pady=10)

janela.mainloop()
