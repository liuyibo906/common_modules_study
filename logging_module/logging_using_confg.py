# email liuyibo906@163.com
# 时间 2022/11/28 20:59
#使用配置文件
import logging
import logging.config
#读取配置文件
logging.config.fileConfig('D:/PycharmProjects/common_modules_study/logging_module/logging.conf')

logger = logging.getLogger('applog')
logger.debug("This is Logger, debug")

root_logger=logging.getLogger()
root_logger.debug('this is root logger,debug')

try:
    int('a')
except Exception as e:
    logger.exception(e)