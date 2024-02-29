from flask import Flask, render_template
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Obtener la cadena de conexión de la variable de entorno
CONNECTION_STRING = os.getenv("DefaultEndpointsProtocol=https;AccountName=dashboard0553205910;AccountKey=OoXmxQggOf112qqUP//depSiJ9j6ROaiz7zuwef02VZnH7gUBCqB6sPCIM3+cish6VDx8Pcve6IJ+AStUk5PBg==;EndpointSuffix=core.windows.net")

# Verificar si la cadena de conexión está configurada
if not CONNECTION_STRING:
    raise ValueError("La variable de entorno AZURE_STORAGE_CONNECTION_STRING no está configurada.")

# Nombre del contenedor de Blob donde están almacenadas las imágenes
CONTAINER_NAME = "basedatoscsv"

# Conectar a tu cuenta de Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

@app.route("/")
def mostrar_imagenes():
    # Obtener una lista de los blobs (imágenes) en el contenedor
    blobs = blob_service_client.get_container_client(CONTAINER_NAME).list_blobs()

    # Renderizar la plantilla HTML pasando la lista de blobs como contexto
    return render_template("index.html", blobs=blobs)

if __name__ == "__main__":
    app.run(debug=True)
