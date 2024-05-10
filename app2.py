from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Obtener los archivos subidos
    zoho_file = request.files['zoho_file']
    sunnova_file = request.files['sunnova_file']

    # Leer los datos desde los archivos CSV
    zoho_df = pd.read_csv(zoho_file)
    sunnova_df = pd.read_csv(sunnova_file)

    # Realizar la unión de los DataFrames utilizando los campos "Sunnova Project ID" y "Sunnova System ID"
    merged_df = pd.merge(zoho_df, sunnova_df, left_on='Sunnova Project ID', right_on='Sunnova System ID', how='left')

    # Crear un objeto de BytesIO para escribir el archivo CSV
    output = io.BytesIO()
    merged_df.to_csv(output, index=False)

    # Devolver el archivo CSV como una respuesta HTTP
    return send_file(output, as_attachment=True, download_name='informe_combinado.csv')




if __name__ == '__main__':
    app.run(debug=True)
