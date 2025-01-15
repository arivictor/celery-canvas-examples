from celery import chord
from celery.result import allow_join_result

from worker import add, callback


def main():
    """
    
    Demonstrates fanning-out and fanning-in using Chord
    
    Input:              Output:
    [1, 2, 3, 4, 5] ->  25

    """
    items = [1, 2, 3, 4, 5]
    task = chord(
        add.s(item, 2) for item in items
        )(callback.s())

    with allow_join_result():
        result = task.get()
        print("result", result)


if __name__ == "__main__":
    main()