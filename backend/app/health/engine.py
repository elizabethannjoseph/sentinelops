from app.health.registry import registry
from app.repositories.health_repository import HealthRepository


class HealthEngine:

    async def run(self):

        results = []
        repository = HealthRepository()

        for checker in registry:
            result = await checker.check()
            repository.save(result)
            results.append(result)

        return results