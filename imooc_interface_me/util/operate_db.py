#encode:utf-8
import MySQLdb.cursors

class OperateDB:
    '''操作数据库
    '''
    def __init__(self):
        self.conn = MySQLdb.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = '12345678',
            db = 'interface_test',
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor  # 以字典形式返回
        )
        self.cursor = self.conn.cursor()  # 创建游标

    def search_one(self,sql):
        '''查询一条数据
        '''
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.conn.close()
        return res

if __name__ == '__main__':
    db = OperateDB()
    result = db.search_one("select * from user_info where userName='zhangsan'")
    print(result)

