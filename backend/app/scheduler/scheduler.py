import asyncio

from app.health.engine import HealthEngine


class Scheduler:

    def __init__(self):
        self.engine = HealthEngine()

    async def start(self):

        while True:

            logger.info("Running health checks...")

            await self.engine.run()

            await asyncio.sleep(5)