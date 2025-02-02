# 17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("sql statement inserted")
    def update(self):
        print("sql statement updated")
    def delete(self):
        print("sql statement deleted")
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("no sql statement inserted")
    def update(self):
        print("no sql statement updated")
    def delete(self):
        print("no sql statement deleted")
sql=SQLDatabase()
sql.insert()
sql.update()
sql.delete()
nosql=NoSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()