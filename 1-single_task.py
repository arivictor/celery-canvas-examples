from celery.result import allow_join_result

from worker import add


def main():
    """

    Demonstrates running a single task and awaiting the result.
    
    """
    task = add.apply_async((1, 2))
    with allow_join_result():
        result = task.get()
        print("result", result)


if __name__ == "__main__":
    main()