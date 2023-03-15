class TokensPair():
    def __init__(self, id, access, refresh):
        self.id = id
        self.access = access
        self.refresh = refresh

    def on_create(self, id):
        self.id = id
