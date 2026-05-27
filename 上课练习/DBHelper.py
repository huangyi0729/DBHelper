import pymysql
import time
class DBHelper:
    def __init__(self, host, user, pwd, db):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            database=db,
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        try:
            affected = self.cursor.execute(sql, params or ())
            self.conn.commit()
            return affected
        except Exception as e:
            self.conn.rollback()
            raise e

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


class UserManager:
    def __init__(self, db_helper: DBHelper):
        self.db = db_helper

    def add_user(self, username: str, email: str, phone: str) -> int:
        sql = "INSERT INTO users (username, email, phone) VALUES (%s, %s, %s)"
        try:
            self.db.execute(sql, (username, email, phone))
            self.db.cursor.execute("SELECT LAST_INSERT_ID()")
            last_id = self.db.cursor.fetchone()[0]
            return last_id
        except Exception as e:
            print(f"添加用户失败: {e}")
            return 0

    def get_user_by_id(self, user_id: int):
        sql = "SELECT user_id, username, email, phone FROM users WHERE user_id = %s"
        result = self.db.query(sql, (user_id,))
        return result[0] if result else None

    def update_user_email(self, user_id: int, new_email: str) -> bool:
        sql = "UPDATE users SET email = %s WHERE user_id = %s"
        try:
            affected = self.db.execute(sql, (new_email, user_id))
            return affected > 0
        except Exception as e:
            print(f"更新邮箱失败: {e}")
            return False

    def delete_user(self, user_id: int) -> bool:
        sql = "DELETE FROM users WHERE user_id = %s"
        try:
            affected = self.db.execute(sql, (user_id,))
            return affected > 0
        except Exception as e:
            print(f"删除用户失败: {e}")
            return False


if __name__ == '__main__':
    db = DBHelper('localhost', 'root', 'root', 'dianshang')
    user_mgr = UserManager(db)
    unique_email = f'wei_{int(time.time())}@example.com'
    new_id = user_mgr.add_user('hujian', unique_email, '15898387558')
    print(f"新用户ID: {new_id}")

    if new_id > 0:
        user = user_mgr.get_user_by_id(new_id)
        print(f"查询结果: {user}")
        if user_mgr.update_user_email(new_id, 'newemail@example.com'):
            print("邮箱更新成功")
        updated_user = user_mgr.get_user_by_id(new_id)
        print(f"更新后用户: {updated_user}")
        if user_mgr.delete_user(new_id):
            print("用户删除成功")
    else:
        print("用户添加失败，请检查邮箱是否唯一")

    db.close()