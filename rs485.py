import minimalmodbus
import json
import time
import requests

PORT = 'COM10'
SLAVE_ID = 1
BAUDRATE = 9600

instrument = minimalmodbus.Instrument(PORT, SLAVE_ID)
instrument.serial.baudrate = BAUDRATE
instrument.mode = minimalmodbus.MODE_RTU

URL = "https://rotariaweb.net/joaquin/api.php"

def leer_y_enviar():
    try:
        voltage1 = instrument.read_register(37, 1)
        voltage2 = instrument.read_register(38, 1)
        voltage3 = instrument.read_register(39, 1)
        current1 = instrument.read_register(40, 2)
        current2 = instrument.read_register(41, 2)
        current3 = instrument.read_register(42, 2)
        power1   = instrument.read_register(48,0)
        power2  = instrument.read_register(49, 0)
        power3 = instrument.read_register(50, 0)
        
        data = {
            "voltaje_1": round(voltage1, 2),
            "voltaje_2": round(voltage2, 2),
            "voltaje_3": round(voltage3, 2),
            "corriente_1": round(current1, 2),
            "corriente_2": round(current2, 2),
            "corriente_3": round(current3, 2),
            "potencia_1": round(power1, 2)*10,
            "potencia_2": round(power2, 2)*10,
            "potencia_3": round(power3, 2)*10,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print("📤 Enviando:", json.dumps(data))
        
        response = requests.post(
            URL, 
            data=json.dumps(data), 
            headers={'Content-Type': 'application/json'}, 
            timeout=5
        )
        
        print("✅ Status:", response.status_code)
        print("📥 Respuesta:", response.text)

    except Exception as e:
        print("❌ Error:", e)

print("🚀 Iniciando envío de datos desde Modbus...")
print("Presiona Ctrl+C para detener\n")

while True:
    leer_y_enviar()
    time.sleep(1)