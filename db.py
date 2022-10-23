import json

class MysqlDatabases:
    def __init__(self):
        with open('items.json', mode='r', encoding='utf-8') as f:
            items = f.read()
        self.items = json.loads(items)

    def all(self):
        return self.items
    
    def insert(self, item):
        self.items["items"].append(item)

    def delete(self, item_name):
        for item in self.items["items"]:
            if (item == item_name):
                self.items["items"].remove(item)
                return True, '删除成功'
        
        return False, '物品不存在'

    def search(self, item_name):
        for item in self.items["items"]:
            if (item == item_name):
                return True, '查找成功'
        
        return False, '物品不存在'

db = MysqlDatabases()
if __name__ == '__main__':
    print(db.all())