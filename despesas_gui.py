"""
Calculadora de Despesas Pessoais com Interface Gráfica (Tkinter)
Professor: Max. Müller
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

despesas = []

def adicionar_despesa():
    nome = simpledialog.askstring("Adicionar Despesa", "Descrição da despesa:")
    if nome:
        try:
            valor = float(simpledialog.askstring("Adicionar Despesa", "Valor da despesa (R$):"))

            # Nova janela para escolher a categoria
            categoria_window = tk.Toplevel(root)
            categoria_window.title("Selecionar Categoria")

            # Texto explicativo
            tk.Label(categoria_window, text="Selecione a categoria da despesa:").pack(pady=10)

            # Variável para guardar a categoria escolhida
            categoria_var = tk.StringVar(value="Alimentação")

            # Lista de categorias fixas
            categorias = ["Alimentação", "Transporte", "Lazer"]
            categoria_combo = ttk.Combobox(categoria_window, textvariable=categoria_var, values=categorias, state="readonly")
            categoria_combo.pack(pady=5)

            # Função chamada ao clicar em "Confirmar"
            def confirmar_categoria():
                categoria = categoria_var.get() # Pega a categoria selecionada
                # Adiciona a despesa com nome, valor e categoria
                despesas.append({'nome': nome, 'valor': valor, 'categoria': categoria})
                messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
                categoria_window.destroy()

            # Botão para confirmar e adicionar a despesa
            btn_confirmar = tk.Button(categoria_window, text="Confirmar", command=confirmar_categoria)
            btn_confirmar.pack(pady=10)

        except:
            messagebox.showerror("Erro", "Valor inválido!")


def listar_despesas():
    if not despesas:
        messagebox.showinfo("Despesas", "Nenhuma despesa cadastrada.")
        return

    janela_lista = tk.Toplevel(root)
    janela_lista.title("Lista de Despesas")

    tree = ttk.Treeview(janela_lista, columns=("Descrição", "Valor"), show="headings")
    tree.heading("Descrição", text="Descrição")
    tree.heading("Valor", text="Valor (R$)")

    for despesa in despesas:
        tree.insert("", "end", values=(despesa['nome'], f"R$ {despesa['valor']:.2f}"))

    tree.pack(fill="both", expand=True)

def remover_despesa():
    if not despesas:
        messagebox.showinfo("Remover", "Nenhuma despesa para remover.")
        return

    nomes = [f"{i + 1} - {d['nome']} (R$ {d['valor']:.2f})" for i, d in enumerate(despesas)]
    escolha = simpledialog.askinteger("Remover Despesa", 
        "Escolha o número da despesa:\n" + "\n".join(nomes))

    if escolha is not None and 1 <= escolha <= len(despesas):
        removida = despesas.pop(escolha - 1)
        messagebox.showinfo("Remover", f"Despesa '{removida['nome']}' removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Opção inválida!")

def calcular_total():
    total = sum(d['valor'] for d in despesas)
    messagebox.showinfo("Total de Despesas", f"O total das despesas é: R$ {total:.2f}")

# Janela principal
root = tk.Tk()
root.title("Calculadora de Despesas")
root.geometry("400x400")
root.config(bg="#5E1212")

titulo = tk.Label(root, text="CALCULADORA DE DESPESAS", font=("Arial", 18, "bold"), bg="#f2f2f2")
titulo.pack(pady=20)

btn_adicionar = tk.Button(root, text="ADICIONAR DESPESA", font=("Arial", 12, "bold"), width=25, height=2, command=adicionar_despesa)
btn_adicionar.pack(pady=5)

btn_listar = tk.Button(root, text="LISTAR DESPESA", font=("Arial", 12, "bold"), width=25, height=2, command=listar_despesas)
btn_listar.pack(pady=5)

btn_remover = tk.Button(root, text="REMOVER DESPESA", font=("Arial", 12, "bold"), width=25, height=2, command=remover_despesa)
btn_remover.pack(pady=5)

btn_total = tk.Button(root, text="CALCULAR TOTAL", font=("Arial", 12, "bold"), width=25, height=2, command=calcular_total)
btn_total.pack(pady=5)

btn_sair = tk.Button(root, text="SAIR", font=("Arial", 12, "bold"), width=25, height=2, command=root.quit)
btn_sair.pack(pady=20)

root.mainloop()
