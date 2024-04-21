from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    height = db.Column(db.Integer)
    lifespan = db.Column(db.Integer)
    classification = db.Column(db.String(80))
    designation = db.Column(db.String(80))
    eye_color = db.Column(db.String(80))
    hair_color = db.Column(db.String(80))
    language = db.Column(db.String(80))
    skin_color = db.Column(db.String(80))

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "lifespan": self.lifespan,
            "classification": self.classification,
            "designation": self.designation,
            "eye color": self.eye_color,
            "hair color": self.hair_color,
            "language": self.language,
            "skin color": self.skin_color
            # do not serialize the password, its a security breach
        } 

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(80))
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    population = db.Column(db.Integer)
    rotational_period = db.Column(db.Integer)
    surface_water = db.Column(db.Integer)
    terrain = db.Column(db.String(80))


    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.name,
            "Climate": self.climate,
            "Diameter": self.diameter,
            "Gravity": self.gravity,
            "Orbital period": self.orbital_period,
            "Population": self.population,
            "Rotational period": self.rotational_period,
            "Surface water": self.surface_water,
            "Terrain": self.terrain
            # do not serialize the password, its a security breach
        }  

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(80))
    cost_in_credits = db.Column(db.Integer)
    crew = db.Column(db.String(80))
    lenght = db.Column(db.Integer)
    manufacturer = db.Column(db.String(80))
    max_speed = db.Column(db.Integer)
    model = db.Column(db.String(80))
    passengers = db.Column(db.String(80))
    vehicle_class = db.Column(db.String(80))


    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.name,
            "Cargo capacity": self.cargo_capacity,
            "Consumables": self.consumables,
            "Cost in credits": self.cost_in_credits,
            "Crew": self.crew,
            "Lenght": self.lenght,
            "Manufacturer": self.manufacturer,
            "Max speed": self.max_speed,
            "Model": self.model,
            "Passengers": self.passengers,
            "Vehicle class": self.vehicle_class

            # do not serialize the password, its a security breach
        }  

class FavoritesCharacters(db.Model):
    __tablename__ = 'favorites_characters'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return '<FavoritesCharacters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,

            # do not serialize the password, its a security breach
        } 

class FavoritesPlanets(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return '<FavoritesPlanets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,

            # do not serialize the password, its a security breach
        } 

class FavoritesVehicles(db.Model):
    __tablename__ = 'favorites_vehicles'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return '<FavoritesVehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,

            # do not serialize the password, its a security breach
        }      
