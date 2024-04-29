import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox, filedialog
import requests
import requests_cache
from requests.auth import HTTPBasicAuth

class PyBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyBrowser")
        self.geometry("800x600")
        self.session = requests.Session()  # Use a session object to handle cookies automatically
        requests_cache.install_cache('pybrowser_cache')  # Enable caching

        # Initialize login process
        if self.login():
            self.create_widgets()  # Create main application window if login is successful
        else:
            self.quit()  # Quit the application if login fails

    def login(self):
        # Creating a top-level widget for login
        login_window = tk.Toplevel(self)
        login_window.title("Login")
        login_window.geometry("300x200")
        login_window.transient(self)  # Make login window transient to the main app
        login_window.grab_set()  # Modal- makes all other windows inaccessible

        tk.Label(login_window, text="Username:").pack(pady=10)
        username_entry = tk.Entry(login_window, width=30)
        username_entry.pack(pady=5)

        tk.Label(login_window, text="Password:").pack(pady=10)
        password_entry = tk.Entry(login_window, show="*", width=30)
        password_entry.pack(pady=5)

        login_successful = tk.BooleanVar(value=False)  # Boolean to keep track of login status

        def check_credentials():
            # Check if the credentials are correct
            if username_entry.get() == "abu_taha" and password_entry.get() == "m123456":
                login_successful.set(True)
                login_window.destroy()  # Close the login window on successful login
            else:
                messagebox.showerror("Login failed", "Incorrect username or password")

        # Login button
        login_button = tk.Button(login_window, text="Login", command=check_credentials)
        login_button.pack(pady=20)

        login_window.wait_window()  # Wait for the login window to close
        return login_successful.get()  # Return the status of the login attempt

    def create_widgets(self):
        tk.Label(self, text="URL:").pack()
        self.url_entry = tk.Entry(self, width=80)
        self.url_entry.pack()

        self.method_var = tk.StringVar(value="GET")
        methods = ["GET", "POST", "PUT", "DELETE"]
        for method in methods:
            tk.Radiobutton(self, text=method, value=method, variable=self.method_var).pack(anchor=tk.W)

        tk.Label(self, text="Data (for POST/PUT):").pack()
        self.data_text = tk.Text(self, height=5)
        self.data_text.pack()

        tk.Button(self, text="Send Request", command=self.send_request).pack()
        tk.Button(self, text="Save as HTML", command=self.save_response_as_html).pack()

        self.response_text = scrolledtext.ScrolledText(self, height=15)
        self.response_text.pack()

    def send_request(self):
        url = self.url_entry.get()
        method = self.method_var.get()
        data = self.data_text.get("1.0", "end-1c")
        headers = {'Content-Type': 'application/json'} if method in ['POST', 'PUT'] else {}

        auth = HTTPBasicAuth('abu_taha', 'm123456')

        try:
            response = self.session.request(method, url, data=data, headers=headers, auth=auth)
            self.display_response(response)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", str(e))

    def display_response(self, response):
        self.response_text.config(state=tk.NORMAL)
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, f"Status Code: {response.status_code}\n\n")
        self.response_text.insert(tk.END, f"Headers:\n{response.headers}\n\n")
        self.response_text.insert(tk.END, f"Body:\n{response.text}\n")
        self.response_text.config(state=tk.DISABLED)

    def save_response_as_html(self):
        response_data = self.response_text.get("1.0", tk.END)
        if response_data.strip():
            file_path = filedialog.asksaveasfilename(defaultextension=".html",
                                                     filetypes=[("HTML files", "*.html"), ("All files", "*.*")])
            if file_path:
                try:
                    with open(file_path, 'w') as file:
                        file.write(response_data)
                    messagebox.showinfo("Success", "The HTML file has been saved successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No data to save. Please perform a request first.")

if __name__ == "__main__":
    app = PyBrowser()
    app.mainloop()
