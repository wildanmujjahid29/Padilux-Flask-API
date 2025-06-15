from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Untuk development
    app.run(debug=True)
else:
    # Untuk production (Railway)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)