from flask import Flask
from app.routes.prediction import predict_bp
from app.routes.disease import disease_bp

def create_app():
    app = Flask(__name__)

    # Register blueprint
    app.register_blueprint(predict_bp)
    app.register_blueprint(disease_bp)

    # Home route
    @app.route('/')
    def index():
        return 'Padilux API is running.... Welcome to the Padilux API ;)'

    return app
