import requests
from config import Config 
# Özel hata sınıfı (Eğitmenin yönergedeki "AIServiceError fırlatın" kuralı için)[span_2](start_span)[span_2](end_span)
class AIServiceError(Exception):
    pass
class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.url = "llama3-8b-8192"

    def yanit_uret(self, mesaj, gecmis=None):
        # Yönerge kuralı: Anahtar yoksa çökmek yerine demo modu mesajı döndür[span_3](start_span)[span_3](end_span)
        if not self.api_key or self.api_key.startswith("gsk_buraya"):
            return "Merhaba! Ben LQM Kozmetik asistanı. Şu an size lokum yumuşaklığındaki parlatıcılarımızdan bahsetmek için sabırsızlanıyorum!"

        if gecmis is None:
            gecmis = []
        # Yönerge kuralı: Sistem talimatı (role: system), geçmiş mesajlar ve yeni mesaj sırası[span_4](start_span)[span_4](end_span)
        messages = [{"role": "system", "content": Config.BUSINESS_CONTEXT}]
        messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})

        headers = { "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"}
        
        # Yönerge kuralı: Groq API'sine model llama-3.1-8b-instant ile istek at[span_5](start_span)[span_5](end_span)
        payload = { "model": "openai/gpt-oss-120b",
            "messages": messages}
        # Yönerge kuralı: Hata yönetimi için try-except bloğu[span_6](start_span)[span_6](end_span)
        try:
            response = requests.post(self.url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            raise AIServiceError("Yapay zeka servisi hatası: {str(e)}")

# Yönerge kuralı: Dosya sonunda tek bir örnek oluştur[span_7](start_span)[span_7](end_span)
ai_service = AIService()