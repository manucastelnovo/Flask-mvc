from flask_sqlalchemy import SQLAlchemy
from service.database_service import db


class QR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_first=db.Column(db.Boolean,default=False)
    party_name=db.Column(db.String(50))
    qr_data=db.Column(db.String(300))
    is_used=db.Column(db.Boolean,default=False)
    timestamp=db.Column(db.Integer)