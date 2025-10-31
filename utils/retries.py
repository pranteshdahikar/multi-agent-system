# utils/retries.py
import time
import logging

def retry(fn, retries=3, base_delay=1.0, exceptions=(Exception,)):
    for attempt in range(1, retries+1):
        try:
            return fn()
        except exceptions as e:
            logging.warning(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                raise
            time.sleep(base_delay * (2 ** (attempt-1)))
