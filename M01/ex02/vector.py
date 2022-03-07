class Vector:
    def __init__(self, args):
        conv = []
        if type(args) is int:
            for i in range(args):
                conv.append([float(i)])
            args = conv
        if type(args) is tuple:
            rang = range(args[0], args[1])
            for i in rang:
                conv.append([float(i)])
            args = conv
        column = 0
        row = 0
        self.values = []
        if any(isinstance(i, list) for i in args):
            for line in args:
                row += 1
                for i in line:
                    column += 1
        else:
            row = 1
            for i in args:
                column += 1

        column = column/row
        if column.is_integer():
            for line in args:
                self.values.append(line)
        else:
            print("input vector error:", args)
            quit(0)
        self.shape = (row, int(column))

    def T(self):
        ret = []
        if any(isinstance(i, list) for i in self.values):
            for line in self.values:
                ret.append(line[0])
        else:
            for i in self.values:
                ret.append([i])
        return(Vector(ret))

    def dot(self, vec2):
        ret = 0
        if self.shape == vec2.shape:
            if any(isinstance(i, list) for i in self.values):
                for x, w in zip(self.values, vec2.values):
                    for i, j in zip(x, w):
                        ret += i * j
            else:
                for i, j in zip(self.values, vec2.values):
                    ret += i*j
            return ret
        else:
            print("not same shape")

    def __add__(self, vec2):
        ret = []
        if self.shape == vec2.shape:
            if any(isinstance(i, list) for i in self.values):
                for i, j in zip(self.values, vec2.values):
                    ret.append([i[0] + j[0]])
            else:
                for i, j in zip(self.values, vec2.values):
                    ret.append(i + j)
            return(Vector(ret))
        else:
            print("not same shape")
            return(Vector(0))

    def __sub__(self, vec2):
        ret = []
        if self.shape == vec2.shape:
            if any(isinstance(i, list) for i in self.values):
                for i, j in zip(self.values, vec2.values):
                    ret.append([i[0] - j[0]])
            else:
                for i, j in zip(self.values, vec2.values):
                    ret.append(i - j)
            return(Vector(ret))
        else:
            print("not same shape")
            return(Vector(0))

    def __radd__(self, vec2):
        return(vec2.__add__(self))

    def __rsub__(self, vec2):
        return(vec2.__sub__(self))

    def __truediv__(self, scal):
        ret = []
        if type(scal) is int or type(scal) is float:
            if any(isinstance(i, list) for i in self.values):
                for i in self.values:
                    ret.append([i[0] / scal])
            else:
                for i in self.values:
                    ret.append(i / scal)
            return(Vector(ret))
        else:
            print("not a scalar")
            return(Vector(0))

    def __rtruediv__(self, scal):
        self.__truediv__(scal)

    def __mul__(self, scal):
        ret = []
        if type(scal) is int or type(scal) is float:
            if any(isinstance(i, list) for i in self.values):
                for i in self.values:
                    ret.append([i[0] * scal])
            else:
                for i in self.values:
                    ret.append(i * scal)
            return(Vector(ret))
        else:
            print("not a scalar")
            return(Vector(0))

    def __rmul__(self, scal):
        return(self.__mul__(scal))

    def __str__(self):
        return f'shape = {self.shape} \nvalues = {self.values}'

    def __repr__(self):
        return (
            f'{self.__class__.__name__}' +
            f'(shape={self.shape}, values={self.values})')
