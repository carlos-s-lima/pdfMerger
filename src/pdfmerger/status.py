from enum import Enum

class Status(Enum):
    WAITING = 'Waiting'
    PROCESSING = 'Processing'
    SUCCESS = 'Success'
    ERROR = 'Error'
