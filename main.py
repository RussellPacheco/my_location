import os
import logging
from flask import Flask


log_level = os.getenv("LOG_LEVEL", "INFO")
log_file = os.getenv("LOG_FILE", "my_location.log")

numeric_level = getattr(logging, log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % log_level)
logger = logging.getLogger("my_location")
logger.setLevel(log_level)
fh = logging.FileHandler(log_file,  encoding='utf-8', mode='a')
fh.setLevel(log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)


