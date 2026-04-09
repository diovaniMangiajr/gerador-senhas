"""Interface de usuário para o gerador de senha."""

import customtkinter as ctk
from tkinter import messagebox
from gerador_senha import gerar_senha

# --- Configurações iniciais da interface ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    def __init__(self):
        # Inicia a classe mãe
        super().__init__()

        # Criação da self principal
        self.title("Gerador de Senha")
        self.geometry("400x500")

        # --- Elementos da interface ---
        # Título da aplicação
        self.titulo = ctk.CTkLabel(
            self, text="Gerador de Senha", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.titulo.pack(pady=20, padx=10)

        # Mostrador do tamanho, começa com um valor padrão
        self.label_tamanho = ctk.CTkLabel(self, text="Tamanho da senha: 12")
        self.label_tamanho.pack(pady=5)

        # O slider
        self.slider = ctk.CTkSlider(self, from_=4, to=30, command=self.atuaizar_texto_slider)
        self.slider.set(12)
        self.slider.pack(pady=12)

        # --- ÁREA DOS CHECKBOXES ---
        # Cria um "Frame" (caixa invisível) para organizar os checkboxes
        self.frame_opcoes = ctk.CTkFrame(self)
        self.frame_opcoes.pack(pady=20)

        self.check_maiusculas = ctk.CTkCheckBox(self.frame_opcoes, text="A-Z (Maiúsculas)")
        self.check_maiusculas.pack(pady=5, padx=10, anchor="w")
        self.check_maiusculas.select()

        self.check_minusculas = ctk.CTkCheckBox(self.frame_opcoes, text="a-z (Minúsculas)")
        self.check_minusculas.pack(pady=5, padx=10, anchor="w")
        self.check_minusculas.select()

        self.check_numeros = ctk.CTkCheckBox(self.frame_opcoes, text="0-9 (Números)")
        self.check_numeros.pack(pady=5, padx=10, anchor="w")
        self.check_numeros.select()

        self.check_simbolos = ctk.CTkCheckBox(self.frame_opcoes, text="$!@ (Símbolos)")
        self.check_simbolos.pack(pady=5, padx=10, anchor="w")
        self.check_simbolos.select()

        # --- Área de Resultado (Caixa + Botão Copiar) ---
        # A caixa de senha vai dentro do frame_resultado
        self.caixa_senha = ctk.CTkEntry(self, width=250, font=ctk.CTkFont(size=14))
        self.caixa_senha.pack(pady=10, padx=10)

        # O botão principal que vai gerar a senha
        self.botao_gerar = ctk.CTkButton(self, text="Gerar nova senha", command=self.acao_gerar)
        self.botao_gerar.pack(pady=10, padx=10)

        # Botão de copiar
        self.botao_copiar = ctk.CTkButton(self, text="Copiar", width=70, command=self.copiar_senha)
        self.botao_copiar.pack(pady=10, padx=10)


    # --- Lógica de geração de senha ---
    #
    def atuaizar_texto_slider(self, valor: int):
        """
        Essa função será chamada sempre que arrastar o slider

        :param valor: Description
        """
        valor_inteiro = int(valor)
        self.label_tamanho.configure(text=f"Tamanho da senha: {valor_inteiro}")


    def acao_gerar(self):
        """Essa função será chamada para gerar a senha"""
        try:
            tamanho = int(self.slider.get())
            maiusc = self.check_maiusculas.get()
            minusc = self.check_minusculas.get()
            nums = self.check_numeros.get()
            simb = self.check_simbolos.get()

            nova_senha = gerar_senha(tamanho, maiusc, minusc, nums, simb)

            self.caixa_senha.delete(0, "end")
            self.caixa_senha.insert(0, nova_senha)

        except ValueError:
            self.caixa_senha.delete(0, "end")
            self.caixa_senha.insert(0, "Selecione ao menos uma opção")
            messagebox.showwarning("Aviso", "Selecione ao menos uma opção de caracter.")
    

    def copiar_senha(self):
        """Copia a senha gerada para a área de transferência do sistema."""
        senha_atual = self.caixa_senha.get()
        
        # Verifica se a caixa não está vazia e se não é a mensagem de erro
        if senha_atual and senha_atual != "Selecione ao menos uma opção":
            # Limpa o clipboard do sistema e adiciona a nova senha
            self.clipboard_clear()
            self.clipboard_append(senha_atual)
            self.update() # Força a atualização (importante para funcionar bem no Linux)

            # Feedback visual: muda o texto do botão temporariamente
            self.botao_copiar.configure(text="Copiado!")
            
            # Depois de 2 segundos (2000 ms), volta o botão para "Copiar"
            self.after(2000, lambda: self.botao_copiar.configure(text="Copiar"))

if __name__ == "__main__":
    app = App()
    app.mainloop()
