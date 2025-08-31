from datetime import datetime
from sqlalchemy import func
from app import db

class ContactSubmission(db.Model):
    """Model for storing contact form submissions"""
    __tablename__ = 'contact_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    service_type = db.Column(db.String(50), nullable=True)
    message = db.Column(db.Text, nullable=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Status tracking
    status = db.Column(db.String(20), default='new', nullable=False)  # new, contacted, completed
    notes = db.Column(db.Text, nullable=True)  # Internal notes for follow-up
    
    def __repr__(self):
        return f'<ContactSubmission {self.name} - {self.email}>'
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'service_type': self.service_type,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
            'status': self.status,
            'notes': self.notes
        }

class ServiceInquiry(db.Model):
    """Model for tracking different types of service inquiries"""
    __tablename__ = 'service_inquiries'
    
    id = db.Column(db.Integer, primary_key=True)
    contact_submission_id = db.Column(db.Integer, db.ForeignKey('contact_submissions.id'), nullable=False)
    service_category = db.Column(db.String(50), nullable=False)  # medicao, georreferenciamento, legalizacao, completo
    estimated_area = db.Column(db.Float, nullable=True)  # Area in hectares
    property_type = db.Column(db.String(20), nullable=True)  # rural, urbano
    location = db.Column(db.String(200), nullable=True)
    urgency = db.Column(db.String(20), default='normal', nullable=False)  # baixa, normal, alta
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationship
    contact_submission = db.relationship('ContactSubmission', backref=db.backref('service_inquiries', lazy=True))
    
    def __repr__(self):
        return f'<ServiceInquiry {self.service_category} - {self.contact_submission.name}>'