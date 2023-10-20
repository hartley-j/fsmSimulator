class NAND:

    def __init__(self, *args):
        self.inputs = [bool(args[x]) for x in range(len(args) - 1)]
        self.output = not (all(self.inputs))

    def get_output(self):
        return self.output

    def update(self, *args):
        self.inputs = [bool(args[x]) for x in range(len(args) - 1)]
        self.output = not (all(self.inputs))
