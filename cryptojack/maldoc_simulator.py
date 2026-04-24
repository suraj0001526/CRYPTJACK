import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

class CryptojackSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Range: Cryptojacking & Endpoint Forensics")
        self.root.geometry("1000x650")
        self.root.configure(bg="#1a1a2e")

        # System State Variables
        self.is_infected = False
        self.miner_active = False
        self.cpu_usage = 12
        self.mining_pool_ip = "198.51.100.77" # Standard mock IP
        self.malicious_pid = "4092"
        
        # Simulated Windows Registry
        self.mock_registry = {
            "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run": {
                "OneDrive": '"C:\\Users\\Admin\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe" /background',
                "Discord": '"C:\\Users\\Admin\\AppData\\Local\\Discord\\Update.exe" --processStart Discord.exe'
            }
        }

        self.setup_ui()
        self.hardware_monitor_loop()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TNotebook", background="#1a1a2e", borderwidth=0)
        style.configure("TNotebook.Tab", background="#16213e", foreground="white", padding=[15, 5], font=('Arial', 11, 'bold'))
        style.map("TNotebook.Tab", background=[("selected", "#0f3460")])

        header = tk.Label(self.root, text="Cryptojacking Lifecycle: Infection to Forensics", font=("Arial", 16, "bold"), bg="#1a1a2e", fg="#e94560")
        header.pack(pady=10)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.tab1_attack = tk.Frame(self.notebook, bg="#16213e")
        self.tab2_soc = tk.Frame(self.notebook, bg="#16213e")
        self.tab3_dfir = tk.Frame(self.notebook, bg="#16213e")

        self.notebook.add(self.tab1_attack, text="Phase 1: Red Team (Infection)")
        self.notebook.add(self.tab2_soc, text="Phase 2: Blue Team (Endpoint EDR)")
        self.notebook.add(self.tab3_dfir, text="Phase 3: DFIR (Persistence Sandbox)")

        self.build_attack_tab()
        self.build_soc_tab()
        self.build_dfir_tab()

    # ==========================================
    # TAB 1: ATTACK PANEL (Red Team)
    # ==========================================
    def build_attack_tab(self):
        tk.Label(self.tab1_attack, text="Employee Software Download Simulation", font=("Arial", 14, "bold"), bg="#16213e", fg="white").pack(pady=20)

        download_frame = tk.Frame(self.tab1_attack, bg="#0f3460", bd=2, relief="groove")
        download_frame.pack(pady=10, padx=50, fill=tk.X)

        tk.Label(download_frame, text="Download: Adobe_Premiere_Pro_CRACKED_v2026.exe", bg="#0f3460", fg="white", font=("Arial", 12, "bold")).pack(pady=15)
        
        self.btn_download = tk.Button(download_frame, text="⬇️ Download & Install Free Software", bg="#e94560", fg="white", font=("Arial", 12, "bold"), command=self.execute_malware)
        self.btn_download.pack(pady=15)

        self.attack_status = tk.Label(self.tab1_attack, text="Status: System normal. Waiting for user action...", bg="#16213e", fg="gray", font=("Arial", 11))
        self.attack_status.pack(pady=20)

    def execute_malware(self):
        if not self.is_infected:
            self.is_infected = True
            self.miner_active = True
            self.btn_download.config(state="disabled", bg="gray")
            self.attack_status.config(text="Status: Miner Deployed. Persistence established in Registry. Mining started.", fg="#e94560")
            
            # Attacker establishes persistence quietly
            self.mock_registry["HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"]["WindowsUpdateSvc"] = '"C:\\Users\\Admin\\AppData\\Roaming\\winupd.exe" --pool 198.51.100.77:3333 --cpu 99'

    # ==========================================
    # TAB 2: SOC EDR DASHBOARD (Blue Team)
    # ==========================================
    def build_soc_tab(self):
        tk.Label(self.tab2_soc, text="EDR Endpoint Resource Monitor", font=("Arial", 14, "bold"), bg="#16213e", fg="#4cabe4").pack(pady=10)

        # Hardware Monitor UI
        hw_frame = tk.Frame(self.tab2_soc, bg="#16213e")
        hw_frame.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(hw_frame, text="CPU Usage:", bg="#16213e", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        self.cpu_bar = ttk.Progressbar(hw_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.cpu_bar.pack(side=tk.LEFT, padx=10)
        self.cpu_label = tk.Label(hw_frame, text="12%", bg="#16213e", fg="white", font=("Arial", 12, "bold"))
        self.cpu_label.pack(side=tk.LEFT, padx=10)

        # Process Table
        columns = ("PID", "Process Name", "CPU %", "Network State")
        self.process_tree = ttk.Treeview(self.tab2_soc, columns=columns, show="headings", height=5)
        for col in columns:
            self.process_tree.heading(col, text=col)
            self.process_tree.column(col, width=150, anchor="center")
        self.process_tree.pack(fill=tk.X, padx=20, pady=15)

        # EDR Console
        tk.Label(self.tab2_soc, text="Automated EDR Console:", bg="#16213e", fg="white").pack(pady=5, anchor="w", padx=20)
        self.edr_console = tk.Text(self.tab2_soc, height=8, bg="black", fg="#00ff00", font=("Consolas", 10))
        self.edr_console.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        self.edr_console.tag_config('alert', foreground='red')

        self.log_edr_event("EDR Agent Active. Monitoring process heuristics.")
        self.update_process_list()

    def hardware_monitor_loop(self):
        # Simulate normal CPU fluctuations vs. Miner usage
        if self.miner_active:
            self.cpu_usage = random.randint(95, 100)
            self.cpu_label.config(fg="red")
            self.check_edr_rules()
        else:
            self.cpu_usage = random.randint(5, 15)
            self.cpu_label.config(fg="white")

        self.cpu_bar['value'] = self.cpu_usage
        self.cpu_label.config(text=f"{self.cpu_usage}%")
        self.update_process_list()

        self.root.after(1500, self.hardware_monitor_loop)

    def update_process_list(self):
        for row in self.process_tree.get_children():
            self.process_tree.delete(row)
            
        # Normal processes
        normal_cpu = max(1, self.cpu_usage - 95) if self.miner_active else self.cpu_usage
        self.process_tree.insert("", tk.END, values=("1024", "explorer.exe", f"{normal_cpu}%", "Local"))
        self.process_tree.insert("", tk.END, values=("2248", "chrome.exe", "2%", "ESTABLISHED"))

        # Malicious process
        if self.miner_active:
            self.process_tree.insert("", tk.END, values=(self.malicious_pid, "winupd.exe", "98%", f"SYN_SENT -> {self.mining_pool_ip}"))

    def check_edr_rules(self):
        # EDR Rule: High CPU + External unknown connection
        if self.miner_active and self.cpu_usage > 95:
            self.log_edr_event(f"CRITICAL: Process 'winupd.exe' (PID {self.malicious_pid}) utilizing 98% CPU.", "alert")
            self.log_edr_event(f"ALERT: Unauthorized connection to cryptomining pool {self.mining_pool_ip}.", "alert")
            self.log_edr_event(f"ACTION: Suspending process {self.malicious_pid} to prevent hardware exhaustion.", "alert")
            self.miner_active = False # Suspend the miner

    def log_edr_event(self, message, tag=None):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.edr_console.insert(tk.END, f"[{timestamp}] {message}\n", tag)
        self.edr_console.see(tk.END)

    # ==========================================
    # TAB 3: DFIR SANDBOX (Forensics)
    # ==========================================
    def build_dfir_tab(self):
        tk.Label(self.tab3_dfir, text="Endpoint Registry & Persistence Forensics", font=("Arial", 14, "bold"), bg="#16213e", fg="#f0a500").pack(pady=10)

        control_frame = tk.Frame(self.tab3_dfir, bg="#16213e")
        control_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Button(control_frame, text="1. Scan Autorun / Registry Keys", width=30, command=self.scan_registry).pack(side=tk.LEFT, padx=10)

        tk.Label(self.tab3_dfir, text="Forensic Registry Dump:", bg="#16213e", fg="white").pack(pady=5, anchor="w", padx=20)
        self.dfir_console = tk.Text(self.tab3_dfir, height=15, bg="#0a0a0a", fg="#00ff00", font=("Consolas", 10))
        self.dfir_console.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        self.dfir_console.tag_config('malicious', foreground='red')

    def scan_registry(self):
        self.dfir_console.delete(1.0, tk.END)
        self.dfir_console.insert(tk.END, "[*] Initializing Hive Scan...\n")
        self.dfir_console.insert(tk.END, "[*] Scanning HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run...\n\n")
        
        run_keys = self.mock_registry["HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"]
        
        for name, value in run_keys.items():
            if "winupd.exe" in value:
                self.dfir_console.insert(tk.END, f"[!] SUSPICIOUS KEY FOUND: {name}\n", "malicious")
                self.dfir_console.insert(tk.END, f"    Value: {value}\n", "malicious")
                self.dfir_console.insert(tk.END, "    Analysis: 'winupd.exe' is a known masquerade name. The --pool argument confirms Cryptojacking persistence.\n\n", "malicious")
            else:
                self.dfir_console.insert(tk.END, f"[+] Clean Key: {name}\n")
                self.dfir_console.insert(tk.END, f"    Value: {value}\n\n")

        if self.is_infected:
            self.dfir_console.insert(tk.END, "[*] RECOMMENDATION: Delete malicious registry key and quarantine 'winupd.exe' from AppData\\Roaming.")
        else:
            self.dfir_console.insert(tk.END, "[*] No persistent threats found in Run keys.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptojackSimulator(root)
    root.mainloop()