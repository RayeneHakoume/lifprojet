import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.constants import BOTTOM, RIGHT
from tkinter import font as fontTk
import pandas as pd 

root = tk.Tk()
root.geometry("750x600")
root.pack_propagate(False)
root.resizable(0, 0)

# Mise en place de la police
f = fontTk.Font(family='Comic Sans MS')

frame1 = tk.LabelFrame(root, text="Affichage des données")
frame1['font'] = f
frame1.place(height=308, width=600)

file_frame = tk.LabelFrame(root, text="Ouvrir")
file_frame.place(height = 150, width = 400, rely= 0.65, relx = 0)

btn1 = tk.Button(file_frame, text="Rechercher", command=lambda: File_dialog())
btn1['font'] = f
btn1.place(rely=0.65, relx=0.50)

btn2 = tk.Button(file_frame, text="Charger", command=lambda: Load_excel_data())
btn2.place(rely=0.65, relx=0.30)

btnQuit = tk.Button(root, text="QUITTER", bg="red", )
btnQuit.place(rely=0.95, relx=0.89)

label_file = ttk.Label(file_frame, text="Aucun fichier selectionné")
label_file.place(rely=0, relx=0)

tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")

def File_dialog():
	filename = filedialog.askopenfilename(initialdir="~", title="Selectionner un fichier", filetypes=(("csv files", "*.csv"),("JSON files", "*.json"),("xlsx files", "*.xlsx"),("Tous les fichiers", "*.*")))
	print(filename)
	
	label_file["text"] = filename
	return None

def Load_excel_data():
	file_path = label_file["text"]
	try:
		excel_filename = r"{}".format(file_path) 
		if excel_filename[-4:] == ".csv":
			df = pd.read_csv(excel_filename)
			
			print(excel_filename)
		else:
			df = pd.read_json(excel_filename)

	except ValueError:
		tk.messagebox.showerror("Information", "Le fichier que vous avez choisi est invalide")
		return None
	except FileNotFoundError:
		tk.messagebox.showerror("Information", "Il n'y a pas de ficher dans {file_path}")

	clear_data()
	tv1["column"] = list(df.columns)
	tv1["show"] = "headings"
	for column in tv1["columns"]:
		tv1.heading(column, text=column)

	df_rows = df.to_numpy().tolist()
	for row in df_rows:
		tv1.insert("", "end", values=row)
	return None

		


def clear_data():
	tv1.delete(*tv1.get_children())
	return None






root.mainloop()
