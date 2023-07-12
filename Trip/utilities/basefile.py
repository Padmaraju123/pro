import pytest
import logging


@pytest.mark.usefixtures("invoke_browser")
class Base:

    def get_logger(self):
        logger = logging.getLogger(__name__)

        filehandler_obj = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s ")
        filehandler_obj.setFormatter(formatter)
        logger.addHandler(filehandler_obj)

        logger.setLevel(logging.INFO)
        logger.debug("A debug statement is executed.")
        logger.info("A info is executed")
        logger.warning("Something is warning mode")
        logger.error("A major error occur")
        logger.critical("Critical issue")


