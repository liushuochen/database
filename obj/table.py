from obj.base import _Database


class Table(_Database):
    def __init__(self,
                 name: str,
                 database: str,
                 columns: list,
                 storage="InnoDB",
                 charset="utf8"
                 ):
        super().__init__(name)
        self.columns = columns
        self.storage = storage
        self.charset = charset
        self.database = database
