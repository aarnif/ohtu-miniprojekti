from app import app
from config import port

if __name__ == "__main__":
    app.run(port=port, host="0.0.0.0", debug=True)
