import tkinter as tk
import time
import os

STATE_FILE = 'chrono_state.txt'

class Chrono(tk.Tk):
    def __init__(self):
        super().__init__()
        # récupérer l'état précédent si disponible
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, 'r') as f:
                    self.elapsed = float(f.read().strip())
            except:
                self.elapsed = 0.0
        else:
            self.elapsed = 0.0

        self.start_time = None
        self.running = False

        # fenêtre épurée
        self.overrideredirect(True)
        self.configure(bg='black')

        self.label = tk.Label(
            self,
            text=self._format_time(self.elapsed),
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg="black"
        )
        self.label.pack(padx=8, pady=4)

        # clic gauche => start/stop
        self.bind("<Button-1>", self.toggle)
        # molette (clic milieu) => reset
        self.bind("<Button-2>", self.reset)
        # clic droit => save & close
        self.bind("<Button-3>", self.close)

        self._update_clock()

    def _format_time(self, sec):
        h, rem = divmod(sec, 3600)
        m, s   = divmod(rem, 60)
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d}"

    def toggle(self, event=None):
        if not self.running:
            # démarrer ou reprendre
            self.start_time = time.time() - self.elapsed
            self.running = True
        else:
            # pause
            self.elapsed = time.time() - self.start_time
            self.running = False

    def reset(self, event=None):
        # remettre à zéro et supprimer le fichier d'état
        self.running = False
        self.start_time = None
        self.elapsed = 0.0
        if os.path.exists(STATE_FILE):
            os.remove(STATE_FILE)
        self.label.config(text=self._format_time(0.0))

    def close(self, event=None):
        # sauvegarder l'état puis fermer
        if self.running:
            self.elapsed = time.time() - self.start_time
        with open(STATE_FILE, 'w') as f:
            f.write(str(self.elapsed))
        self.destroy()

    def _update_clock(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.label.config(text=self._format_time(self.elapsed))
        self.after(100, self._update_clock)

if __name__ == "__main__":
    Chrono().mainloop()
