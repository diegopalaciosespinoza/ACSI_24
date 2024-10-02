import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Comparación de Sistemas Operativos: Linux, Windows y macOS")

# Introducción
st.header("Introducción")
st.write("""
Esta aplicación compara tres sistemas operativos principales: **Linux**, **Windows**, y **macOS**. 
""")

# Selección de secciones
st.sidebar.title("Menú Interactivo")
opcion = st.sidebar.selectbox("Selecciona una sección", 
                              ("Introducción", "Estructura y Filosofía", 
                               "Interfaz de Usuario", "Gestión de GPU", 
                               "Soporte de Software", "Comunidad y Soporte", 
                               "Gráficos Interactivos"))

# Estructura y Filosofía
if opcion == "Estructura y Filosofía":
    st.header("1. Estructura y Filosofía")
    data = {
        'Aspecto': ['Licencia', 'Kernel', 'Usuarios', 'Sistema de Archivos'],
        'Linux': ['Open Source', 'Basado en Unix (Kernel Linux)', 'Desarrolladores, servidores', 'ext4, Btrfs, ZFS'],
        'Windows': ['Propietario', 'Basado en NT (Kernel propio)', 'Hogares, empresas, juegos', 'NTFS'],
        'macOS': ['Propietario', 'Basado en Unix', 'Diseño gráfico, multimedia', 'APFS']
    }
    df = pd.DataFrame(data)
    st.table(df)

# Interfaz de Usuario
elif opcion == "Interfaz de Usuario":
    st.header("2. Interfaz de Usuario")
    st.write("""
    - **Linux**: Variedad de entornos de escritorio (GNOME, KDE, XFCE) que permiten personalización completa.
    - **Windows**: Un único entorno con barra de tareas y menú de inicio. Amplio uso de GUI.
    - **macOS**: Interfaz gráfica coherente y simple, popular entre los usuarios de productos Apple.
    """)
    st.image("https://i.ytimg.com/vi/n0vJ-AEL1es/maxresdefault.jpg", caption="Entorno de Escritorio GNOME en Linux", use_column_width=True)

# Gestión de GPU
elif opcion == "Gestión de GPU":
    st.header("3. Gestión de GPU")
    st.write("""
    Comparación de la gestión de GPUs entre los sistemas operativos.
    """)
    # Datos para el gráfico de GPU
    gpu_data = {
        'Sistemas Operativos': ['Linux', 'Windows', 'macOS'],
        'Soporte Manual de GPU (NVIDIA/AMD)': [8, 9, 5],
        'Optimización para Computación Científica': [9, 7, 4],
        'Facilidad de Integración con eGPU': [6, 8, 9]
    }
    df_gpu = pd.DataFrame(gpu_data)
    
    # Crear gráfico de barras
    fig, ax = plt.subplots()
    df_gpu.set_index('Sistemas Operativos').plot(kind='bar', ax=ax)
    ax.set_ylabel('Puntuación (0-10)')
    ax.set_title('Comparación de Soporte de GPU por Sistema Operativo')
    st.pyplot(fig)

# Soporte de Software y Usos Especializados
elif opcion == "Soporte de Software":
    st.header("4. Soporte de Software y Usos Especializados")
    st.write("""
    - **Linux**: Popular para servidores, desarrollo de software y computación científica.
    - **Windows**: Más utilizado en hogares, empresas y juegos, con una amplia compatibilidad de software.
    - **macOS**: Enfocado en diseño gráfico, producción multimedia y usuarios del ecosistema Apple.
    """)

    # Muestra de tabla comparativa
    data_software = {
        'Aspecto': ['Desarrollo de Software', 'Gaming', 'Diseño Multimedia'],
        'Linux': ['Muy fuerte', 'Limitado', 'Moderado'],
        'Windows': ['Moderado', 'Muy fuerte', 'Moderado'],
        'macOS': ['Moderado', 'Limitado', 'Muy fuerte']
    }
    df_software = pd.DataFrame(data_software)
    st.table(df_software)

# Comunidad y Soporte
elif opcion == "Comunidad y Soporte":
    st.header("5. Comunidad y Soporte")
    st.write("""
    - **Linux**: Comunidad muy activa y global, soporte a través de foros y documentación abierta.
    - **Windows**: Soporte comercial por parte de Microsoft, amplia comunidad en línea.
    - **macOS**: Soporte oficial de Apple a través de AppleCare, pero con una comunidad más pequeña comparada con Linux.
    """)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2mJHtt39VBbSf7YCjw-Gh7sjOhe_gwcU0Iw&s", caption="Logotipo de Windows",width=600, use_column_width=True)

# Gráficos Interactivos
elif opcion == "Gráficos Interactivos":
    st.header("6. Gráficos Interactivos")

    # Datos para el gráfico interactivo
    os_data = {
        'Sistemas Operativos': ['Linux', 'Windows', 'macOS'],
        'Seguridad': [9, 6, 8],
        'Facilidad de Uso': [6, 9, 8],
        'Personalización': [10, 7, 5],
        'Compatibilidad de Software': [7, 10, 7]
    }
    df_os = pd.DataFrame(os_data)

    # Selección interactiva
    metric = st.selectbox('Selecciona la métrica para comparar:', 
                          ('Seguridad', 'Facilidad de Uso', 'Personalización', 'Compatibilidad de Software'))

    # Gráfico
    fig, ax = plt.subplots()
    df_os.plot(x='Sistemas Operativos', y=metric, kind='bar', ax=ax, color='skyblue')
    ax.set_title(f'Comparación de {metric}')
    st.pyplot(fig)
