from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


properties = db.Table('properties',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True),
    db.Column('property_id', db.Integer, db.ForeignKey('property.id'), primary_key=True)
)


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    properties = db.relationship(
        'Property', secondary=properties, lazy='subquery', backref=db.backref('groups, lazy=True')
    )


class Property(db.Model):
    __tablename__ = 'property'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=True)
    value = db.Column(db.String(50), nullable=True)

