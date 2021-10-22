"""Create and execute asynchronous tasks in a loop."""
import asyncio
import time

from logger import LOGGER

from .coroutines import simple_coroutine
from .futures import register_future
from .loops import inspect_event_loop
from .tasks import create_tasks


async def init_script(start_time: float):
    """
    Demo of an asynchronous script's lifecycle.

    :param float start_time: Counter representing the time the script was initialized.
    """
    LOGGER.info(f"Asyncio tutorial Part I: Intro to Asyncio.")
    future = register_future()
    await create_and_execute_tasks()
    future.set_result(
        f"Executed {__name__} in {time.perf_counter() - start_time:0.2f} seconds."
    )


async def create_and_execute_tasks():
    """Creates tasks and executes them in an event loop."""
    task_list = await create_tasks(simple_coroutine)
    inspect_event_loop()
    await asyncio.gather(*task_list)
