import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.ad import Ad, GeneratedAd
from src.models.template import WinningTemplate, AdVariation
from src.routes.user import user_bp
from src.routes.ads import ads_bp
from src.routes.automatic_ads import automatic_ads_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'src', 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
CORS(app)
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(ads_bp, url_prefix='/api')
app.register_blueprint(automatic_ads_bp, url_prefix='/api/automatic')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'src', 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

