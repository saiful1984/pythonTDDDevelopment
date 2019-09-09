class Calculator:

    def add(self, provided_args):
        self.total = 0
        self.provided_args = provided_args
        for item in self.provided_args:
            if type(item) == int or type(item) == float:
                self.total = self.total + item
            else:
                raise TypeError("Invalid type of args provided")
        return self.total

    def subtract(self, provided_args):
        self.total = provided_args.pop(0)
        self.provided_args = provided_args
        for item in self.provided_args:
            if type(item) == int or type(item) == float:
                self.total = self.total - item
            else:
                raise TypeError("Invalid type of args provided")
        return self.total

    def multiply(self, provided_args):
        self.total = provided_args.pop(0)
        self.provided_args = provided_args
        for item in self.provided_args:
            if type(item) == int or type(item) == float:
                self.total = self.total * item
            else:
                raise TypeError("Invalid type of args provided. Expected int or float got [{}]".format(type(item)))
        return self.total

    def division(self, provided_args):
        self.total = provided_args.pop(0)
        self.provided_args = provided_args
        try:
            for item in self.provided_args:
                self.total = self.total / item
        except ZeroDivisionError:
            raise ZeroDivisionError("Illegal division by zero attempt")
        except TypeError:
            raise TypeError("Invalid type of args provided. Expected int or float got [{}]".format(type(item)))
        return self.total
