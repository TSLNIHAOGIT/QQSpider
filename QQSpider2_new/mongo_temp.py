from pymongo import MongoClient
import datetime
class MongoManager(object):

    def __init__(self, server_ip='localhost', client=None):
        print(server_ip)
        self.client = MongoClient(server_ip, 27017) if client is None else client
        # self.redis_client = redis.StrictRedis(host=server_ip, port=6379, db=0)
        self.mongo_db = self.client.QQ
        #有插入操作后才会在数据库中产生
        self.mongo_db.query.insert({

            # 'time': datetime.utcnow(),
            'prediction': '''[prediction]'''})
if __name__=='__main__':
    MongoManager()