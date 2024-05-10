# Usamos la imagen base de Python
FROM python:3.8-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos el contenido del directorio actual al directorio /app en el contenedor
COPY . /app/

# Instalamos las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 8080 para que sea accesible desde fuera del contenedor
EXPOSE 8080

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
