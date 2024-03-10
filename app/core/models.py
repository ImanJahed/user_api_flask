from app.extensions import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    roll = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name}, {self.email})"
