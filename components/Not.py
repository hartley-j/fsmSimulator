class Not:

    def __init__(self, _input):
        self.input = bool(_input)
        self.output = not self.input

    def get_output(self):
        return self.output

    def update(self, _input):
        self.input = bool(_input)
        self.output = not self.input
