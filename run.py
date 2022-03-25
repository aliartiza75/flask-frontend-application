import os
import sys
from app import create_app

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), 'instance'))

config_name = "development"
app = create_app(config_name)


if __name__ == '__main__':
    app.run(debug=True)
