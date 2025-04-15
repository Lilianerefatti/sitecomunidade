import os
from comunidade import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # usa 5000 localmente e PORT no Railway
    app.run(debug=True, host='0.0.0.0', port=port)
