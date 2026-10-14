"""Gunicorn WSGI server configuration."""
import multiprocessing
import os

bind = f"{os.environ.get('HOST', '0.0.0.0')}:{os.environ.get('PORT', '5000')}"
worker_class = os.environ.get("GUNICORN_WORKER_CLASS", "gthread")
workers = int(os.environ.get(
    "GUNICORN_WORKERS",
    str(multiprocessing.cpu_count() * 2 + 1)))
threads = int(os.environ.get("GUNICORN_THREADS", "4"))
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "60"))
keepalive = int(os.environ.get("GUNICORN_KEEPALIVE", "5"))

accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("GUNICORN_LOG_LEVEL", "info")
access_log_format = (
    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)sµs')
