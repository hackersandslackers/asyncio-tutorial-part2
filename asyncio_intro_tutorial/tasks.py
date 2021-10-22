"""Create a task from a coroutine."""
import asyncio
from asyncio import Task
from typing import Coroutine, List


async def create_tasks(simple_coroutine: Coroutine) -> List[Task]:
    """
    Create asyncio tasks to be executed.

    :returns: List[Task]
    """
    task_list = []
    for i in range(3):
        task = asyncio.create_task(simple_coroutine(i, delay=1))
        task_list.append(task)
    return task_list
