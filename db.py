import json

class MysqlDatabases:
    def __init__(self):
        with open('items.json', mode='r', encoding='utf-8') as f:
            items = f.read()
        self.items = json.loads(items)

    def all(self):
        return self.items

db = MysqlDatabases()
if __name__ == '__main__':
    print(db.all())