from app.health.registry import registry


class HealthEngine:

    async def run(self):

        results = []

        for checker in registry:
            result = await checker.check()
            results.append(result)

        return results