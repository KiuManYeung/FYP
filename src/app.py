import ast
import tkinter as tk
import shutil
import os
import traceback




class Application(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.winfo_toplevel().title("Python visualizer")
        self.winfo_toplevel().bind('<Control-Left>', self.previous_img)
        self.winfo_toplevel().bind('<Control-Right>', self.next_img)


        self.img_path = os.path.join(os.path.curdir, "png")
        self.index = 0
        self.graphs = []
        self.namespace = {}
        self.status_variable = tk.StringVar()
        self.status_variable.set("Status: Ready")
        self.setup_widgets()

    def run(self):
        self.status_variable.set("Status: Executing")
        self.lbl_status.update()

        self.index = 0
        self.namespace = {}
        if os.path.isdir(self.img_path):
            shutil.rmtree(self.img_path)
        os.mkdir(self.img_path)
        
        text = self.txt_edit.get(1.0, tk.END)
        src = Handler(text)

        if src.error_msg:
            self.lbl_right.configure(image='')
            self.lbl_right.configure(text=src.error_msg)
        else:
            try:
                exec(compile(src.processed, filename="<src>", mode="exec"), self.namespace)
                self.graphs = [f for f in os.listdir(self.img_path) if f.endswith(".png")]
                if self.graphs:
                    filename = os.path.join(self.img_path, self.graphs[0])
                    img = tk.PhotoImage(file=filename)
                    self.lbl_right.configure(image=img)
                    self.lbl_right.image=img
                else:
                    self.lbl_right.configure(image='')
            except Exception as e:
                self.lbl_right.configure(image='')
                self.lbl_right.configure(text=traceback.format_exc())

    
        self.status_variable.set("Status: Ready")

    def next_img(self, event=None):
        if self.index < len(self.graphs)-1:
            self.index += 1
            filename = os.path.join(self.img_path, self.graphs[self.index])
            img = tk.PhotoImage(file=filename)
            self.lbl_right.configure(image=img)
            self.lbl_right.image=img

    def previous_img(self, event=None):
        if self.index > 0:
            self.index -= 1
            filename = os.path.join(self.img_path, self.graphs[self.index])
            img = tk.PhotoImage(file=filename)
            self.lbl_right.configure(image=img)
            self.lbl_right.image=img

    def setup_widgets(self):
        self.pack(fill="both", expand=True)
        self.columnconfigure(0, weight=1, minsize=500)
        self.columnconfigure(1, weight=1, minsize=500)
        self.rowconfigure(0, weight=1, minsize=490)
        self.rowconfigure(1, weight=0, minsize=20)

        self.lbl_status = tk.Label(self, textvariable=self.status_variable)
        # self.lbl_status = tk.Label(self, text="Status: Ready")
        self.lbl_status.grid(row=1, column=0, columnspan=2, sticky="w")

        self.frm_left = tk.Frame(master=self, relief=tk.RAISED, borderwidth=1)
        self.frm_left.grid(row=0,column=0, sticky="nsew")

        self.frm_right = tk.Frame(master=self, relief=tk.RAISED, borderwidth=1)
        self.frm_right.grid(row=0,column=1, sticky="nsew")

        self.frm_left.columnconfigure(0, weight=1, minsize=500)
        self.frm_left.rowconfigure(0, weight=1, minsize=470)
        self.frm_left.rowconfigure(1, weight=0, minsize=30)

        self.frm_right.columnconfigure(0, weight=1, minsize=250)
        self.frm_right.columnconfigure(1, weight=1, minsize=250)
        self.frm_right.rowconfigure(0, weight=1, minsize=470)
        self.frm_right.rowconfigure(1, weight=0, minsize=30)

        self.txt_edit = tk.Text(master=self.frm_left, width=1, height=1)
        self.txt_edit.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.btn_run = tk.Button(master=self.frm_left, text="Run", height=2, command=self.run)
        self.btn_previous = tk.Button(master=self.frm_right, text="Previous", height=2, command=self.previous_img)
        self.btn_next = tk.Button(master=self.frm_right, text="Next", height=2, command=self.next_img)
        self.btn_run.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.btn_previous.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.btn_next.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.frame_lbl = tk.Frame(self.frm_right, background="white")
        self.frame_lbl.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.lbl_right = tk.Label(self.frame_lbl, justify="left", background="white", wraplength=500)
        self.lbl_right.pack(fill="both", expand=True)



class Handler:
    def __init__(self, original):

        self.error_msg = ""
        try:
            self.original = ast.parse(original)
        except Exception as e:
            # Probably only catches syntax errors
            self.error_msg = traceback.format_exc()
            self.original = ast.parse("")

        self.imports = ast.parse('''
from lolviz import *
import os
''')
        self.clean_lineno(self.imports, -1)

        self.vars = "','".join(list({node.id for node in ast.walk(self.original) if isinstance(node, ast.Name)}))
        
        self.globals = ast.parse('''
global png_counter
global graph_lines''')

        self.graphs = insert = ast.parse('''
mySpecialGraph = callsviz(varnames=[''' + "'" + self.vars + "'" + '''])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, "png", str(png_counter).zfill(4)))
''')
        self.processed = self.original

        self.do_global = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
        self.do_not_follow = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Return, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith, ast.Try, ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal, ast.Pass, ast.Break, ast.Continue)

        
        self.insert_graphs(self.processed)
        self.insert_global(self.processed)
        self.insert_imports(self.processed)

    def lineno_builder(self, line_numbers):
        insert = ast.parse('''print("Executing line: '''+ str(line_numbers) +'''")''')
        return insert
        
    def clean_lineno(self, node, lineno):
        if hasattr(node, 'lineno'):
            node.lineno = lineno
        if hasattr(node, 'body'):
            for element in node.body:
                self.clean_lineno(element, lineno)

    def insert_graphs(self, node):
        if hasattr(node, 'body'):
            if isinstance(node, ast.Try):
                for element in node.orelse:
                    self.insert_graphs(element)  
                temp = []
                for element in node.orelse:
                    temp.append(element)
                    if not isinstance(element, self.do_not_follow):
                        self.clean_lineno(self.graphs, element.lineno)
                        temp = temp + self.graphs.body
                node.orelse = temp

                for element in node.finalbody:
                    self.insert_graphs(element)  
                temp = []
                for element in node.finalbody:
                    temp.append(element)
                    if not isinstance(element, self.do_not_follow):
                        self.clean_lineno(self.graphs, element.lineno)
                        temp = temp + self.graphs.body
                node.finalbody = temp

            for element in node.body:
                self.insert_graphs(element)
            temp = []
            if isinstance(node, self.do_global) :
                temp = temp + self.globals.body
            for element in node.body:
                temp.append(element)
                if not isinstance(element, self.do_not_follow):
                    self.clean_lineno(self.graphs, element.lineno)
                    temp = temp + self.graphs.body
            # if isinstance(node, ast.Module):
            #     temp = temp[:-4]
            node.body = temp

    def insert_imports(self, node):
        node.body = self.imports.body + node.body

    def insert_global(self, node):
        global_variables = ast.parse('''global png_counter
png_counter = 0
global graph_lines
graph_lines = []''')
        i = 0
        for i in range(len(node.body)):
            if not isinstance(node.body[i], (ast.Import, ast.ImportFrom)):
                break
        node.body = node.body[0:i] + global_variables.body + node.body[i:]





if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(1000,500)
    app = Application(master=root)
    root.state('zoomed')
    root.mainloop()