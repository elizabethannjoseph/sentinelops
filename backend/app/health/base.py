from abc import ABC, abstractmethod

from app.health.result import HealthResult


class HealthCheck(ABC):

    @abstractmethod
    async def check(self) -> HealthResult:
        pass