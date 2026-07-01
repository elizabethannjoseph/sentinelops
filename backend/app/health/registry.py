from app.health.glpi import GLPIHealthCheck
from app.health.glpi import GLPIHealthCheck
from app.health.postgres import PostgreSQLHealthCheck

registry = [
    GLPIHealthCheck(),
    PostgreSQLHealthCheck(),
]
