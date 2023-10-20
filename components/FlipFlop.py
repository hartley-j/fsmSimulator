import itertools
from random import randint

class FlipFlop:
    id_iter = itertools.count()

    def __init__(self, _s, _r):
        self.inputs = {"Set": _s, "Reset": _r}
        # Determined best initial output should be None value
        # Probably not the best implementation, but will work for now
        self.output = bool(randint(0, 1))
        self.id = next(self.id_iter)

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
        FlipFlop.__init__(self, _s=_d, _r=not _d)

    def set_inputs(self, *args, **kwargs):
        super(DFlipFlop, self).set_inputs(_s=not kwargs["_d"], _r=kwargs["_d"])
