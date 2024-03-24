import kopf
import asyncio

LOCK: asyncio.Lock


@kopf.on.startup()
async def startup_fn(logger, **kwargs):
    global LOCK
    LOCK = asyncio.Lock()
    logger.info("Hello World!")
