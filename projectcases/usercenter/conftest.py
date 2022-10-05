from utils.log_util import logger
from utils.mysql_util import db

#获取验证码
def get_code(mobile):
    sql = "select code from users_verifycode where mobile = '%s' order by id desc limit 1" % mobile
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果：{result}')
    return result['code']

#删除用户
def delete_user(mobile):
    sql = "delete from users_userprofile where mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')
#删除验证码
def delete_code(mobile):
    sql = "delete from users_verifycode where mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')

#查询uid
def get_userid(mobile):
    sql = "select id from users_userprofile where mobile= '%s';" % mobile
    result = db.select_db_one(sql)
    return result['id']

#查询uuid
def get_shop_cart_num(username,goods_id):
    id = get_userid(username)
    sql = "select nums from trade_shoppingcart where user_id = %d and goods_id = %d" % (id, goods_id)
    result = db.select_db_one(sql)
    return result['nums']