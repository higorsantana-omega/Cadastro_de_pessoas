from PIL import Image, ImageTk
import database
import sqlite3

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

root = tk.Tk()

class GUI_:
    def __init__(self):
        self.root = root
        self.root.geometry("550x450+418+131")
        self.root.title('Cadastro de Clientes')
        self.root.configure(background="#d9d9d9")
        self.labels()
        self.tree_view()
        self.tree__()
        self.root.mainloop()
    
    def labels(self):
        font10 = "-family {Trebuchet MS} -size 16 -weight bold"
        font12 = "-family {Trebuchet MS} -size 9 -weight bold"
        font14 = "-family {Trebuchet MS} -size 12"
        font15 = "-family {Trebuchet MS} -size 11"

        self.Lb_CadastroCliente = tk.Label(self.root)
        self.Lb_CadastroCliente.place(relx=0.0, rely=0.0, height=50, width=400)
        self.Lb_CadastroCliente.configure(anchor='w')
        self.Lb_CadastroCliente.configure(background="#c6eaec")
        self.Lb_CadastroCliente.configure(disabledforeground="#a3a3a3")
        self.Lb_CadastroCliente.configure(font=font10)
        self.Lb_CadastroCliente.configure(foreground="#ffffff")
        self.Lb_CadastroCliente.configure(text='''Cadastro de Clientes''')

        self.Lb_ProcurarNome = tk.Label(self.root)
        self.Lb_ProcurarNome.place(relx=0.491, rely=0.0, height=20, width=126)
        self.Lb_ProcurarNome.configure(background="#c6eaec")
        self.Lb_ProcurarNome.configure(cursor="fleur")
        self.Lb_ProcurarNome.configure(disabledforeground="#a3a3a3")
        self.Lb_ProcurarNome.configure(font=font12)
        self.Lb_ProcurarNome.configure(foreground="#ffffff")
        self.Lb_ProcurarNome.configure(text='''Procurar pelo nome:''')

        self.Lb_ProcurarTelefone = tk.Label(self.root)
        self.Lb_ProcurarTelefone.place(relx=0.473, rely=0.056, height=20
                , width=136)
        self.Lb_ProcurarTelefone.configure(activebackground="#f9f9f9")
        self.Lb_ProcurarTelefone.configure(activeforeground="black")
        self.Lb_ProcurarTelefone.configure(background="#c6eaec")
        self.Lb_ProcurarTelefone.configure(disabledforeground="#a3a3a3")
        self.Lb_ProcurarTelefone.configure(font="-family {Trebuchet MS} -size 9 -weight bold")
        self.Lb_ProcurarTelefone.configure(foreground="#ffffff")
        self.Lb_ProcurarTelefone.configure(highlightbackground="#d9d9d9")
        self.Lb_ProcurarTelefone.configure(highlightcolor="black")
        self.Lb_ProcurarTelefone.configure(text='''Procurar pelo telefone:''')

        self.Ent_ProcurarNome = tk.Entry(self.root)
        self.Ent_ProcurarNome.place(relx=0.745, rely=0.011, height=15
                , relwidth=0.244)
        self.Ent_ProcurarNome.configure(background="white")
        self.Ent_ProcurarNome.configure(disabledforeground="#a3a3a3")
        self.Ent_ProcurarNome.configure(font="TkFixedFont")
        self.Ent_ProcurarNome.configure(foreground="#000000")
        self.Ent_ProcurarNome.configure(insertbackground="black")
        self.Ent_ProcurarNome.bind('<Return>', self.ProcurarNome)

        self.Ent_ProcurarTelefone = tk.Entry(self.root)
        self.Ent_ProcurarTelefone.place(relx=0.745, rely=0.067, height=15
                , relwidth=0.244)
        self.Ent_ProcurarTelefone.configure(background="white")
        self.Ent_ProcurarTelefone.configure(disabledforeground="#a3a3a3")
        self.Ent_ProcurarTelefone.configure(font="TkFixedFont")
        self.Ent_ProcurarTelefone.configure(foreground="#000000")
        self.Ent_ProcurarTelefone.configure(highlightbackground="#d9d9d9")
        self.Ent_ProcurarTelefone.configure(highlightcolor="black")
        self.Ent_ProcurarTelefone.configure(insertbackground="black")
        self.Ent_ProcurarTelefone.configure(selectbackground="#c4c4c4")
        self.Ent_ProcurarTelefone.configure(selectforeground="black")
        self.Ent_ProcurarTelefone.bind('<Return>', self.ProcurarTel)

        self.Lb_Nome_Sobrenome = tk.Label(self.root)
        self.Lb_Nome_Sobrenome.place(relx=0.0, rely=0.222, height=20, width=134)
        self.Lb_Nome_Sobrenome.configure(background="#d9d9d9")
        self.Lb_Nome_Sobrenome.configure(disabledforeground="#a3a3a3")
        self.Lb_Nome_Sobrenome.configure(font=font14)
        self.Lb_Nome_Sobrenome.configure(foreground="#000000")
        self.Lb_Nome_Sobrenome.configure(text='''Nome completo:''')

        self.Lb_Telefone = tk.Label(self.root)
        self.Lb_Telefone.place(relx=0.0, rely=0.289, height=20, width=134)
        self.Lb_Telefone.configure(activebackground="#f9f9f9")
        self.Lb_Telefone.configure(activeforeground="black")
        self.Lb_Telefone.configure(background="#d9d9d9")
        self.Lb_Telefone.configure(disabledforeground="#a3a3a3")
        self.Lb_Telefone.configure(font="-family {Trebuchet MS} -size 12")
        self.Lb_Telefone.configure(foreground="#000000")
        self.Lb_Telefone.configure(highlightbackground="#d9d9d9")
        self.Lb_Telefone.configure(highlightcolor="black")
        self.Lb_Telefone.configure(text='''Telefone:''')

        self.Lb_Foto = tk.Label(self.root)
        self.Lb_Foto.place(relx=0.0, rely=0.356, height=20, width=134)
        self.Lb_Foto.configure(activebackground="#f9f9f9")
        self.Lb_Foto.configure(activeforeground="black")
        self.Lb_Foto.configure(background="#d9d9d9")
        self.Lb_Foto.configure(disabledforeground="#a3a3a3")
        self.Lb_Foto.configure(font="-family {Trebuchet MS} -size 12")
        self.Lb_Foto.configure(foreground="#000000")
        self.Lb_Foto.configure(highlightbackground="#d9d9d9")
        self.Lb_Foto.configure(highlightcolor="black")
        self.Lb_Foto.configure(text='''Foto:''')

        self.Lb_Mais_informações = tk.Label(self.root)
        self.Lb_Mais_informações.place(relx=0.002, rely=0.422, height=21
                , width=134)
        self.Lb_Mais_informações.configure(activebackground="#f9f9f9")
        self.Lb_Mais_informações.configure(activeforeground="black")
        self.Lb_Mais_informações.configure(background="#d9d9d9")
        self.Lb_Mais_informações.configure(disabledforeground="#a3a3a3")
        self.Lb_Mais_informações.configure(font="-family {Trebuchet MS} -size 12")
        self.Lb_Mais_informações.configure(foreground="#000000")
        self.Lb_Mais_informações.configure(highlightbackground="#d9d9d9")
        self.Lb_Mais_informações.configure(highlightcolor="black")
        self.Lb_Mais_informações.configure(text='''Mais informações:''')

        load = Image.open("profile.png")
        load.thumbnail((70, 70))
        self.foto = ImageTk.PhotoImage(load)
        self.Lb_Profile = tk.Label(self.root, image=self.foto)
        self.Lb_Profile.place(relx=0.291, rely=0.511)

        self.Ent_Nome_Sobrenome = tk.Entry(self.root)
        self.Ent_Nome_Sobrenome.place(relx=0.236, rely=0.222, height=22
                , relwidth=0.753)
        self.Ent_Nome_Sobrenome.configure(background="white")
        self.Ent_Nome_Sobrenome.configure(disabledforeground="#a3a3a3")
        self.Ent_Nome_Sobrenome.configure(font="TkFixedFont")
        self.Ent_Nome_Sobrenome.configure(foreground="#000000")
        self.Ent_Nome_Sobrenome.configure(insertbackground="black")

        self.Ent_Telefone = tk.Entry(self.root)
        self.Ent_Telefone.place(relx=0.2, rely=0.289,height=22, relwidth=0.789)
        self.Ent_Telefone.configure(background="white")
        self.Ent_Telefone.configure(disabledforeground="#a3a3a3")
        self.Ent_Telefone.configure(font="TkFixedFont")
        self.Ent_Telefone.configure(foreground="#000000")
        self.Ent_Telefone.configure(highlightbackground="#d9d9d9")
        self.Ent_Telefone.configure(highlightcolor="black")
        self.Ent_Telefone.configure(insertbackground="black")
        self.Ent_Telefone.configure(selectbackground="#c4c4c4")
        self.Ent_Telefone.configure(selectforeground="black")

        self.Ent_Foto = tk.Entry(self.root)
        self.Ent_Foto.place(relx=0.164, rely=0.356,height=22, relwidth=0.716)
        self.Ent_Foto.configure(background="white")
        self.Ent_Foto.configure(disabledforeground="#a3a3a3")
        self.Ent_Foto.configure(font="TkFixedFont")
        self.Ent_Foto.configure(foreground="#000000")
        self.Ent_Foto.configure(highlightbackground="#d9d9d9")
        self.Ent_Foto.configure(highlightcolor="black")
        self.Ent_Foto.configure(insertbackground="black")
        self.Ent_Foto.configure(selectbackground="#c4c4c4")
        self.Ent_Foto.configure(selectforeground="black")

        self.Ent_Mais_Informações = tk.Entry(self.root)
        self.Ent_Mais_Informações.place(relx=0.255, rely=0.422, height=22
                , relwidth=0.735)
        self.Ent_Mais_Informações.configure(background="white")
        self.Ent_Mais_Informações.configure(disabledforeground="#a3a3a3")
        self.Ent_Mais_Informações.configure(font="TkFixedFont")
        self.Ent_Mais_Informações.configure(foreground="#000000")
        self.Ent_Mais_Informações.configure(highlightbackground="#d9d9d9")
        self.Ent_Mais_Informações.configure(highlightcolor="black")
        self.Ent_Mais_Informações.configure(insertbackground="black")
        self.Ent_Mais_Informações.configure(selectbackground="#c4c4c4")
        self.Ent_Mais_Informações.configure(selectforeground="black")

        self.Bt_Foto = tk.Button(self.root)
        self.Bt_Foto.place(relx=0.891, rely=0.356, height=22, width=53)
        self.Bt_Foto.configure(activebackground="#ececec")
        self.Bt_Foto.configure(activeforeground="#000000")
        self.Bt_Foto.configure(background="#d9d9d9")
        self.Bt_Foto.configure(disabledforeground="#a3a3a3")
        self.Bt_Foto.configure(foreground="#000000")
        self.Bt_Foto.configure(highlightbackground="#d9d9d9")
        self.Bt_Foto.configure(highlightcolor="black")
        self.Bt_Foto.configure(pady="0")
        self.Bt_Foto.configure(text='''Procurar''')

        self.Bt_AddCliente = tk.Button(self.root)
        self.Bt_AddCliente.place(relx=0.009, rely=0.511, height=24, width=147)
        self.Bt_AddCliente.configure(activebackground="#ececec", command=self.adicionar_pessoa)
        self.Bt_AddCliente.configure(activeforeground="#000000")
        self.Bt_AddCliente.configure(background="#c6eaec")
        self.Bt_AddCliente.configure(disabledforeground="#a3a3a3")
        self.Bt_AddCliente.configure(font=font15)
        self.Bt_AddCliente.configure(foreground="#000000")
        self.Bt_AddCliente.configure(highlightbackground="#d9d9d9")
        self.Bt_AddCliente.configure(highlightcolor="black")
        self.Bt_AddCliente.configure(pady="0")
        self.Bt_AddCliente.configure(text='''Adicionar Cliente''')

        self.Bt_Deletar = tk.Button(self.root)
        self.Bt_Deletar.place(relx=0.009, rely=0.578, height=24, width=147)
        self.Bt_Deletar.configure(activebackground="#ececec", command=self.del_pessoa)
        self.Bt_Deletar.configure(activeforeground="#000000")
        self.Bt_Deletar.configure(background="#c6eaec")
        self.Bt_Deletar.configure(disabledforeground="#a3a3a3")
        self.Bt_Deletar.configure(font="-family {Trebuchet MS} -size 11")
        self.Bt_Deletar.configure(foreground="#000000")
        self.Bt_Deletar.configure(highlightbackground="#d9d9d9")
        self.Bt_Deletar.configure(highlightcolor="black")
        self.Bt_Deletar.configure(pady="0")
        self.Bt_Deletar.configure(text='''Deletar Selecionado''')

        self.Bt_Editar = tk.Button(self.root)
        self.Bt_Editar.place(relx=0.009, rely=0.644, height=24, width=147)
        self.Bt_Editar.configure(activebackground="#ececec")
        self.Bt_Editar.configure(activeforeground="#000000")
        self.Bt_Editar.configure(background="#c6eaec")
        self.Bt_Editar.configure(disabledforeground="#a3a3a3")
        self.Bt_Editar.configure(font="-family {Trebuchet MS} -size 11")
        self.Bt_Editar.configure(foreground="#000000")
        self.Bt_Editar.configure(highlightbackground="#d9d9d9")
        self.Bt_Editar.configure(highlightcolor="black")
        self.Bt_Editar.configure(pady="0")
        self.Bt_Editar.configure(text='''Editar Selecionado''')

        self.Bt_OrdemNome = tk.Button(self.root)
        self.Bt_OrdemNome.place(relx=0.009, rely=0.711, height=24, width=147)
        self.Bt_OrdemNome.configure(activebackground="#ececec", command=self.sort_by_name)
        self.Bt_OrdemNome.configure(activeforeground="#000000")
        self.Bt_OrdemNome.configure(background="#c6eaec")
        self.Bt_OrdemNome.configure(disabledforeground="#a3a3a3")
        self.Bt_OrdemNome.configure(font="-family {Trebuchet MS} -size 11")
        self.Bt_OrdemNome.configure(foreground="#000000")
        self.Bt_OrdemNome.configure(highlightbackground="#d9d9d9")
        self.Bt_OrdemNome.configure(highlightcolor="black")
        self.Bt_OrdemNome.configure(pady="0")
        self.Bt_OrdemNome.configure(text='''Ordenar por Nome''')

        self.Bt_Sair = tk.Button(self.root)
        self.Bt_Sair.place(relx=0.009, rely=0.778, height=24, width=147)
        self.Bt_Sair.configure(activebackground="#ececec")
        self.Bt_Sair.configure(activeforeground="#000000")
        self.Bt_Sair.configure(background="#c6eaec")
        self.Bt_Sair.configure(disabledforeground="#a3a3a3")
        self.Bt_Sair.configure(font="-family {Trebuchet MS} -size 11")
        self.Bt_Sair.configure(foreground="#000000")
        self.Bt_Sair.configure(highlightbackground="#d9d9d9")
        self.Bt_Sair.configure(highlightcolor="black")
        self.Bt_Sair.configure(pady="0")
        self.Bt_Sair.configure(text='''Sair''')

        self.TSeparator1 = ttk.Separator(self.root)
        self.TSeparator1.place(relx=0.0, rely=0.2, relwidth=1.0)

        self.TSeparator2 = ttk.Separator(self.root)
        self.TSeparator2.place(relx=-0.018, rely=0.844, relwidth=1.036)
    
    def tree_view(self):
        self.tree = ttk.Treeview(self.root, columns=(1, 2, 3), height=5, show ="headings")
        self.tree.place(relx=0.407, rely=0.511, relheight=0.327
                ,relwidth=0.584)
        self.tree.heading(1, text ="ID")
        self.tree.heading(2, text = "Nome")
        self.tree.heading(3, text = "Telefone")
        self.tree.column(1, width=1)
        self.tree.column(2, width=1)
        self.tree.column(3, width=1)

    def tree__(self):
        conn = sqlite3.connect('pessoas.db')
        cur = conn.cursor()
        sel_tree = cur.execute('SELECT * FROM pessoas_dados')
        for row in sel_tree:
            self.tree.insert('' , 'end' , values = row)
        cur.close()

    def adicionar_pessoa(self):
        self.nome_get = self.Ent_Nome_Sobrenome.get()
        self.tel_get = self.Ent_Telefone.get()
        conn = sqlite3.connect('pessoas.db')
        cur = conn.cursor()
        sel_tree = cur.execute("INSERT INTO pessoas_dados (`nome`, `tel`) values (?, ?)", (self.nome_get, self.tel_get))
        conn.commit()
        conn.close()

        self.Ent_Nome_Sobrenome.delete(0, 'end')
        self.Ent_Telefone.delete(0, 'end')
        
        conn = sqlite3.connect('pessoas.db')
        cur = conn.cursor()
        sel = cur.execute('SELECT * FROM pessoas_dados ORDER BY id DESC')
        sel = list(sel)
        self.tree.insert('', 'end', values=sel[0])
        conn.close()

    def del_pessoa(self):
        del_sel = self.tree.item(self.tree.selection())['values'][0]
        self.tree.delete(self.tree.selection())
        conn = sqlite3.connect('pessoas.db')
        cur = conn.cursor()
        del_tree = cur.execute(f'DELETE FROM pessoas_dados WHERE id = {del_sel}')
        conn.commit()
        conn.close()

    def sort_by_name(self):
        for l in self.tree.get_children():
            self.tree.delete(l)
        
        conn = sqlite3.connect('pessoas.db')
        cursor = conn.cursor()
        sel = cursor.execute('SELECT * FROM pessoas_dados ORDER BY nome ASC')

        for row in sel:
            self.tree.insert('', 'end', values = row)

    def ProcurarNome(self, event):
        for x in self.tree.get_children():
            self.tree.delete(x)
        nome1 = self.Ent_ProcurarNome.get()
        conn = sqlite3.connect('pessoas.db')
        cursor = conn.cursor()
        sel = cursor.execute("SELECT * FROM pessoas_dados WHERE nome = (?)", (nome1,))
        print(f'Selecionado {sel}')
        conn.commit()
        for row in sel:
            self.tree.insert('', 'end', values = row)
        conn.close()

    def ProcurarTel(self, event):
        for x in self.tree.get_children():
            self.tree.delete(x)
        tel = self.Ent_ProcurarTelefone.get()
        conn = sqlite3.connect('pessoas.db')
        cursor = conn.cursor()
        sel = cursor.execute("SELECT * FROM pessoas_dados WHERE tel = (?)", (tel,))
        print(f'Selecionado {sel}')
        conn.commit()
        for row in sel:
            self.tree.insert('', 'end', values = row)
        conn.close()

if __name__ == "__main__":
        database.InitDB()
        GUI_()

