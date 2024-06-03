from project.settings import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    name = DATABASE.Column(DATABASE.String(60))
    price = DATABASE.Column(DATABASE.Integer)
    image = DATABASE.Column(DATABASE.String(50))
    count = DATABASE.Column(DATABASE.Integer)
    final_price = DATABASE.Column(DATABASE.Integer)


    def __repr__(self) -> str:
        return f'id - {self.id}, name - {self.name}'

