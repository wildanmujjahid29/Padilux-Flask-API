from flask import Flask, render_template
from routes.prediction import predict_bp
from routes.disease import disease_bp

app = Flask(__name__, template_folder='templates')

# Register blueprint
app.register_blueprint(predict_bp)
app.register_blueprint(disease_bp)

# Home route
@app.route('/')
def index():
    return render_template('index.html')
