from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_hashed_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Invalid email format"
        return email