import streamlit as st

# Título de la aplicación
st.title("Comparación de Sistemas Operativos: Linux, Windows y macOS")

# Sección de introducción
st.header("Introducción")
st.write("""
En esta aplicación, vamos a comparar tres sistemas operativos principales: **Linux**, **Windows**, y **macOS**.
Nos enfocaremos en varios aspectos como la estructura, interfaz de usuario, gestión de GPU, soporte de software y comunidad.
""")

# Sección de estructura y filosofía
st.header("1. Estructura y Filosofía")

# Tabla comparativa de estructura y filosofía
st.write("""
| Aspecto            | Linux                         | Windows                       | macOS                         |
|--------------------|-------------------------------|-------------------------------|-------------------------------|
| **Licencia**        | Open Source                   | Propietario                   | Propietario                   |
| **Kernel**          | Basado en Unix (Kernel Linux) | Basado en NT (Kernel propio)   | Basado en Unix                |
| **Usuarios**        | Desarrolladores, servidores   | Hogares, empresas, juegos      | Diseño gráfico, multimedia    |
| **Sistema de archivos** | ext4, Btrfs, ZFS           | NTFS                          | APFS                          |
""")

# Sección de interfaz de usuario
st.header("2. Interfaz de Usuario")
st.write("""
- **Linux**: Variedad de entornos de escritorio (GNOME, KDE, XFCE) que permiten una personalización completa.
- **Windows**: Un único entorno con barra de tareas y menú de inicio. Amplio uso de GUI.
- **macOS**: Interfaz gráfica coherente y simple, popular entre los usuarios de productos Apple.
""")

# Sección de gestión de GPU
st.header("3. Gestión de GPU")
st.write("""
| Sistema Operativo   | Soporte GPU                            | Uso en Computación Científica |
|---------------------|----------------------------------------|-------------------------------|
| **Linux**           | Soporte manual (NVIDIA/AMD), CUDA, OpenCL | Popular para IA y computación en paralelo |
| **Windows**         | Soporte automático, DirectX, Vulkan    | Menos común en entornos de desarrollo científicos |
| **macOS**           | Soporte cerrado, buen soporte para eGPU | No común en computación científica |
""")

# Sección de soporte de software y usos especializados
st.header("4. Soporte de Software y Usos Especializados")
st.write("""
- **Linux**: Popular para servidores, desarrollo de software y computación científica.
- **Windows**: Más utilizado en hogares, empresas y juegos, con una amplia compatibilidad de software.
- **macOS**: Enfocado en diseño gráfico, producción multimedia y usuarios del ecosistema Apple.
""")

# Sección de comunidad y soporte
st.header("5. Comunidad y Soporte")
st.write("""
- **Linux**: Comunidad muy activa y global, soporte a través de foros y documentación abierta.
- **Windows**: Soporte comercial por parte de Microsoft, amplia comunidad en línea.
- **macOS**: Soporte oficial de Apple a través de AppleCare, pero con una comunidad más pequeña comparada con Linux.
""")

# Despliegue interactivo
st.sidebar.title("Menú")
opcion = st.sidebar.selectbox("Selecciona una sección", 
                              ("Introducción", "Estructura y Filosofía", "Interfaz de Usuario", 
                               "Gestión de GPU", "Soporte de Software", "Comunidad y Soporte"))

if opcion == "Introducción":
    st.write("Has seleccionado la **Introducción**.")
elif opcion == "Estructura y Filosofía":
    st.write("Estás en la sección de **Estructura y Filosofía**.")
elif opcion == "Interfaz de Usuario":
    st.write("Estás en la sección de **Interfaz de Usuario**.")
elif opcion == "Gestión de GPU":
    st.write("Estás en la sección de **Gestión de GPU**.")
elif opcion == "Soporte de Software":
    st.write("Estás en la sección de **Soporte de Software**.")
elif opcion == "Comunidad y Soporte":
    st.write("Estás en la sección de **Comunidad y Soporte**.")

# Mostrar una comparación final en la interfaz
st.header("Conclusión")
st.write("""
Cada sistema operativo tiene sus fortalezas y debilidades. Linux destaca en servidores y desarrollo, Windows en juegos y software comercial, y macOS en la creación multimedia y el ecosistema Apple. ¡La elección depende de tus necesidades!
""")
