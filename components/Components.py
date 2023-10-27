import itertools
from random import randint


class Component:
    id_iter = itertools.count()

    def __init__(self):
        self.inputs = None
        self.output = None
        self.id = next(self.id_iter)


class Not(Component):

    def __init__(self, _input):
        super().__init__()
        self.inputs = _input
        self.output = not self.inputs

    def get_output(self):
        return self.output

    def update(self, _input):
        self.inputs = bool(_input)
        self.output = not self.inputs


class NAND(Component):

    def __init__(self, *args):
        super().__init__()
        self.inputs = [args[x] for x in range(len(args) - 1)]
        self.output = not (all(self.inputs))

    def get_output(self):
        return self.output

    def update(self, *args):
        self.inputs = [args[x] for x in range(len(args) - 1)]
        self.output = not (all(self.inputs))


class FlipFlop(Component):

    def __init__(self, _s, _r):
        super().__init__()
        self.inputs = {"Set": bool(_s), "Reset": bool(_r)}
        # Determined best initial output should be None value
        # Probably not the best implementation, but will work for now
        self.output = bool(randint(0, 1))

    def get_output(self):
        return self.output

    def set_inputs(self, *args, **kwargs):
        self.inputs = {"Set": kwargs['_s'], "Reset": kwargs['_r']}

    def update(self):
        if self.inputs["Set"] and self.inputs["Reset"]:
            self.output = self.output
        elif self.inputs["Set"] and not (self.inputs["Reset"]):
            self.output = False
        elif not (self.inputs["Set"]) and self.inputs["Reset"]:
            self.output = True
        elif not (self.inputs["Set"]) and not (self.inputs["Reset"]):
            raise ValueError(f"Set and Reset are both zero for flip flop ID:{self.id}")


class DFlipFlop(FlipFlop):

    def __init__(self, _d):
        FlipFlop.__init__(self, not _d, _r=_d)

    def set_inputs(self, *args, **kwargs):
        super(DFlipFlop, self).set_inputs(_s=not kwargs["_d"], _r=kwargs["_d"])
