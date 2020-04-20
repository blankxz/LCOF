from collections import OrderedDict


class LRUCathe:
    def __init__(self, capacity=120):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    # 更新k/v
    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            # 更新key到表头
            self.od[key] = value
        else:
            self.od[key] = value
            # 判断当前容量是否满了
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)