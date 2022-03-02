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
            

v1 = Vector([[0.0,1.0,2.0]])

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



