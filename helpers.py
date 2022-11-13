import sys
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg

def get_path() -> str:
    """Get path and return it as string
    
    """
    path= sys.argv[0]
    path_split= path.split("/")
    path_split = path_split[:-1]
    slash= "\\"[0]
    path = ""
    for i in path_split:
        path = path + slash + i

    return path[1:] + slash

def show_table(excel_name :str):
        try:

            df = pd.read_excel(get_path() + excel_name + ".xlsx")
            df.plot()
            plt.show()

        except FileNotFoundError as e:

            try:

                df = pd.read_excel(get_path() + excel_name + ".xls")
                df.plot()
                plt.show()

            except FileNotFoundError:

                sg.popup(title="File not found, please try again" ,custom_text="ok")
