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

# Health check endpoint (opsional tapi bagus untuk debugging)
@app.route('/health')
def health():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    # Untuk development
    app.run(debug=True)
else:
    # Untuk production (Railway)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
