import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Set the logger's level
logger.setLevel(logging.INFO)

# Create a formatter object
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Set the formatter's format
formatter.format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Add the formatter to the logger
logger.addHandler(logging.StreamHandler())

# Log a message
# logger.info('This is an info message.')
