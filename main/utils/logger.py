"""
This module lets the dev create a custom logger

Classes:
    Logger
"""
import logging
import logging.config
import datetime

MAIN_FORMAT = '%(asctime)s %(levelname)-6s %(name)-12s:: %(message)s'
REST_API_FORMAT = '%(asctime)s %(message)s'
TITLE_FORMAT = '%(message)s'


class Logger(logging.Logger):
    """A class to implement the use of a customized data logger, based on the native logging lib."""
    handlers = []

    def __init__(self, name='main', log_level=logging.WARNING, str_format=MAIN_FORMAT):
        """
        Constructs all the necessary attributes for the Logger to work properly.

        :param name:   str  The name with which the logger will be identified and accessed.
        """
        suite_name = name.split('.')[-1:][0]
        today = datetime.datetime.now().isoformat(' ', 'seconds')[:10]

        logging.Logger.__init__(self, suite_name)
        console_handler = logging.StreamHandler()
        if 'request_manager' in suite_name:
            str_format = REST_API_FORMAT
            file_name = f"./logs/requests_{today}.log"
        else:
            file_name = f"./logs/console_{today}.log"

        formatter = logging.Formatter(str_format, datefmt='%d-%m-%y %H:%M:%S')
        self.setup_logger(suite_name, file_name, formatter)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        self.handlers.append(console_handler)
        # Format for titles
        self.title_formatter = logging.Formatter(TITLE_FORMAT)

    def setup_logger(self, name, log_file, formatter, level=logging.DEBUG):
        """To setup as many loggers as you want"""

        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        self.handlers.append(handler)

    def info(self, message, is_title=False):
        """ Helps to log a INFO message with a Title format.

        :param message:  str    The message to send
        :param is_title: bool   Will remove the formatter of the handlers temporary if True. Default is False.
        """
        prev_formattters = []
        if is_title:
            for handler in self.handlers:
                prev_formattters.append(handler.formatter)
                handler.setFormatter(self.title_formatter)
        super().info(message)
        for idx, formatter in enumerate(prev_formattters):
            self.handlers[idx].formatter = formatter

    def debug(self, message, is_title=False):
        """ Helps to log a DEBUG message with a Title format.

        :param message:  str    The message to send
        :param is_title: bool   Will remove the formatter of the handlers temporary if True. Default is False.
        """
        prev_formattters = []
        if is_title:
            for handler in self.handlers:
                prev_formattters.append(handler.formatter)
                handler.setFormatter(self.title_formatter)
        super().debug(message)
        for idx, formatter in enumerate(prev_formattters):
            self.handlers[idx].formatter = formatter

    def close(self):
        """Close the logger session"""
        for handler in self.handlers:
            handler.flush()
            handler.close()
