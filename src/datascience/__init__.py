import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Define logger
logger = logging.getLogger("customLogger")
logger.setLevel(logging.DEBUG)  # Log levels: DEBUG < INFO < WARNING < ERROR < CRITICAL

# Formatter
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# File handler
file_handler = logging.FileHandler("logs/app.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

# Avoid duplicate logs
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Optional: to prevent propagation to root logger
logger.propagate = False
