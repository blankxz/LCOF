from flask import Flask, request
from flask.views import MethodView

app = Flask(__name__)
REDIS_CONF = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 1
}
app.config.update({'REDIS_CONF': REDIS_CONF})

from redis import StrictRedis
import random

REDIS = StrictRedis(**REDIS_CONF)


class GetGoods(MethodView):
    def post(self):
        uid = random.randint(1, 10)
        if REDIS.lpop('goods_list'):
            if REDIS.hset('user_list', uid, 1):
                print(f'Success,{uid}')
                return f'Success,{uid}'
            else:
                # 不可重复抢（每人限领一个）
                print(f'push ,{uid}')
                REDIS.lpush('goods_list', 1)
                return f'create a user {uid}'
        else:
            # 已抢完
            print('Finsh!')
            return 'Finsh!'

    def get(self):
        user_list = REDIS.hgetall('user_list')
        user_list_len = REDIS.hlen('user_list')
        goods_list = REDIS.llen('goods_list')
        result_dict = {"user_list": user_list, "user_list_len": user_list_len, 'goods_list': goods_list}
        print(result_dict)
        return 'success!'


class SendGoods(MethodView):
    def post(self):
        count = request.form.get('count')
        if REDIS.exists('goods_list'):
            print('delet exists goods')
            REDIS.delete('goods_list')

        for item in range(int(count)):
            REDIS.lpush('goods_list', 1)
        REDIS.delete('user_list')
        goods_list = REDIS.lrange('goods_list', 0, count)
        return f'send goods success! {goods_list}'


# 用户抢购接口
app.add_url_rule('/goods', view_func=GetGoods.as_view('goods'), methods=['POST'])
# 商家查看商品抢购结果
app.add_url_rule('/goods', view_func=GetGoods.as_view('get_goods'), methods=['GET'])
# 商家发布商品
app.add_url_rule('/send/goods', view_func=SendGoods.as_view('send_goods'), methods=['POST'])

app.run(host='127.0.0.1', port=8000, threaded=10, debug=True)