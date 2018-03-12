# py-logger

使用方法:在django專案所屬的settings.py加入下面code就可以自動log了

```
try:
    from loggers.log_settings import *
except Exception as e:
    # in case of any error, pass silently.
    pass
```
