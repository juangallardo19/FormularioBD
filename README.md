# Taller 2 - Formularios Django

Proyecto académico desarrollado en Django que implementa dos aplicaciones independientes para el registro de **asistencia** y gestión de **solicitudes**, con formularios basados en `ModelForm` y persistencia en base de datos.

## Integrantes

| Rol   | Nombre              |
|-------|---------------------|
| Dev 1 | [Nombre Dev 1]      |
| Dev 2 | [Nombre Dev 2]      |

## Estructura del proyecto

```
ElectivaITaller/
├── taller_formularios_nombre_estudiantes/
│   ├── asistencia/          # App de registro de asistencia
│   │   ├── models.py        # Modelo Asistencia
│   │   ├── forms.py         # ModelForm de Asistencia
│   │   ├── views.py         # Vistas del formulario y confirmación
│   │   ├── urls.py          # Rutas de la app
│   │   └── templates/       # Plantillas HTML
│   ├── solicitudes/         # App de gestión de solicitudes
│   │   ├── models.py        # Modelo Solicitud
│   │   ├── forms.py         # ModelForm de Solicitud
│   │   ├── views.py         # Vistas del formulario y confirmación
│   │   ├── urls.py          # Rutas de la app
│   │   └── templates/       # Plantillas HTML
│   ├── taller_formularios_nombre_estudiantes/
│   │   ├── settings.py      # Configuración del proyecto
│   │   └── urls.py          # URLs raíz del proyecto
│   └── manage.py
├── venv/                    # Entorno virtual (no versionado)
├── .gitignore
└── README.md
```

## Aplicaciones

### asistencia
Registra la presencia de personas con los campos:
- Nombre completo, Documento de identidad, Correo electrónico
- Fecha de asistencia, Hora de ingreso, Hora de salida
- Presente (booleano), Observaciones (opcional)

**Rutas:**
- `/asistencia/` — Formulario de registro
- `/asistencia/confirmacion/` — Página de éxito

### solicitudes
Gestiona solicitudes de tipo académico, administrativo, técnico u otro con los campos:
- Nombre del solicitante, Documento de identidad, Correo electrónico
- Teléfono de contacto, Tipo de solicitud, Asunto
- Descripción detallada, Fecha de solicitud, Archivo adjunto (opcional)

**Rutas:**
- `/solicitudes/` — Formulario de solicitud
- `/solicitudes/confirmacion/` — Página de éxito

## Requisitos

- Python 3.10+
- Django 4.x o superior

## Instalación y ejecución local

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd ElectivaITaller

# 2. Crear y activar entorno virtual
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install django

# 4. Aplicar migraciones
cd taller_formularios_nombre_estudiantes
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario (para acceder al admin)
python manage.py createsuperuser

# 6. Ejecutar servidor
python manage.py runserver
```

Acceder en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Panel de administración: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Flujo de trabajo Git (GitFlow)

Este proyecto sigue la metodología **GitFlow**. Ver la sección de [GitFlow paso a paso](#gitflow-paso-a-paso) más abajo.

### Ramas principales

| Rama      | Propósito                                  |
|-----------|--------------------------------------------|
| `main`    | Código en producción, versiones estables   |
| `develop` | Integración de features en desarrollo      |

### Ramas de feature

| Rama                           | Responsable | Descripción                        |
|--------------------------------|-------------|------------------------------------|
| `feature/app-asistencia`       | Dev 1       | App de asistencia completa         |
| `feature/app-solicitudes`      | Dev 2       | App de solicitudes completa        |

## Tecnologías

- **Backend:** Python, Django
- **Base de datos:** SQLite (desarrollo)
- **Frontend:** HTML, CSS (plantillas Django)
- **Control de versiones:** Git + GitFlow
