# utils/monitoring.py
import logging, time, json, os
LOG_PATH = "logs/system.log"
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def log_event(level, message, extra=None):
    if extra is None: extra = {}
    logging.log(level, f"{message} | extra: {json.dumps(extra)}")
