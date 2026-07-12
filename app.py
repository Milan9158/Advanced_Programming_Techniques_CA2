from flask import Flask
from config import Config
from models import db
from routes.issue_routes import issue_bp
from routes.vulnerability_routes import vulnerability_bp

app = Flask(__name__)
#to load the application configuration
app.config.from_object(Config)

#to connect SQLALchemy to the Flask application
db.init_app(app)
app.register_blueprint(issue_bp)
app.register_blueprint(vulnerability_bp)

#Home route
@app.route("/")
def home():
    return{
        "application": "Issue and Vulnerability Tracking System",
        "company": "Milan Solutions",
        "status": "API Running"
    }

#to create the database if it doesnot alreday exist
with app.app_context():
    db.create_all()

# to run application
if __name__ == "__main__":
    app.run(debug=True)
