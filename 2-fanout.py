from celery import group
from celery.result import allow_join_result

from worker import add


def main():
    """

    Demonstrates fanning out multiple tasks to the queue.
    No result is awaited.

    """
    items = [1, 2, 3, 4, 5]
    group(
        add.s(item, 2) for item in items
    ).delay()


if __name__ == "__main__":
    main()