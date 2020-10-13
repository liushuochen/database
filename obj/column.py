from obj.base import _Database


class Column(_Database):
    def __init__(self,
                 name,
                 filed_type,
                 null=False,
                 key=None,
                 default=None,
                 extra=None
                 ):
        super().__init__(name)
        self.type = filed_type
        self.null = null
        self.key = key
        self.default = default
        self.extra = extra
