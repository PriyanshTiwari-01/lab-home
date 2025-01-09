import sqlite3
import hashlib
import customtkinter as ctk

# Function to hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify the username and password from the database
def verify_login(username, password):
    # Connect to the database
    with sqlite3.connect("users.db") as con:
        cursor = con.cursor()

        # Query the database for the user
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = cursor.fetchone()

        # If user exists, compare the hashed passwords
        if result:
            stored_password = result[0]
            if stored_password == hash_password(password):
                return True
        return False

# Function to handle login action
def on_login_button_click():
    username = username_entry.get()
    password = password_entry.get()

    # Verify login credentials
    if verify_login(username, password):
        login_status_label.configure(text="Login Successful!", text_color="green")
        app.withdraw()  # Hide the login window
        open_admin_window()  # Open the admin window
    else:
        login_status_label.configure(text="Invalid Username or Password", text_color="red")

# Function to open the admin window after successful login
def open_admin_window():
    admin_window = ctk.CTk()  # Create a new window for the admin tools
    admin_window.title("Admin Tools")
    admin_window.geometry("400x380")

    # Label for Admin Tools (Centered)
    admin_label = ctk.CTkLabel(admin_window, text="Admin Tools Available")
    admin_label.place(relx=0.5, rely=0.3, anchor="center")

    # Example Button for Admin Tool 1
    admin_tool1_button = ctk.CTkButton(admin_window, text="Admin Tool 1", command=lambda: print("Admin Tool 1 Selected"))
    admin_tool1_button.place(relx=0.5, rely=0.4, anchor="center")

    # Example Button for Admin Tool 2
    admin_tool2_button = ctk.CTkButton(admin_window, text="Admin Tool 2", command=lambda: print("Admin Tool 2 Selected"))
    admin_tool2_button.place(relx=0.5, rely=0.5, anchor="center")

    # Example Button for Admin Tool 3
    admin_tool3_button = ctk.CTkButton(admin_window, text="Admin Tool 3", command=lambda: print("Admin Tool 3 Selected"))
    admin_tool3_button.place(relx=0.5, rely=0.6, anchor="center")

    # Run the admin window
    admin_window.mainloop()

# Create the application window (Login Window)
app = ctk.CTk()

# Set the appearance mode to dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app.title("Inventory Management")
app.geometry("400x380")

# Center the window
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

# Button for Login
login_button = ctk.CTkButton(app, text="Login", command=on_login_button_click)
login_button.place(relx=0.5, rely=0.7, anchor="center")

# Label for login status (Feedback to the user)
login_status_label = ctk.CTkLabel(app, text="", text_color="red")
login_status_label.place(relx=0.5, rely=0.8, anchor="center")

# Run the login window
app.mainloop()
