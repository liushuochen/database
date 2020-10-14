import util


class FieldBase(object):
    def __init__(self):
        self.uuid = util.uuid_string(upper=True)

    def __str__(self):
        raise TypeError("Invalid base function called.")


class IntegerNumber(FieldBase):
    def __init__(self, length, unsigned=False, zerofill=False):
        super().__init__()
        self.length = length
        self.unsigned = unsigned
        self.zerofill = zerofill

        if zerofill and (not self.unsigned):
            self.unsigned = True

    def __str__(self):
        raise TypeError("Invalid base function called.")


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

        if self.n < 0:
            self.n = 0
        if m < n:
            self.m = n

    def __str__(self):
        raise TypeError("Invalid base function called.")


class Float(FloatNumber):
    pass


class Double(FloatNumber):
    pass


class Decimal(FloatNumber):
    def __init__(self, m=10, n=0):
        super().__init__(m, n)


class String(FieldBase):
    def __init__(self, length):
        super().__init__()
        self.length = length

        if self.length < 1:
            self.length = 1
        if self.length > 255:
            self.length = 255

    def __str__(self):
        raise TypeError("Invalid base function called.")


class Char(String):
    pass


class Varchar(String):
    pass


class Datetime(FieldBase):
    def __init__(self, date):
        super().__init__()
        self.year = date.year
        self.month = date.month
        self.day = date.day
        self.hour = date.hour
        self.minute = date.minute
        self.second = date.second

    def __str__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)\
            + " " + str(self.hour) + ":" + str(self.minute) + ":" + \
            str(self.second)
