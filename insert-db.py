# -*- coding: utf-8 -*-
# !/usr/bin/env python
'''
@time    : 2019/11/16 11:46
@email   : 774664710@qq.com
@author  : baojinlong
@description: 批量爬虫工业构建数据
'''
import pymysql
import random
from faker import Faker


# 插入数据到mysql
def insert_mysql(insert_data, table_name):
    # 1.连接
    conn = pymysql.connect(host='localhost', user='root', password='root', db='local_test', charset='utf8')
    # 创建一个游标
    cursor = conn.cursor()
    # 插入数据
    sql = f"INSERT INTO {table_name}(create_time,campaign_id,link_url,channel_type,tenant_id,campaign_type,node_id,instance_his_id,message_id) VALUES " \
          f"( '{insert_data['create_time']}', '{insert_data['campaign_id']}', '{insert_data['link_url']}', '{insert_data['channel_type']}', '{insert_data['tenant_id']}', " \
          f"'{insert_data['campaign_type']}', '{insert_data['node_id']}', '{insert_data['instance_his_id']}', '{insert_data['message_id']}')"
    cursor.execute(sql)

    conn.commit()  # 提交
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接


# 从请求的url字符串中获取基本参数字典
def gen_time():
    return china_faker.date_time_between(start_date='-{}d'.format(random.randint(1, 1)),
                                         end_date='now').strftime(format='%Y-%m-%d %H:%M:%S')


# 爬取数据并同步到mysql中
if __name__ == '__main__':
    #  详情页打开的基本参数对应的key
    table_name = 'event_all_action_history'
    # 插入记录数 4864
    num_count = 1
    campaign_id = 391
    node_id = 4
    instance_id = 177363
    china_faker = Faker('zh_CN')
    for i in range(num_count):
        insert_data = {}
        insert_data['create_time'] = gen_time()
        insert_data['campaign_id'] = campaign_id
        insert_data['link_url'] = -1
        insert_data['channel_type'] = 1
        insert_data['tenant_id'] = 12818
        insert_data['campaign_type'] = 1
        insert_data['node_id'] = node_id
        insert_data['instance_his_id'] = instance_id
        insert_data['message_id'] = -1
        insert_mysql(insert_data, table_name)
    else:
        print('插入完毕ok')
