import requests

# URL exacta de tu endpoint de reportes
url = "https://veci-alerta-api-1.onrender.com/api/reportes"

# Datos de prueba que quieres guardar (asegúrate de que el id_usuario, id_categoria y id_estado existan en tu base de datos)
nuevo_reporte = {
    "id_usuario": 1,
    "id_categoria": 1,
    "id_estado": 1,
    "titulo": "Bache en la calle",
    "descripcion": "Hay un bache grande frente a la casa.",
    "ubicacion": "Calle Principal #123"
}

# Mandamos la petición POST para guardar el dato
respuesta = requests.post(url, json=nuevo_reporte)

print("Código de estado:", respuesta.status_code)
print("Respuesta de la API:", respuesta.json())