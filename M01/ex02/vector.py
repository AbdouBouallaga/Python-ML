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

    #    def __rtruediv__() ? scalar
    
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



v1 = Vector([2.0,5.0,6.0])
v1s = Vector([1.0,2.0,4.0])
v1n = Vector([2.0,5.0])

print("print v1 values\n", v1.values)
print("print v1 shape\n", v1.shape)
print()
v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
print("print v2 values\n", v2.values)
print("print v2 shape\n", v2.shape)
print("")
v3 = Vector((10,15))
print("print v3 values\n", v3.values)
print("print v3 shape\n", v3.shape)
print("")
v4 = Vector(3)
print("print v4 values\n", v4.values)
print("print v4 shape\n", v4.shape)
v4t = v4.T()
print("print transpose v4\n", v4t.values)
v4tb = v4t.T()
print("print transpose back v4\n", v4tb.values)
print("dot product of v2 and v2, same shape:", v2.dot(v2))
print()
print("dot product of v4t and v2 not same shape:", v4t.dot(v2))
print()
vplus = Vector(1)
vplus = v1 + v1n
print("not nested: v1 + v1n =", vplus.values)

vplus = v1 + v1
vn = Vector([[2.0], [5.0], [6.0]])
print("here is v1 and vn\nv1",v1.values, "\nvn", vn.values)
print()
print("not nested: v1 + v1 =", vplus.values)
print()
vplus = vn.__radd__(vn)
print("nested: vn + vn =", vplus.values)
print()
vsub = v1.__rsub__(v1s)
print("non nested: v1 - v1s =", vsub.values)
print()
vdiv = v1 / 2
print("div: v1 / 2 =", vdiv.values)
print()
vmul = v1 * 2
print("multi: v1 * 2 =", vmul.values)
