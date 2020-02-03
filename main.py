from flask import Flask

from config import db_config
from config.db_exts import db
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(db_config)
db.init_app(app)

# with app.app_context():
#     db.create_all()

CORS(app,
     resources={r"/*": {"origins": "*"}},
     supports_credentials=True,
     # methods=["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"]
     methods=["GET", "POST"],
     )

from controller import index_controller
from controller.blog import user_controller

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
