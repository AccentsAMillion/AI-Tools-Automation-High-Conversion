from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ad_copy = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.Text)  # JSON string of keywords
    platform = db.Column(db.String(50), nullable=False)  # e.g., 'Facebook', 'Google'
    competitor_name = db.Column(db.String(100))
    estimated_spend = db.Column(db.Float)
    performance_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_competitor_ad = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'ad_copy': self.ad_copy,
            'keywords': self.keywords,
            'platform': self.platform,
            'competitor_name': self.competitor_name,
            'estimated_spend': self.estimated_spend,
            'performance_score': self.performance_score,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_competitor_ad': self.is_competitor_ad
        }

class GeneratedAd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_description = db.Column(db.Text, nullable=False)
    generated_copy = db.Column(db.Text, nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    predicted_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_description': self.product_description,
            'generated_copy': self.generated_copy,
            'platform': self.platform,
            'predicted_score': self.predicted_score,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

