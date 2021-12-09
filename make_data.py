#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


def main():
    Connect = pymysql.connect(host='localhost', user='root', password='root', database='ticket_management_system',
                              port=3306)
    Cursor = Connect.cursor()

    train_id_list = make_data_train(Connect, Cursor)
    make_data_seat(Connect, Cursor, train_id_list)

    Cursor.close()
    Connect.close()


def make_data_train(Connect, Cursor):
    """
    train表造数据

    :param Connect: 数据库连接对象
    :param Cursor: 游标对象
    :return: None
    """
    num = 20  # 插入记录数
    train_id_list = []
    departure_list = []
    destination_list = []
    date_list = []
    departure_time_list = []
    arrival_time_list = []
    # 车次
    id_list = random.sample(range(2222, 9999), num)
    for num_id in id_list:
        train_id_list.append(random.choice(['G', 'K', 'D', 'L']) + str(num_id))
    print(train_id_list)
    # 地点
    location_list = ['广州', '深圳', '佛山', '珠海', '厦门', '北京', '上海', '南京', '杭州', '天津', '成都', '西安', '桂林']
    for _ in range(num):
        temp_list = random.sample(location_list, 2)
        departure_list.append(temp_list[0])
        destination_list.append(temp_list[1])
    print(departure_list)
    print(destination_list)
    # 时间
    t1 = datetime.datetime.now() + datetime.timedelta(days=30)
    t2 = t1 + datetime.timedelta(days=30)
    start = int(time.mktime(tuple(t1.timetuple())))
    end = int(time.mktime(tuple(t2.timetuple())))
    for _ in range(num):
        t = random.randint(start, end)
        date_tuple = time.localtime(t)
        date_list.append(time.strftime("%Y-%m-%d", date_tuple))
        departure_time_list.append(time.strftime("%H:%M", date_tuple))
    print(date_list)
    print(departure_time_list)
    for departure_time in departure_time_list:
        arrival_time_list.append((datetime.datetime.strptime(departure_time, "%H:%M")
                                  + datetime.timedelta(minutes=random.randint(60, 250))).strftime("%H:%M"))
    print(arrival_time_list)
    # 插入数据库
    for i in range(num):
        sql = r"insert into train_information(train_id, departure, destination, date, departure_time, arrival_time) " \
              r"values ('%s', '%s', '%s', '%s', '%s', '%s');" \
              % (train_id_list[i], departure_list[i], destination_list[i],
                 date_list[i], departure_time_list[i], arrival_time_list[i])
        try:
            Cursor.execute(sql)
            Connect.commit()
        except Exception as e:
            print(sql)
            print(e)
            Connect.rollback()
    return train_id_list


def make_data_seat(Connect, Cursor, train_id_list):
    """
    seat表造数据

    :param Connect: 数据库连接对象
    :param Cursor: 游标对象
    :param train_id_list: train_id列表
    :return: None
    """
    row_num = 3
    col_num = 4
    seat_num_per_train = 48
    seat_id_list = []
    rank_list = []
    high_list = []
    low_list = []
    price_list = []
    # 高价和低价
    for _ in train_id_list:
        high_list.append(random.randint(200, 300))
        low_list.append(random.randint(100, 199))
    # 座位号, 座位等级, 票价
    for i in range(len(train_id_list)):
        for row in range(1, row_num + 1):
            for col in range(1, col_num + 1):
                if row == 1:
                    for t in ['A', 'B']:
                        seat_id_list.append('0' + str(row) + '车' + '0' + str(col) + t)
                        rank_list.append('一等座')
                        price_list.append(high_list[i])
                else:
                    for t in ['A', 'B', 'C', 'E', 'F']:
                        seat_id_list.append('0' + str(row) + '车' + '0' + str(col) + t)
                        rank_list.append('二等座')
                        price_list.append(low_list[i])
    print(seat_id_list)
    print(rank_list)
    print(price_list)
    # 插入数据库
    j = 0
    for i in range(len(seat_id_list)):
        train_id = train_id_list[j]
        sql = r"insert into seat_information values ('%s', '%s', '%s', '%s', '%s');" \
              % (train_id, seat_id_list[i], rank_list[i], price_list[i], 0)
        try:
            Cursor.execute(sql)
            Connect.commit()
            if (i + 1) % seat_num_per_train == 0:
                j += 1
        except Exception as e:
            print(sql)
            print(e)
            Connect.rollback()


if __name__ == '__main__':
    main()
