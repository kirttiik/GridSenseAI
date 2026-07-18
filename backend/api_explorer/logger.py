import logging
import sys

def setup_logger():
    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logger = logging.getLogger("api_explorer")
    logger.setLevel(logging.INFO)
    
    # Create console handler with formatting
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    
    # Avoid duplicate logs
    if not logger.handlers:
        logger.addHandler(ch)
        
    return logger

logger = setup_logger()
