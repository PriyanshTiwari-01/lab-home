import customtkinter as ctk

app = ctk.CTk()

# Set the appearance mode to dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app.title("Inventory Management")
app.geometry("400x380")

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")
center_window(app)


# Label for Username (Centered)
Label1 = ctk.CTkLabel(app, text="Enter Your Username")
Label1.place(relx=0.5, rely=0.3, anchor="center")

# Entry for Username (Centered)
username_entry = ctk.CTkEntry(app, placeholder_text="Enter Your Username", width=250)
username_entry.place(relx=0.5, rely=0.4, anchor="center")

# Label for Password (Centered)
Label2 = ctk.CTkLabel(app, text="Enter Your Password")
Label2.place(relx=0.5, rely=0.5, anchor="center")

# Entry for Password (Centered)
password_entry = ctk.CTkEntry(app, placeholder_text="Enter Your Password", width=250, show="*")
password_entry.place(relx=0.5, rely=0.6, anchor="center")

app.mainloop()
