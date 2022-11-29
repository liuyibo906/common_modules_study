
#使用logging模块，未使用配置文件
import  logging
#创建记录器
logger = logging.getLogger('app.applog')
logger.setLevel(logging.DEBUG)

#创建处理器
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler= logging.FileHandler('./logging_oper.log')
fileHandler.setLevel(logging.INFO)

#创建格式
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

#记录器添加处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

#过滤器
flt= logging.Filter('app')
#记录器添加过滤器
logger.addFilter(flt)

#输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')