from flask import Flask, render_template
from routes.prediction import predict_bp
from routes.disease import disease_bp
import os

app = Flask(__name__, template_folder='templates')

# Register blueprint
app.register_blueprint(predict_bp)
app.register_blueprint(disease_bp)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False untuk production
