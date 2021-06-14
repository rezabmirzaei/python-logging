import logging

logger = logging.getLogger(__name__)


class Subclass:

    def __init__(self) -> None:
        logger.info('Initiating subclass')

    def test_log_info(self) -> None:
        logger.info('Subclass logging info')

    def test_log_warning(self) -> None:
        logger.warn('Subclass logging warning')
