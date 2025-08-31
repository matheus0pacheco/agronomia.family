import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///papaleguas.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize the app with the extension
db.init_app(app)

# Create database tables
with app.app_context():
    # Import models to register them with SQLAlchemy
    import models
    db.create_all()

# Import models for use in routes
from models import ContactSubmission

@app.route("/")
def home():
    """Homepage displaying company information and services"""
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """Handle contact form submissions"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        message = request.form.get('message', '').strip()
        service_type = request.form.get('service_type', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            return redirect(url_for('home'))
        
        # Save to database
        try:
            submission = ContactSubmission(
                name=name,
                email=email,
                phone=phone,
                service_type=service_type,
                message=message
            )
            db.session.add(submission)
            db.session.commit()
            
            app.logger.info(f"Contact form submission saved to database: {name} ({email})")
            flash('Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.', 'success')
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error saving contact submission: {e}")
            flash('Erro ao enviar mensagem. Tente novamente ou entre em contato por telefone.', 'error')
        
        return redirect(url_for('home'))
    
    return redirect(url_for('home'))

@app.route("/admin/submissions")
def admin_submissions():
    """Admin route to view contact submissions"""
    submissions = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).all()
    return render_template("admin_submissions.html", submissions=submissions)

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
