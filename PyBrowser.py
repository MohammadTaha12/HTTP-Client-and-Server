import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox, simpledialog
import urllib.request
import http.cookiejar
import base64
import json

class PyBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyBrowser")
        self.geometry("600x400")
        self.cookie_jar = http.cookiejar.CookieJar()  # Initialize the cookie jar
        self.create_widgets()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie_jar))

    def create_widgets(self):
        self.url_entry = tk.Entry(self, width=80)
        self.url_entry.pack(pady=10)

        self.get_button = tk.Button(self, text="GET Request", command=lambda: self.send_request('GET'))
        self.get_button.pack(side=tk.LEFT, padx=5)

        self.post_button = tk.Button(self, text="POST Request", command=lambda: self.send_request('POST'))
        self.post_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self, text="Save as HTML", command=self.save_to_html)
        self.save_button.pack(pady=10)

        self.response_text = scrolledtext.ScrolledText(self, width=70, height=10, state=tk.DISABLED)
        self.response_text.pack(pady=10)

    def send_request(self, method='GET'):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "URL is required")
            return

        headers = {'User-Agent': 'PyBrowser/1.0'}
        data = None

        if method == 'POST':
            content = simpledialog.askstring("Input", "Enter JSON data for POST request:")
            if content:
                try:
                    data = json.dumps(json.loads(content)).encode('utf-8')
                    headers['Content-Type'] = 'application/json'
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "Invalid JSON data.")
                    return

        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with self.opener.open(req) as response:
                response_data = response.read().decode('utf-8')
                self.display_response(response, response_data)
        except urllib.error.URLError as e:
            messagebox.showerror("Error", f"Network error: {e}")

    def display_response(self, response, response_data):
        self.response_text.config(state=tk.NORMAL)
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, f"Status Code: {response.status}\n")
        self.response_text.insert(tk.END, f"Headers: {response.headers}\n")
        self.response_text.insert(tk.END, f"Content: {response_data}\n")
        self.response_text.config(state=tk.DISABLED)

    def save_to_html(self):
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

def login():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Username:").pack(pady=10)
    username_entry = tk.Entry(login_window, width=30)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", width=30)
    password_entry.pack(pady=5)

    def check_credentials():
        username = username_entry.get()
        password = password_entry.get()
        if username == "mohammad@loay.com" and password == "lm123456":
            login_window.destroy()
            app = PyBrowser()
            app.mainloop()
        else:
            messagebox.showerror("Login failed", "Incorrect username or password")
            login_window.lift()

    tk.Button(login_window, text="Login", command=check_credentials).pack(pady=20)

    login_window.mainloop()

if __name__ == "__main__":
    login()
