"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# This must be imported after the Flask app is created
# pylint: disable=wrong-import-position,cyclic-import
from service import routes
# pylint: disable=wrong-import-position
from service.common import log_handlers

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("SERVICE RUNNING".center(70, "*"))
app.logger.info(70 * "*")
