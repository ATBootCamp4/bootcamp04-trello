"""Module to read environment variables"""
from configparser import ConfigParser


class EnvironmentVariableReader:
    """Class to read environment variables"""

    _environment_variables = ConfigParser()

    def __init__(self, file_path='behave.ini'):
        """Initialize"""
        self._environment_variables.read(file_path)

    @classmethod
    def get_variable(cls, section, data):
        """Get a variable value from file

        :param section: Section on the ini file
        :type section: str
        :param data: Data on the ini file
        :type data: str
        :return: Value from the ini file
        :rtype: str
        """
        try:
            env_var = cls._environment_variables[section][data]
            return env_var
        except KeyError as error:
            print('{} environment variable was not found in behave.ini'.format(error))
