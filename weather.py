import requests

# Substitua pela sua chave de API do OpenWeather
API_KEY = "SUA_CHAVE_AQUI"
CITY = "São Paulo,BR"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def previsao_chuva():
    response = requests.get(URL)
    data = response.json()

    if "weather" in data:
        descricao = data["weather"][0]["description"]
        chuva = "rain" in descricao.lower()
        print(f"Condição atual em {CITY}: {descricao}")
        print("Vai chover?" , "Sim" if chuva else "Não")
        return chuva
    else:
        print("Erro ao acessar API:", data)
        return False

if __name__ == "__main__":
    chuva = previsao_chuva()

    # No ESP32, você pode simular inserindo esse valor
    # Exemplo: no sketch.ino, crie uma variável bool previsaoChuva = false;
    # e altere manualmente para true/false conforme saída daqui.
