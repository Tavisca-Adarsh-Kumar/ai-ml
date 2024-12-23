import logging
import lib
logger = logging.getLogger(__name__)

def main():
    print("Logging Demo Application")

    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    lib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()
