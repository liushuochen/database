from obj.base import _Database


class Table(_Database):
    def __init__(self,
                 name: str,
                 columns: list,
                 storage="InnoDB",
                 charset="utf8"
                 ):
        super().__init__(name)
        self.columns = columns
        self.storage = storage
        self.charset = charset

    def create(self):
        commands = [
            "create table if not exists %s(\n" % self.name,
        ]

        for column in self.columns:
            commands.append(str(column) + ",\n")
        commands[-1].strip(",\n")
        commands.append(") %s" % self.charset)
        return "".join(commands)
