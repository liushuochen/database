import util


class Field(object):
    def __init__(self):
        self.TINYINT = Tinyint
        self.SMALLINT = Smallint
        self.MEDIUMINT = Mediumint
        self.INT = Int
        self.BIGINT = Bigint
        self.BOOL = Bool
        self.FLOAT = Float
        self.DOUBLE = Double
        self.DECIMAL = Decimal
        self.CHAR = Char
        self.VARCHAR = Varchar
        self.DATETIME = Datetime
        self.DATE = Date
        self.TIMESTAMP = Timestamp
        self.TIME = Time
        self.YEAR = Year
        self.TINYTEXT = Tinytext
        self.TEXT = Text
        self.MEDIUMTEXT = Mediumtext
        self.LONGTEXT = Longtext
        self.BLOB = Blob
        self.ENUM = Enum
        self.SET = Set


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


class Tinyint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 4
        if self.length < self.default_length:
            self.length = self.default_length

    def __str__(self):
        if self.zerofill:
            return "tinyint(%s) zerofill" % self.length
        elif self.unsigned:
            return "tinyint(%s) unsigned" % self.length
        else:
            return "tinyint(%s)" % self.length


class Smallint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 6
        if self.length < self.default_length:
            self.length = self.default_length

    def __str__(self):
        if self.zerofill:
            return "smallint(%s) zerofill" % self.length
        elif self.unsigned:
            return "smallint(%s) unsigned" % self.length
        else:
            return "smallint(%s)" % self.length


class Mediumint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 9
        if self.length < self.default_length:
            self.length = self.default_length

    def __str__(self):
        if self.zerofill:
            return "mediumint(%s) zerofill" % self.length
        elif self.unsigned:
            return "mediumint(%s) unsigned" % self.length
        else:
            return "mediumint(%s)" % self.length


class Int(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 11
        if self.length < self.default_length:
            self.length = self.default_length

    def __str__(self):
        if self.zerofill:
            return "int(%s) zerofill" % self.length
        elif self.unsigned:
            return "int(%s) unsigned" % self.length
        else:
            return "int(%s)" % self.length


class Bigint(IntegerNumber):
    def __init__(self, length=0):
        super().__init__(length)
        self.default_length = 20
        if self.length < self.default_length:
            self.length = self.default_length

    def __str__(self):
        if self.zerofill:
            return "bigint(%s) zerofill" % self.length
        elif self.unsigned:
            return "bigint(%s) unsigned" % self.length
        else:
            return "bigint(%s)" % self.length


class Bool(FieldBase):
    def __str__(self):
        return "bool"


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
    def __init__(self, length=23):
        super().__init__(length)

    def __str__(self):
        return "char(%s)" % self.length


class Varchar(String):
    def __init__(self, length=255):
        super().__init__(length)

    def __str__(self):
        return "varchar(%s)" % self.length


class Datetime(FieldBase):
    def __str__(self):
        return "datetime"


class Date(FieldBase):
    def __str__(self):
        return "date"


class Timestamp(FieldBase):
    def __str__(self):
        return "timestamp"


class Time(FieldBase):
    def __str__(self):
        return "time"


class Year(FieldBase):
    def __str__(self):
        return "year"


class Tinytext(FieldBase):
    def __str__(self):
        return "tinytext"


class Text(FieldBase):
    def __str__(self):
        return "text"


class Mediumtext(FieldBase):
    def __str__(self):
        return "mediumtext"


class Longtext(FieldBase):
    def __str__(self):
        return "longtext"


class Blob(FieldBase):
    def __str__(self):
        return "blob"


class Enum(FieldBase):
    def __init__(self, data_list):
        super().__init__()
        if len(data_list) <= 0:
            raise TypeError("SQL syntax error for enum: Empty data list.")
        if len(data_list) > 10:
            data_list = data_list[:10]
        if len(set(data_list)) != len(data_list):
            raise TypeError("Duplicate element for enum list.")
        self.data_list = data_list

    def __str__(self):
        data = ",".join(
            ["\'" + element + "\'" for element in self.data_list]
        )
        return "enum(%s)" % data


class Set(FieldBase):
    def __init__(self, data_list):
        super().__init__()
        if len(data_list) <= 0:
            raise TypeError("SQL syntax error for set: Empty data list.")
        if len(data_list) > 10:
            data_list = data_list[:10]
        if len(set(data_list)) != len(data_list):
            raise TypeError("Duplicate element for set list.")
        self.data_list = data_list

    def __str__(self):
        data = ",".join(
            ["\'" + element + "\'" for element in self.data_list]
        )
        return "set(%s)" % data
