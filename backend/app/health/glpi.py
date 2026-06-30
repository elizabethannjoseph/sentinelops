import time

from app.health.base import HealthCheck
from app.health.result import HealthResult


class GLPIHealthCheck(HealthCheck):

    async def check(self) -> HealthResult:
        start = time.perf_counter()

        elapsed = (time.perf_counter() - start) * 1000

        return HealthResult(
            service_name="GLPI",
            status="Healthy",
            response_time_ms=elapsed,
        )