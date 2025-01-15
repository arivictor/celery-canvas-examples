from celery import group
from celery.result import allow_join_result

from worker import add


def main():
    """

    Demonstrates fanning out multiple tasks to the queue.
    
    Input:              Output:
    [1, 2, 3, 4, 5] -> [3, 4, 5, 6, 7]

    """
    items = [1, 2, 3, 4, 5]
    task = group(
        add.s(item, 2) for item in items
    ).delay()

    with allow_join_result():
        result = task.get()
        print("result", result)


if __name__ == "__main__":
    main()