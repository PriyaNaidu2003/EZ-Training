import tkinter as tk
class Circle:
    def __init__(self,canvas,x,y,radius,color='grey'):
        self.radius=radius
        self.color=color
        self.x=x
        self.y=y
        self.canvas=canvas
    def draw(self):
        x0=self.x-self.radius
        x1=self.x+self.radius
        y0=self.y-self.radius
        y1=self.y+self.radius
        self.canvas.create_oval(x0,y0,x1,y1,fill=self.color)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('OOPS Circle Demo')
        self.geometry('400x400')
        self.canvas=tk.Canvas(self,bg='white',width=400,height=400)
        self.canvas.pack()
        self.circle=Circle(self.canvas,200,200,100)
        self.circle.draw()

if __name__=='__main__':
    app=Application()
    app.mainloop()
