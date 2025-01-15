# Celery Primitives Example

Start the worker:

```shell
celery -A 0-worker  worker --loglevel=INFO
```

From another terminal call a operation:

```shell
# example
python3 1-single_task.py
```

Look at the operation file to see how its implemented# celery-canvas-examples
