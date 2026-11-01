import logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is a debug message")
logging.info("Application started successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("This is a critical error")

def divide(a, b):
    logging.info("Division operation started")

    try:
        result = a / b
        logging.info("Division completed successfully")
        return result

    except ZeroDivisionError:
        logging.exception("Cannot divide by zero")
        return None


print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

print("Check application.log for log messages.")