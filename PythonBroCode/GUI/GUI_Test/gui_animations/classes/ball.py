class ball:

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.object = self.canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.object)

        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0:
            self.xVelocity = -self.xVelocity
        elif coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.yVelocity = -self.xVelocity

        self.canvas.move(self.object, self.xVelocity, self.yVelocity)