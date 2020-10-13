import util


class FieldBase(object):
    def __init__(self):
        self.uuid = util.uuid_string(upper=True)


class IntegerNumber(FieldBase):
    def __init__(self, length, unsigned=False, zerofill=False):
        super().__init__()
        self.length = length
        self.unsigned = unsigned
        self.zerofill = zerofill

        if zerofill and (not self.unsigned):
            self.unsigned = True


class Tinyint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 4
        if self.length < self.default_length:
            self.length = self.default_length


class Smallint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 6
        if self.length < self.default_length:
            self.length = self.default_length


class Mediumint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 9
        if self.length < self.default_length:
            self.length = self.default_length


class Int(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 11
        if self.length < self.default_length:
            self.length = self.default_length


class Bigint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 20
        if self.length < self.default_length:
            self.length = self.default_length


class Bool(FieldBase):
    pass


class FloatNumber(FieldBase):
    def __init__(self, m, n=0):
        super().__init__()
        self.m = m
        self.n = n

        if self.m < 0:
            self.m = 0
        if self.n < 0:
            self.n = 0


class Float(FloatNumber):
    pass

