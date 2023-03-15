class Profile():
    def __init__(self, id, user_id, first_name, last_name):
        self.id = id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def on_create(self, id):
        self.id = id

    def set_user_id(self, user_id):
        self.user_id = user_id
