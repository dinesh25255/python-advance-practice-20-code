from tkinter import *
import os

# Function to restart the system immediately
def restart_system():
    os.system("shutdown /r /t 1")  # Windows restart command

# Function to restart the system with a delay
def restart_with_time():
    os.system("shutdown /r /t 30")  # Restarts after 30 seconds

# Function to log out the current user
def log_out():
    os.system("shutdown /l")  # Logs out the user

# Function to shut down the system
def shutdown_system():
    os.system("shutdown /s /t 1")  # Shutdown the system

# Create a Tkinter window
st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="pink")

# Restart Button
r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"), 
                  relief=RAISED, cursor="hand2", command=restart_system)
r_button.place(x=150, y=60, height=50, width=200)

# Restart with Time Button
rt_button = Button(st, text="Restart in 30s", font=("Times New Roman", 20, "bold"), 
                   relief=RAISED, cursor="hand2", command=restart_with_time)
rt_button.place(x=150, y=130, height=50, width=200)

# Log Out Button
logout_button = Button(st, text="Log Out", font=("Times New Roman", 20, "bold"), 
                       relief=RAISED, cursor="hand2", command=log_out)
logout_button.place(x=150, y=200, height=50, width=200)

# Shutdown Button
shutdown_button = Button(st, text="Shutdown", font=("Times New Roman", 20, "bold"), 
                         relief=RAISED, cursor="hand2", command=shutdown_system)
shutdown_button.place(x=150, y=270, height=50, width=200)

# Run the Tkinter event loop
st.mainloop()
