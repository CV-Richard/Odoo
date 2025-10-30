FROM odoo:18.0

USER root

# Instala debugpy ignorando el entorno externo administrado
RUN pip install --break-system-packages debugpy

USER odoo