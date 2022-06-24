class Calculator:
    def __init__(self):
        self.angles_measure = "degrees"  # degrees, radians

    def execute(self, string):
        return eval(string)
