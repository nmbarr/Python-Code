import customtkinter as ctk

GUI_WIDTH = 1200
GUI_HEIGHT = 720
GUI_SIZE = f"{str(GUI_WIDTH)}x{str(GUI_HEIGHT)}"
GUI_TITLE = "SLC-2W MODBUS GUI"
GUI_APPEARANCE = "Dark"

TABS = ["LN2 PLC A", "LN2 PLC B", "LN2 OFFLOAD PLC", "LOX OFFLOAD PLC"]
SERVER_CONNECT_BUTTON_TEXT = "Connect"

# Define GUI object
app = ctk.CTk()

# Define GUI style parameters
app.geometry(GUI_SIZE)
app.title(GUI_TITLE)
app._set_appearance_mode(GUI_APPEARANCE)

tabview = ctk.CTkTabview(master = app, width = GUI_WIDTH, height = GUI_HEIGHT)
tabview.pack(padx=100, pady=100)

for tab in TABS:
    tabview.add(tab)
    button = ctk.CTkButton(master = tabview.tab(tab), text = SERVER_CONNECT_BUTTON_TEXT)
    button.pack(padx = 20, pady = 20)

tabview.set(TABS[0])

# Main loop to execute GUI. Must be at the end.
app.mainloop()