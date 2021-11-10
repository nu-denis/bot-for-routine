from configparser import ConfigParser
import os.path

config = ConfigParser()
config.read('config.cfg')
if os.path.isfile('config.dev.cfg'):
		config_dev = ConfigParser()
		config_dev.read('config.dev.cfg')
		config = config_dev
