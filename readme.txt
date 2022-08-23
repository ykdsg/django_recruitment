极客时间-Django快速开发实战，相关代码。

以及DRF 相关demo练习。

区分了不同环境的配置，放在settings下面。所以启动的时候需要加上配置参数
--settings=settings.local
如果是通过pycharm启动的，需要配置环境变量 DJANGO_SETTINGS_MODULE ，因为默认的配置在manage.py里面配置了base

进入Django shell
python manage.py shell