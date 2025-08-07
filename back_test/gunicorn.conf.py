import multiprocessing

bind = "0.0.0.0:8000"

timeout = 120

# This means it will send to STDOUT the Access Log
accesslog = "-"

# Recommended formula is (num_cores * 2) + 1
workers = multiprocessing.cpu_count() * 2 + 1

# Use uvicorn workers with gunicorn as process manager
worker_class = "uvicorn_worker.UvicornWorker"

# Set high numbers to allow for worker restarts every once in a while
# but not so often
max_requests = 5000
max_requests_jitter = 500
