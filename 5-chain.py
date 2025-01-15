from celery import chain, group
from celery.result import allow_join_result
from worker import add, callback


def main():
    """
    
    Demonstrates chaining multiple operations
    - chain() passes the result of one task to the next
    - group() runs multiple tasks in parallel

    Therefore, this is a manual fan-out and fan-in operation.
    
    Input:              Output:
    [1, 2, 3, 4, 5] ->  25
    """
    items = [1, 2, 3, 4, 5]
    group_chain_task = chain(
        group(
            add.s(item, 2) for item in items # same as [add.s(1, 2), add.s(2, 2), ...]
        ),
        callback.s()
    ).delay()

    with allow_join_result():
        result = group_chain_task.get()
        print("result", result)


if __name__ == "__main__":
    main()