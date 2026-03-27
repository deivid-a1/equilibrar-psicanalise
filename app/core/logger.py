import logging
import sys
from loguru import logger

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            if frame.f_back:
                frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )

def setup_logging():
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(logging.INFO)

    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = [InterceptHandler()]
        logging.getLogger(name).propagate = False

    logger.configure(handlers=[{"sink": sys.stdout, "level": logging.DEBUG}])
    logger.add("logs/app_info.log", level="INFO", rotation="10 MB", retention="7 days")
    logger.add("logs/app_debug.log", level="DEBUG", rotation="10 MB", retention="7 days")