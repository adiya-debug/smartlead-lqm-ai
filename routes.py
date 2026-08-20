from flask import Blueprint, request, jsonify, render_template
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

pages = Blueprint('pages', __name__)
api = Blueprint('api', __name__, url_prefix='/api')

# --- SAYFALAR (GET) ---
@pages.route('/')
def index():
    # Karşılama sayfasını (Ana sayfa) gösterir
    return render_template('index.html')

@pages.route('/dashboard')
def dashboard():
    # Yönetim panelini gösterir
    return render_template('dashboard.html')

# --- API UÇ NOKTALARI (Veri alışverişi) ---
@api.route('/sohbet', methods=['POST'])
def sohbet():
    veri = request.json
    if not veri or 'mesaj' not in veri:
        # Eksik veri gelirse 400 hatası
        return jsonify({'basari': False, 'hata': 'Mesaj gerekli'}), 400
    
    try:
        # AI çağrısını try-except ile sarıyoruz
        cevap = ai_service.yanit_uret(veri['mesaj'], veri.get('gecmis'))
        return jsonify({'basari': True, 'cevap': cevap})
    except AIServiceError as e:
        # Hata olursa 503 ve kibar bir mesaj
        return jsonify({'basari': False, 'hata': 'Asistanimiz şu an çok yoğun, lütfen birazdan tekrar deneyin.'}), 503

@api.route('/leads', methods=['POST'])
def lead_ekle():
    veri = request.json
    if not veri or 'isim' not in veri or 'telefon' not in veri:
        # Eksik veri gelirse 400
        return jsonify({'basari': False, 'hata': 'İsim ve telefon gerekli'}), 400
    
    # Yeni kayıt (Lead) oluşturma
    yeni_id = lead_ekle (veri['isim'], veri['telefon'], veri.get('mesaj', ''))
    # Başarılı kayıtta 201 durum kodu
    return jsonify({'basari': True, 'mesaj': 'Kayit başariyla alindi'}), 201

@api.route('/leads', methods=['GET'])
def leadleri_getir():
    # Veritabanından tüm lead'leri çekme
    leads = tum_leadler()
    return jsonify({'basari': True, 'leads': leads})