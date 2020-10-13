import util


class FieldBase(object):
    def __init__(self):
        self.uuid = util.uuid_string(upper=True)
        self.smallint = util.uuid_string(upper=True),
        self.mediumint = util.uuid_string(upper=True),
        self.int = util.uuid_string(upper=True)
        self.bigint = util.uuid_string(upper=True),
        self.smallint_unsigned = util.uuid_string(upper=True),
        self.mediumint_unsigned = util.uuid_string(upper=True),
        self.int_unsigned = util.uuid_string(upper=True),
        self.bigint_unsigned = util.uuid_string(upper=True),
        self.smallint_zerofill = util.uuid_string(upper=True),
        self.mediumint_zerofill = util.uuid_string(upper=True),
        self.int_zerofill = util.uuid_string(upper=True)
        self.bigint_zerofill = util.uuid_string(upper=True)
        self.bool = util.uuid_string(upper=True)


class Tinyint(FieldBase):
    def __init__(self, length=4, unsigned=False, zerofill=False):
        super().__init__()
        self.length = length
        self.unsigned = unsigned
        self.zerofill = zerofill

        if zerofill and (not self.unsigned):
            self.unsigned = True
        if self.length <= 0:
            self.length = 4
