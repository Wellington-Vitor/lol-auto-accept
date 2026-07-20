class Bot:

    def __init__(self, window, status_label):
        self.running = False
        self.window = window
        self.status_label = status_label

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def update_status(self, text, color):

        self.window.after(
            0,
            lambda: self.status_label.config(
                text=text,
                fg=color
            )
        )