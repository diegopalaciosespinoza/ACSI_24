import os
import shutil
import subprocess
from PIL import Image
import streamlit as st


# Función para limpiar una carpeta
def clean_folder(folder_path):
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)


# Configuración inicial de Streamlit
st.title("CycleGAN Image Converter")
st.write("Sube una imagen para convertirla con CycleGAN.")

# Variables globales para carpetas
TEST_A_DIR = r"D:\Proyectos_Visual\pytorch-CycleGAN-and-pix2pix\datasets\testA"
RESULTS_DIR = r"D:\Proyectos_Visual\pytorch-CycleGAN-and-pix2pix\results\fakeRUS\experiment_name\test_latest\images"

# Subir imagen
uploaded_file = st.file_uploader("Cargar imagen", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Guardar imagen en carpeta testA
    original_image_name = os.path.splitext(uploaded_file.name)[0]  # Nombre sin extensión
    test_image_path = os.path.join(TEST_A_DIR, uploaded_file.name)
    with open(test_image_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(test_image_path, caption="Imagen cargada", use_column_width=True)

    # Botón para convertir la imagen
    if st.button("Convertir Imagen"):
        st.write("Ejecutando modelo...")

        try:
            # Ejecutar el modelo
            subprocess.run([
                r"D:\Proyectos_Visual\pytorch-CycleGAN-and-pix2pix\venv\Scripts\python.exe",
                "test.py",
                "--dataroot", "./datasets",
                "--name", "experiment_name",
                "--model", "cycle_gan",
                "--netG", "unet_256",
                "--input_nc", "1",
                "--output_nc", "1",
                "--results_dir", "./results/fakeRUS",
                "--direction", "AtoB"
            ], check=True)

            st.write("Modelo ejecutado con éxito")

            # Mostrar imagen generada
            generated_image_path = os.path.join(
                RESULTS_DIR,
                f"{original_image_name}_fake_A.png"
            )
            if os.path.exists(generated_image_path):
                st.image(generated_image_path, caption="Imagen generada", use_column_width=True)
            else:
                st.error("No se encontró la imagen generada.")

        except subprocess.CalledProcessError as e:
            st.error(f"Error al ejecutar test.py: {e}")

# Botón para limpiar archivos
if st.button("Finalizar"):
    st.write("Limpiando archivos...")
    clean_folder(TEST_A_DIR)
    clean_folder(RESULTS_DIR)
    st.success("Archivos eliminados. Puedes cargar una nueva imagen.")
