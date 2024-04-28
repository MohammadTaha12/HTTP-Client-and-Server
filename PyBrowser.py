import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import urllib.request
import urllib.error
def send_get_request():
    url = url_entry.get() 
    try:
        with urllib.request.urlopen(url) as response:
            global response_data  
            response_data = response.read().decode('utf-8')
            headers = response.headers
        response_text.config(state=tk.NORMAL)
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, f"Status Code: {response.status}\n")
        response_text.insert(tk.END, f"Headers: {headers}\n")
        response_text.insert(tk.END, f"Content: {response_data}\n")
        response_text.config(state=tk.DISABLED)
    except urllib.error.URLError as e:
        response_text.config(state=tk.NORMAL)
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, f"Error: {e}\n")
        response_text.config(state=tk.DISABLED)
def save_to_html():
    if response_data:
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
        messagebox.showwarning("Warning", "No data to save. Please perform a GET request first.")
root = tk.Tk()
root.title("PyBrowser")
root.geometry("600x400")
response_data = ""
url_entry = tk.Entry(root, width=80)
url_entry.pack(pady=10)
get_button = tk.Button(root, text="GET Request", command=send_get_request)
get_button.pack(pady=10)
save_button = tk.Button(root, text="Save as HTML", command=save_to_html)
save_button.pack(pady=10)
response_text = scrolledtext.ScrolledText(root, width=70, height=10, state=tk.DISABLED)
response_text.pack(pady=10)
root.mainloop()
