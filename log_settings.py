import logging
from logging.handlers import TimedRotatingFileHandler  
import os

directory = os.path.join('log')
if not os.path.exists(directory):
    os.makedirs(directory)  
filename = os.path.join(directory,'{}.log') 

format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s'  

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': format
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': filename.format('info'),
            'when': 'midnight',
            'backupCount': 5,
            'interval': 1,
            'formatter': 'standard'
        },  
        'error_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': filename.format('error'),
            'when': 'midnight',
            'backupCount': 5,
            'interval': 1,
            'formatter': 'standard'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'error_handler', 'console'],
            'level': 'DEBUG',
            'propagate': True  # 是否继承父类的log信息
        },  # handlers 来自于上面的 handlers 定义的内容
        'django.request': {
            'handlers': ['default', 'error_handler', 'console'],
            'level': 'ERROR',
            'propagate': False
        }
    }
}
