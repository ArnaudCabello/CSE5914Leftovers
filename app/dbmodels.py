from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates, relationship
from sqlalchemy.exc import IntegrityError
from sqlalchemy import UniqueConstraint
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    #username = db.Column(db.String(64), unique=True, nullable=False)
    favorites = relationship('FavoriteRecipes', backref='user', lazy=True)

    def set_hashed_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Invalid email format"
        return email
    


class FavoriteRecipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, nullable=False)
    recipe_name = db.Column(db.String(200))
    __table_args__ = (
        UniqueConstraint('user_id', 'recipe_id', name='unique_user_recipe'),
    )

    # Add recipe to favorites for a user
    @staticmethod
    def add_favorite(user, recipe_id, recipe_name):
        try:
            new_favorite = FavoriteRecipes(user_id=user.id, recipe_id=recipe_id, recipe_name=recipe_name)
            db.session.add(new_favorite)
            db.session.commit()
            return True  # Success
        except IntegrityError:
            db.session.rollback()
            return False  # Recipe already favorited

    # Remove recipe from favorites for a user
    @staticmethod
    def remove_favorite(user, recipe_id):
        favorite = FavoriteRecipes.query.filter_by(user_id=user.id, recipe_id=recipe_id).first()
        if favorite:
            db.session.delete(favorite)
            db.session.commit()
            return True  # Success
        else:
            return False  # Recipe not found in favorites

def get_favorited_recipes(user_id):
    # Query the database to get favorited recipes for the user
    user = User.query.get(user_id)
    if user:
        favorited_recipes = user.favorites
        return favorited_recipes
    else:
        return None  # User not found
    
def check_if_favorited(current_user, recipe_id):
    if not current_user.is_authenticated:
        return False
    # Check if the recipe is favorited by the current user
    favorited_recipe = FavoriteRecipes.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
    
    if favorited_recipe:
        return True
    else:
        return False