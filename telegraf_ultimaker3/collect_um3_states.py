#!/usr/bin/python3
import logging
import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


PRINTER_HOSTNAME = '192.168.1.23'
PRINTER_API_VERSION = '1'
PRINTER_API_URL = f'http://{PRINTER_HOSTNAME}/api/v{PRINTER_API_VERSION}/'
PRINTER_HOST_TAG = 'ultimaker3'


def generate(key, value, as_str=False, tags=None):
    """Creates a nicely formatted Key(Value) item for output."""
    tags = tags if tags is not None else {}
    formatted_tags = [f',{tag_key}={tag_value}' for tag_key, tag_value in tags.items()] or ''
    qs = qe = '"' if as_str else ''

    return f'{PRINTER_HOST_TAG}{formatted_tags} {key}={qs}{value}{qe}'


def get_print_job_info():
    response = requests.get(PRINTER_API_URL + 'print_job')
    if response.status_code == 200:
        for key, value in response.json().items():
            if value or value == 0:
                print(generate('print_job_' + key, value, not isinstance(value, (int, float))))


def main():
    logger.info('Start UM3 states collection')

    api_calls = [
        ('printer_status', 'printer/status', lambda x: x, True),
        ('bed_temperature_target', 'printer/bed/temperature', lambda x: x['target'], False),
        ('bed_temperature_current', 'printer/bed/temperature', lambda x: x['current'], False),
        ('extruder_0_temperature_current',
         'printer/heads/0/extruders/0/hotend/temperature',
         lambda x:x['current'], False),
        ('extruder_0_temperature_target',
         'printer/heads/0/extruders/0/hotend/temperature',
         lambda x: x['target'], False),
        ('extruder_1_temperature_current',
         'printer/heads/0/extruders/1/hotend/temperature',
         lambda x: x['current'], False),
        ('extruder_1_temperature_target',
         'printer/heads/0/extruders/1/hotend/temperature',
         lambda x: x['target'], False),
    ]

    for name, call, getter, as_str in api_calls:
        response = requests.get(PRINTER_API_URL + call)
        print(generate(name, getter(response.json()), as_str))

    get_print_job_info()

    logger.info('Finished UM3 states collection')


if __name__ == '__main__':
    main()