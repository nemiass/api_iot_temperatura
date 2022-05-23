from app import create_app
from app.config import config

if __name__ == "__main__":
    app = create_app(config["devConfig"])
    app.run(host="0.0.0.0", port="3000", debug=True)
