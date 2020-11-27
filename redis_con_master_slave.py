import redis
from redis import StrictRedis

try:
    # 1.链接数据库
    client = redis.StrictRedis(
        # host='127.0.0.1',
        # host='47.99.37.225',
        host='172.28.244.109',
        port=6379,
        db=0
    )

    # ２　操作数据库
    data_key = 'Vail'
    result = client.set(data_key, 'sherry vail')
    print(result)
    # client.set("name","itheima")

    check_data = client.get(data_key)
    print(check_data)
    # client.delete('name')

    # result = client.keys()
    # result = client.values()
    #
    # print(result)


except Exception as e:
    print(e)
