from flask import Flask, render_template, request, send_file
import pandas as pd
import io
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # Obtener los archivos subidos
        zoho_file = request.files['zoho_file']
        sunnova_file = request.files['sunnova_file']

        # Leer los datos desde los archivos CSV
        zoho_df = pd.read_csv(zoho_file)
        sunnova_df = pd.read_csv(sunnova_file)

        # Eliminar 'zcrm_' de los valores en la columna 'Record Id' en zoho_df
        zoho_df['Record Id'] = zoho_df['Record Id'].str.replace('zcrm_', '')

        # Realizar el emparejamiento de datos y generar el informe combinado
        merged_df = pd.merge(zoho_df, sunnova_df, left_on='Sunnova Project ID', right_on='Sunnova Project ID', how='left')

        # Crear un objeto de BytesIO para escribir el archivo CSV
        output = io.BytesIO()
        merged_df.to_csv(output, index=False)
        output.seek(0)

        # Devolver el archivo CSV como una respuesta HTTP
        return send_file(output, as_attachment=True, download_name='informe_combinado.csv')
    else:
        # Si la solicitud es GET, redirigir a otra página o mostrar un mensaje
        return 'Método GET no permitido en esta ruta'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

