import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import subprocess
import os
from tkinter.font import Font
import sv_ttk  # Modern theme package

class AutoEditorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoCut Pro")
        self.root.geometry("700x600")
        
        # Set modern theme (sun-valley)
        sv_ttk.set_theme("dark")  # Try "light" or "dark"
        
        # Custom styling
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#1c1c1c")
        self.style.configure("TLabel", background="#1c1c1c", foreground="#ffffff")
        self.style.configure("TCheckbutton", background="#1c1c1c", foreground="#ffffff")
        self.style.configure("TEntry", fieldbackground="#1c1c1c", foreground="#ffffff")
        self.style.map("TEntry", fieldbackground=[("readonly", "#1c1c1c")])
        
        # Main container with modern padding
        self.main_frame = ttk.Frame(root, padding=(20, 15))
        self.main_frame.pack(fill="both", expand=True)
        
        # Header
        self.header = ttk.Frame(self.main_frame)
        self.header.pack(fill="x", pady=(0, 15))
        ttk.Label(self.header, text="AutoCut Pro", font=("Segoe UI", 16, "bold")).pack(side="left")
        
        # Settings frame with card-like appearance
        self.settings_card = ttk.LabelFrame(self.main_frame, text="Editing Settings", padding=15)
        self.settings_card.pack(fill="x", pady=(0, 15))
        
        # Margin input with modern styling
        self.margin_frame = ttk.Frame(self.settings_card)
        self.margin_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(self.margin_frame, text="Silence Margin:").pack(side="left", padx=(0, 10))
        self.margin_entry = ttk.Entry(self.margin_frame, width=8)
        self.margin_entry.pack(side="left")
        self.margin_entry.insert(0, "0.2")
        ttk.Label(self.margin_frame, text="seconds").pack(side="left", padx=(5, 0))
        
        # Export options with modern toggle appearance
        self.export_frame = ttk.Frame(self.settings_card)
        self.export_frame.pack(fill="x")
        
        ttk.Label(self.export_frame, text="Export Mode:").pack(side="left", padx=(0, 10))
        
        self.export_var = tk.StringVar(value="direct")
        
        self.direct_btn = ttk.Radiobutton(
            self.export_frame,
            text="Direct Video",
            variable=self.export_var,
            value="direct",
            style="Toolbutton"
        )
        self.direct_btn.pack(side="left", padx=(0, 5))
        
        self.premiere_btn = ttk.Radiobutton(
            self.export_frame,
            text="Premiere Pro",
            variable=self.export_var,
            value="premiere",
            style="Toolbutton"
        )
        self.premiere_btn.pack(side="left")
        
        # File selection with modern card
        self.file_card = ttk.LabelFrame(self.main_frame, text="Media Files", padding=15)
        self.file_card.pack(fill="both", expand=True, pady=(0, 15))
        
        # Scrollable text area with modern styling
        self.file_display = scrolledtext.ScrolledText(
            self.file_card,
            wrap=tk.WORD,
            width=70,
            height=12,
            font=Font(size=10),
            bg="#3e3e3e",
            fg="#ffffff",
            insertbackground="#ffffff",
            relief="flat",
            bd=0
        )
        self.file_display.pack(fill="both", expand=True)
        
        # Button group with modern spacing
        self.button_group = ttk.Frame(self.file_card)
        self.button_group.pack(fill="x", pady=(10, 0))
        
        self.add_btn = ttk.Button(
            self.button_group,
            text="Add Files",
            style="Accent.TButton",
            command=self.add_files
        )
        self.add_btn.pack(side="left", padx=(0, 5))
        
        self.add_folder_btn = ttk.Button(
            self.button_group,
            text="Add Folder",
            command=self.add_folder
        )
        self.add_folder_btn.pack(side="left", padx=(0, 5))
        
        self.clear_btn = ttk.Button(
            self.button_group,
            text="Clear All",
            command=self.clear_files
        )
        self.clear_btn.pack(side="right")
        
        # Status bar with modern appearance
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Frame(self.main_frame, height=25)
        self.status_bar.pack(fill="x", pady=(5, 0))
        ttk.Label(
            self.status_bar,
            textvariable=self.status_var,
            anchor="w",
            style="TLabel"
        ).pack(side="left", padx=10)
        
        # Run button with accent color
        self.run_btn = ttk.Button(
            self.main_frame,
            text="PROCESS MEDIA",
            style="Accent.TButton",
            command=self.run_auto_editor
        )
        self.run_btn.pack(pady=(10, 0), anchor="e")
        
        # Initialize
        self.file_paths = []
        self._update_file_display()
        self.root.minsize(650, 550)
    
    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select media files",
            filetypes=[
                ("Media files", "*.mp4 *.wav"),
                ("MP4 files", "*.mp4"),
                ("WAV files", "*.wav")
            ]
        )
        self._process_new_files(files)
    
    def add_folder(self):
        folder = filedialog.askdirectory(title="Select folder containing media files")
        if folder:
            files = []
            for root, _, filenames in os.walk(folder):
                for filename in filenames:
                    if filename.lower().endswith(('.mp4', '.wav')):
                        files.append(os.path.join(root, filename))
            self._process_new_files(files)
    
    def _process_new_files(self, files):
        new_files = [f for f in files if f.lower().endswith(('.mp4', '.wav')) and f not in self.file_paths]
        self.file_paths.extend(new_files)
        self._update_file_display()
        self.status_var.set(f"{len(self.file_paths)} file(s) selected" if new_files else "No new valid files found")
    
    def _update_file_display(self):
        self.file_display.config(state=tk.NORMAL)
        self.file_display.delete(1.0, tk.END)
        
        if not self.file_paths:
            self.file_display.insert(tk.END, "No media files selected")
            self.file_display.tag_add("center", "1.0", "end")
            self.file_display.tag_config("center", justify="center", foreground="#777777")
        else:
            for i, path in enumerate(self.file_paths, 1):
                self.file_display.insert(tk.END, f"{i}. {os.path.basename(path)}\n", "bold")
                self.file_display.insert(tk.END, f"   {path}\n\n")
        
        self.file_display.tag_config("bold", font=("Segoe UI", 10, "bold"))
        self.file_display.config(state=tk.DISABLED)
    
    def clear_files(self):
        self.file_paths = []
        self._update_file_display()
        self.status_var.set("Ready")
    
    def run_auto_editor(self):
        if not self.file_paths:
            messagebox.showerror("Error", "Please select at least one media file")
            return
            
        try:
            margin = float(self.margin_entry.get())
            if margin <= 0:
                raise ValueError("Margin must be positive")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for margin")
            return
        
        base_cmd = f'python -m auto_editor --margin {margin}sec'
        
        if self.export_var.get() == "premiere":
            base_cmd += " --export premiere"
        
        self.status_var.set("Processing...")
        self.root.update_idletasks()
        
        success = 0
        for file_path in self.file_paths:
            try:
                subprocess.Popen(f'start cmd /k "{base_cmd} "{file_path}""', shell=True)
                success += 1
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process {os.path.basename(file_path)}:\n{str(e)}")
        
        self.status_var.set(f"Processing started for {success} file(s)")
        if success > 0:
            messagebox.showinfo(
                "Processing Started", 
                f"Auto-Editor is processing {success} file(s) in separate command windows.\n"
                "Please wait for each process to complete."
            )

if __name__ == "__main__":
    root = tk.Tk()
    
    # Windows 10/11 style controls
    if os.name == 'nt':
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    
    app = AutoEditorGUI(root)
    root.mainloop()