from models.DbEntity import DbEntity


class Tournament(DbEntity):
    def __init__(self, name: str=None, description: str=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
