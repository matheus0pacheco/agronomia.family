# Papa-Léguas - Land Surveying and Legalization Website

## Overview

Papa-Léguas is a professional land surveying and legalization services website built with Flask. The application serves as a company portfolio and contact platform for agricultural engineers specializing in land measurement, georeferencing, and property legalization services in Brazil.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5.3.0 for responsive design
- **Icons**: Font Awesome 6.4.0 for consistent iconography
- **JavaScript**: Vanilla JavaScript for client-side interactions
- **Language**: Portuguese (pt-BR) - Brazilian market focus

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Server**: Development server with debug mode enabled
- **Session Management**: Flask sessions with configurable secret key
- **Error Handling**: Custom 404 and 500 error pages
- **Logging**: Python logging module for debugging and monitoring

### Structure Pattern
- **Single Page Application**: Primary content served through one main route
- **Form Processing**: POST endpoint for contact form submissions
- **Static Content**: CSS, JavaScript, and images served through Flask static files

## Key Components

### Core Application (app.py)
- **Main Routes**: Home page and contact form processing
- **Form Validation**: Basic server-side validation for required fields
- **Flash Messages**: User feedback system for form submissions
- **Error Handlers**: Graceful handling of 404 and 500 errors
- **Security**: Environment-based secret key configuration

### Frontend Components
- **Responsive Design**: Mobile-first approach with Bootstrap grid system
- **Navigation**: Sticky navbar with smooth scrolling
- **Hero Section**: Prominent company branding and call-to-action
- **Services Showcase**: Cards layout for service offerings
- **Contact Integration**: Form for customer inquiries
- **Professional Presentation**: Clean, business-focused design

### JavaScript Functionality
- **Smooth Scrolling**: Enhanced navigation experience
- **Form Validation**: Client-side validation before submission
- **Mobile Menu**: Responsive navigation for mobile devices
- **User Experience**: Interactive elements and animations

## Data Flow

### Contact Form Process
1. User fills contact form on homepage
2. Form data submitted via POST to `/contact` endpoint
3. Server validates required fields (name, email, message)
4. Valid submissions logged to application logs
5. User receives flash message confirmation
6. Redirect back to homepage with success/error message

### Static Content Delivery
1. CSS, JavaScript, and images served through Flask static file handler
2. Templates rendered with Jinja2 engine
3. Bootstrap and Font Awesome loaded from CDN for performance

## External Dependencies

### Frontend Libraries
- **Bootstrap 5.3.0**: UI framework loaded via CDN
- **Font Awesome 6.4.0**: Icon library loaded via CDN
- **No database dependencies**: Currently stores no persistent data

### Python Dependencies
- **Flask**: Web application framework
- **Standard Library**: logging, os modules for basic functionality

### Infrastructure
- **Static Assets**: Images and documents stored in static directory
- **Templates**: HTML templates in templates directory
- **Environment Variables**: SESSION_SECRET for production security

## Deployment Strategy

### Development Setup
- **Debug Mode**: Enabled for development with auto-reload
- **Host Configuration**: Configured for 0.0.0.0 to allow external connections
- **Port**: Default port 5000
- **Entry Point**: main.py imports and runs the Flask application

### Production Considerations
- **Secret Key**: Should be set via SESSION_SECRET environment variable
- **Debug Mode**: Must be disabled in production
- **Logging**: Currently logs to console, should be configured for file/external logging
- **Static Files**: Should be served by web server (nginx/Apache) in production
- **HTTPS**: SSL/TLS should be configured for secure form submissions

### Missing Production Features
- **Database Integration**: No persistent storage for contact submissions
- **Email Integration**: Contact forms only logged, not sent via email
- **Analytics**: No tracking or monitoring integration
- **Content Management**: Static content requires code deployment for updates

The application follows a simple, maintainable architecture suitable for a small business website with room for future enhancements like database integration and email notifications.