class Vector:
    def __init__(self, *coords):
        for i in coords:
            try:
                float(i)
            except TypeError:
                raise TypeError(f"{i} is not a number")

        self.__coords = coords

    @property
    def coords(self):
        return self.__coords

    def __str__(self):
        return f"{type(self).__name__}({', '.join([str(i) for i in self.coords])})"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        try:
            end = min(len(self), len(other))
            return type(self)(*[self[i] + other[i] for i in range(end)] + list(self[end:]) + list(other[end:]))
        except TypeError:
            try:
                return type(self)(*[i + other for i in self])
            except TypeError:
                raise TypeError(f"{other} is not a number, vector or one-dimensional array")
    
    def __sub__(self, other):
        try:
            end = min(len(self), len(other))
            return type(self)(*[self[i] - other[i] for i in range(end)] + list(self[end:]) + list(other[end:]))
        except TypeError:
            try:
                return type(self)(*[i - other for i in self])
            except TypeError:
                raise TypeError(f"{other} is not a number, vector or one-dimensional array")

    def __mul__(self, other):
        try:
            return type(self)(*[i * other for i in self])
        except TypeError:
            raise TypeError(f"{other} is not a number")

    def __truediv__(self, other):
        try:
            return type(self)(*[i / other for i in self])
        except TypeError:
            raise TypeError(f"{other} is not a number")

    def __floordiv__(self, other):
        try:
            return type(self)(*[i // other for i in self])
        except TypeError:
            raise TypeError(f"{other} is not a number")

    def __mod__(self, other):
        try:
            return type(self)(*[i % other for i in self])
        except TypeError:
            raise TypeError(f"{other} is not a number")

    def __pow__(self, other):
        try:
            return abs(self)**other
        except TypeError:
            raise TypeError(f"{other} is not a number")

    def __pos__(self):
        return type(self)(*self.coords)

    def __neg__(self):
        return type(self)(*[-i for i in self])

    def __abs__(self):
        return sum([i**2 for i in self.coords])**0.5

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other

    def __rmul__(self, other):
        return self * other

    def __rshift__(self, other):
        if other < 0:
            raise ValueError("negative shift count")
        if other == 0:
            return self
        return type(self)(*([0]*other + list(self[:-other])))

    def __lshift__(self, other):
        if other < 0:
            raise ValueError("negative shift count")
        return type(self)(*(list(self[other:]) + [0]*other))

    def __len__(self):
        return len(self.coords)

    def __eq__(self, other):
        try:
            if len(self) != len(other):
                return False
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
        except TypeError:
            return False
        return True

    def __ne__(self, other):
        return not self == other

    def __getitem__(self, slc):
        if type(slc) is tuple:
            return [self[i] for i in slc]
        elif type(slc) is slice:
            return type(self)(*self.coords[slc])
        elif type(slc) is int:
            return self.coords[slc]
        else:
            raise TypeError(f"{type(self)} indices must be integer, slices or tuples, not {type(slc)}")
