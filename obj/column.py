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

    def __str__(self):
        is_null = "not null"
        if self.null:
            is_null = "null"

        params = [self.name, str(self.type), is_null]
        if self.key:
            params.append(self.key)
        if self.default:
            default = "default %s" % self.default
            params.append(default)
        if self.extra:
            params.append(self.extra)
        return " ".join(params)
