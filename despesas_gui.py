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
            despesas.append({'nome': nome, 'valor': valor})
            messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
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
root.config(bg="#f2f2f2")

titulo = tk.Label(root, text="Calculadora de Despesas", font=("Arial", 18, "bold"), bg="#f2f2f2")
titulo.pack(pady=20)

btn_adicionar = tk.Button(root, text="Adicionar Despesa", width=30, height=2, command=adicionar_despesa)
btn_adicionar.pack(pady=5)

btn_listar = tk.Button(root, text="Listar Despesas", width=30, height=2, command=listar_despesas)
btn_listar.pack(pady=5)

btn_remover = tk.Button(root, text="Remover Despesa", width=30, height=2, command=remover_despesa)
btn_remover.pack(pady=5)

btn_total = tk.Button(root, text="Calcular Total", width=30, height=2, command=calcular_total)
btn_total.pack(pady=5)

btn_sair = tk.Button(root, text="Sair", width=30, height=2, command=root.quit)
btn_sair.pack(pady=20)

root.mainloop()
