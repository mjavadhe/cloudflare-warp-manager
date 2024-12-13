import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import subprocess


class WarpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cloudflare WARP Manager")
        self.root.geometry("700x500")

        # Tabs
        self.notebook = ttk.Notebook(root)

        # Tab 1: VPN
        self.vpn_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.vpn_tab, text="VPN")

        # Tab 2: DNS
        self.dns_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.dns_tab, text="DNS")

        # Tab 3: About Me
        self.create_about_me_tab()

        # Tab 4: Help
        self.create_help_tab()

        self.notebook.pack(expand=1, fill="both")

        # VPN Tab
        self.status_label = ttk.Label(self.vpn_tab, text="Status: Disconnected", foreground="red", font=("Arial", 12))
        self.status_label.pack(pady=20)

        ttk.Button(self.vpn_tab, text="Connect", command=self.connect_warp).pack(pady=10)
        ttk.Button(self.vpn_tab, text="Disconnect", command=self.disconnect_warp).pack(pady=10)
        ttk.Button(self.vpn_tab, text="Check Status", command=self.check_status).pack(pady=10)

        # DNS Tab
        self.dns_label = ttk.Label(self.dns_tab, text="Set Cloudflare DNS:", font=("Arial", 12))
        self.dns_label.pack(pady=10)

        self.dns_entry = ttk.Entry(self.dns_tab, width=40)
        self.dns_entry.insert(0, "1.1.1.1, 1.0.0.1")  # Default Cloudflare DNS
        self.dns_entry.pack(pady=10)

        ttk.Button(self.dns_tab, text="Apply DNS", command=self.set_dns).pack(pady=10)

    def connect_warp(self):
        try:
            subprocess.run(["warp-cli", "connect"], check=True)
            messagebox.showinfo("Success", "Connected to WARP!")
            self.status_label.config(text="Status: Connected", foreground="green")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to connect to WARP.")

    def disconnect_warp(self):
        try:
            subprocess.run(["warp-cli", "disconnect"], check=True)
            messagebox.showinfo("Success", "Disconnected from WARP!")
            self.status_label.config(text="Status: Disconnected", foreground="red")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to disconnect from WARP.")

    def check_status(self):
        try:
            result = subprocess.run(["warp-cli", "status"], capture_output=True, text=True, check=True)
            if "Connected" in result.stdout:
                self.status_label.config(text="Status: Connected", foreground="green")
                messagebox.showinfo("WARP Status", result.stdout)
            else:
                self.status_label.config(text="Status: Disconnected", foreground="red")
                messagebox.showinfo("WARP Status", result.stdout)
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to check WARP status.")

    def set_dns(self):
        dns = self.dns_entry.get()
        if not dns:
            messagebox.showerror("Error", "Please enter a DNS address.")
            return
        try:
            subprocess.run(["warp-cli", "set-dns", dns], check=True)  # Replace with actual DNS setting command
            messagebox.showinfo("Success", f"DNS set to {dns}!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", f"Failed to set DNS to {dns}.")

    def create_about_me_tab(self):
        about_me_frame = ttk.Frame(self.notebook)
        self.notebook.add(about_me_frame, text="About Me")

        about_me_section = ttk.LabelFrame(about_me_frame, text="About Me", padding=(10, 10))
        about_me_section.pack(fill="x", padx=10, pady=10)

        about_me_label = ttk.Label(
            about_me_section,
text=( "Hello, I am Mohammad Javad Heydarpanah, a Python and Django programmer.\n" 
       "I hope you enjoy this program. In the tell me section, you can see ways to contact me.\n"
       "If you want to contact me, good luck and enjoy." ),
            wraplength=600,
            anchor="center"
        )
        about_me_label.pack(pady=5)

        
        tell_me_section = ttk.LabelFrame(about_me_frame, text="Tell Me", padding=(10, 10))
        tell_me_section.pack(fill="x", padx=10, pady=10)

        contacts = [
            {"name": "GitHub", "url": "https://github.com/mjavadhe"},
            {"name": "LinkedIn", "url": "https://linkedin.com/in/mohamadjavad-heydarpanah-13377223b/"},
            {"name": "Telegram", "url": "https://t.me/mjavad_he"},
            {"name": "Instagram", "url": "https://instagram.com/mjavad.he"},
        ]

        for contact in contacts:
            contact_label = ttk.Label(
                tell_me_section,
                text=contact["name"],
                foreground="blue",
                cursor="hand2"
            )
            contact_label.pack(anchor="w", padx=10, pady=5)

            # Bind with the correct URL
            contact_label.bind("<Button-1>", lambda e, url=contact["url"]: self.open_url(url))

    def open_url(self, url):
        try:
            subprocess.run(["xdg-open", url], check=True)
        except Exception as e:
            print(f"Error opening URL with xdg-open: {e}")


    def create_help_tab(self):
        help_frame = ttk.Frame(self.notebook)
        self.notebook.add(help_frame, text="Help")

        help_section = ttk.LabelFrame(help_frame, text="Help", padding=(10, 10))
        help_section.pack(fill="x", padx=10, pady=10)

        help_label = ttk.Label(
            help_section,
            text="This program is an open source software written in Python, so if you need to make changes to this program, you can clone the Cloudflare WARP Manager repository from my GitHub, apply the necessary changes, and run the program.",
            wraplength=600,
            anchor="center"
        )
        help_label.pack(pady=5)

        repository_section = ttk.LabelFrame(help_frame, text="Cloudflare WARP Manager repository", padding=(10, 10))
        repository_section.pack(fill="x", padx=10, pady=10)

        contacts = [
            {"name": "GitHub", "url": "https://github.com/mjavadhe/cloudflare-warp-manager"},
        ]

        for contact in contacts:
            contact_label = ttk.Label(
                repository_section,
                text=contact["name"],
                foreground="blue", 
                cursor="hand2" 
            )
            contact_label.pack(anchor="w", padx=10, pady=5)
            contact_label.bind("<Button-1>", lambda e, url=contact["url"]: self.open_url(url))

    def open_url(self, url):
        try:
            subprocess.run(["xdg-open", url], check=True)
        except Exception as e:
            print(f"Error opening URL with xdg-open: {e}")


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = WarpApp(root)
    root.mainloop()
