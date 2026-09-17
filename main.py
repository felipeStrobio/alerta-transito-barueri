Python
import os
import requests

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def analisar_transito():
    print("Executando simulação de trânsito para teste...")
    
    alertas_gerados = [
        "⚠️ *Rodovia Castello Branco*\nTrânsito Severo! Velocidade caiu para 12 km/h (SIMULAÇÃO)."
    ]
    
    if alertas_gerados:
        print("Problema detectado na simulação! Enviando Telegram...")
        texto_final = "🚨 *ALERTA DA CENTRAL DE MOBILIDADE* 🚨\n\nLentidões críticas detectadas:\n\n" + "\n\n".join(alertas_gerados)
        
        url_telegram = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        pacote_de_dados = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": texto_final,
            "parse_mode": "Markdown"
        }
        
        resposta = requests.post(url_telegram, json=pacote_de_dados)
        print("Resposta do Telegram:", resposta.text)
        print("Telegram enviado com sucesso para a equipe!")
    else:
        print("Trânsito fluindo normalmente.")

if __name__ == "__main__":
    analisar_transito()
