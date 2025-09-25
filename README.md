# 🌱 Projeto 2 – Coleta de Dados e Irrigação Inteligente

## 📌 Descrição
Este projeto da **FarmTech Solutions** simula um sistema de irrigação inteligente utilizando ESP32 na plataforma [Wokwi](https://wokwi.com).  
O sistema coleta dados de **NPK**, **pH do solo** (via LDR) e **umidade** (via DHT22), decidindo automaticamente quando ligar a irrigação.

---

## 🔧 Componentes no Wokwi
- ESP32 DevKit V1  
- 3 Botões (N, P, K)  
- LDR (pH)  
- DHT22 (umidade)  
- Relé (bomba d’água)

---

## ⚙️ Lógica de Decisão
- **Umidade < 60%**  
- **NPK presentes (botões pressionados)**  
- **pH entre 6 e 7 (ideal para soja)**  

➡️ Se todas as condições forem atendidas, a **bomba de irrigação (relé)** é ativada.

---

## 📂 Estrutura do Projeto
