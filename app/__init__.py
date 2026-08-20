from flask import Flask, jsonify
from config import Config

# Fabrika fonksiyonu: Tüm parçaları birleştirir
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # CORS aç (Farklı sitelerden gelen isteklere izin ver)
    @app.after_request
    def cors_ayarlari(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        return response

    # /health uç noktası (Sunucu canlılık kontrolü)
    @app.route('/health')
    def health():
        return jsonify({'durum': 'aktif', 'mesaj': 'LQM Backend calisiyor'})

    # Blueprint'leri (rotaları) kaydet
    from .routes import pages, api
    app.register_blueprint(pages)
    app.register_blueprint(api)

    return app