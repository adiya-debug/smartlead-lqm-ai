from flask import Flask, jsonify
from flask_cors import CORS
from config import config_dict
from app.database import init_db

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    CORS(app)

    with app.app_context():
        init_db(app)

    # Импортируем блюпринты здесь, чтобы не было циклического импорта:
    from app.routes import pages, api
    app.register_blueprint(pages)
    app.register_blueprint(api)

    @app.route('/health')
    def health():
        return jsonify({'durum': 'aktif', 'servis': 'SmartLead AI'}), 200

    return app