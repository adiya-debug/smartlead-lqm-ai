from app import create_app
from app.database import init_db

# Fabrikadan uygulamayı al
app = create_app()

# Veritabanını uygulama bağlamında (app context) başlat
with app.app_context():
    init_db(app)

# Sunucuyu çalıştır
if __name__ == '__main__':
    app.run(debug=True)