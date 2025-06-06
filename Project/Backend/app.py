from flask import Flask
from routes.sample_routes import sample_bp

app = Flask(__name__)
app.register_blueprint(sample_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "Flask API is running"}

if __name__ == "__main__":
    app.run(debug=True)

