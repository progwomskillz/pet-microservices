class User():
    def __init__(self, id, email, password_hash, tokens_pairs, profile):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.tokens_pairs = tokens_pairs
        self.profile = profile

    def on_create(self, id):
        self.id = id
        self.profile.set_user_id(id)
