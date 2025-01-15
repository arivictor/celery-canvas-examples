# Celery Canvas Examples

Start the worker:

```shell
celery -A 0-worker  worker --loglevel=INFO
```

From another terminal call a operation:

```shell
# example
python3 1-single_task.py
```

Look at the operation file to see how its implemented

## Notes

**Adding a Task to Queue**
`some_task.delay()` and `some_task.apply_async()` are essentially the same but the latter offers more control and configuration. Please read the official docuemntation on each to better understand. For most usecase if you just want to put a task on the queue as-is, `delay()` will suffice.
