import  tkinter as tk
from TaskGui import TaskGui

if __name__ == '__main__':
    window = tk.Tk() # loo põhiaken
    taskgui = TaskGui(window) # loo HUI aga amma aken kaasa



    window.mainloop() # viimane rida koodis :)
