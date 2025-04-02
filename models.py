
from app import db
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates


class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    def to_dict(self, depth=1):
        """ Custom method to limit recursion depth. """
        data = {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name
        }
        if depth > 0:
            data['hero_powers'] = [hero_power.to_dict(depth=depth-1) for hero_power in self.hero_powers]
        return data


class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value.strip()) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value

    def to_dict(self, depth=1):
        """ Custom method to limit recursion depth. """
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
        if depth > 0:
            data['hero_powers'] = [hero_power.to_dict(depth=depth-1) for hero_power in self.hero_powers]
        return data


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
   
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id', ondelete='CASCADE'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    table_args = (
        CheckConstraint("strength IN ('Strong', 'Weak', 'Average')", name="check_strength"),
    )

    def to_dict(self, depth=1):
        """ Custom method to limit recursion depth. """
        data = {
            'id': self.id,
            'strength': self.strength,
            'hero_id': self.hero_id,
            'power_id': self.power_id
        }
        if depth > 0:
            data['hero'] = self.hero.to_dict(depth=depth-1)
            data['power'] = self.power.to_dict(depth=depth-1)
        return data
