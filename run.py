# run.py
from waitress import serve
from app import app

try:
    import waitress
except ImportError:
    print("Waitress package is not installed. Please install it using 'pip install waitress'.")
    exit(1)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=1808)