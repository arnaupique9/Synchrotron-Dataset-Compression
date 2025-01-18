import fabio 
import numpy as np 
import os

def cbf_to_raw(file_path, output_dir):
    # Obrir el fitxer CBF
    cbf_image = fabio.open(file_path)
    # Extraure dades de la imatge com un array
    data = cbf_image.data

    # Extraer el nom base del fitxer sense extensió
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Convertir les dades a big-endian
    data_be = data.astype(np.int32).byteswap().newbyteorder()
    # Ruta de sortir
    output_file_be = os.path.join(output_dir, f"{base_name}_s32be-1x2463x2527.raw")
    # Guardar en big-endian
    data_be.tofile(output_file_be)

if __name__ == "__main__":
    # Definir directoris
    input_base_dir = "dir_entrada"
    output_base_dir = "dir_sortida"

    # Iteració de carpetes
    for folder_name in os.listdir(input_base_dir):
        input_dir = os.path.join(input_base_dir, folder_name)
        output_dir = os.path.join(output_base_dir, folder_name)

        # Verificació carpeta sortida
        os.makedirs(output_dir, exist_ok=True)

        # Iteraració de fitxers
        if os.path.isdir(input_dir):
            for file_name in os.listdir(input_dir):
                if file_name.endswith(".cbf"):
                    file_path = os.path.join(input_dir, file_name)
                    cbf_to_raw(file_path, output_dir)

