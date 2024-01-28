import tkinter as tk

class PaintApp(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("PyBoard Paint")
        self.geometry("700x600")

        self.canvas = tk.Canvas(self, bg="white", width=500, height=500)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Shift-B1-Motion>", self.erase)
        self.canvas.bind("<ButtonRelease-1>", self.reset_pos)

        self.color = "blue"
        self.erase_color = "white"
        
        self.brush_size = 10
        self.x_pos, self.y_pos = None, None
        
    def paint(self, event):
        self.line_width = self.brush_size
        self.line_color = self.color
        self.draw(event)

    def erase(self, event):
        self.line_width = self.brush_size * 3
        self.line_color = self.erase_color
        self.draw(event)

    def draw(self, event):
        if self.x_pos and self.y_pos:
            event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y,  
                                     width=self.line_width, fill=self.line_color,
                                     capstyle=tk.ROUND, smooth=True)
                                     
        self.x_pos = event.x
        self.y_pos = event.y
        
    def reset_pos(self, event):
        self.x_pos, self.y_pos = None, None

if __name__ == "__main__":
    app = PaintApp()
    app.mainloop()