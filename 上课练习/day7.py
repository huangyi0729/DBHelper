import pymysql
# try:
#     conn = pymysql.connect(host='localhost', user='root', password='root', db='school')
#     cursor=conn.cursor()#创建游标
#     cursor.execute("SELECT * FROM students")
#     res=cursor.fetchall()#获取结果
#     print(res)
# except pymysql.MySQLError as e:
#     print(e)
# finally:
#     #释放资源
#     cursor.close()
#     conn.close()

# excute(sql,args):执行单条SQL，args为参数元组/字典
# excutemany(sql,args):批量执行SQL语句
# fetchone()/fetchall():获取单行/所有结果
# rowcount():只读属性，返回受影响行数

# conn=pymysql.connect(host='localhost', user='root', password='root', db='company')
# cursor=conn.cursor()
# cursor.execute("SELECT * FROM employees WHERE salary BETWEEN 8000 AND 10000")
# res=cursor.fetchall()
# print(res)
# cursor.close()
# conn.close()

# conn=pymysql.connect(host='localhost', user='root', password='root', db='company')
# cursor=conn.cursor()
# sql="INSERT INTO employees (emp_name,salary) VALUES ('钱九',18000)"
# cursor.execute(sql)
# sql1="SELECT * FROM employees"
# cursor.execute(sql1)
# res=cursor.fetchall()
# print(res)
# conn.commit()
# print(f"插入成功，影响行数：{cursor.rowcount}")

# conn=pymysql.connect(host='localhost',user='root',password='root',db='company')
# cursor=conn.cursor()
# sql="UPDATE employees SET salary=%s WHERE emp_name=%s"
# cursor.execute(sql,(20000,'张三'))
# cursor.execute("SELECT * FROM employees")
# res=cursor.fetchall()
# print(res)
# conn.commit()

# conn=pymysql.connect(host='localhost',user='root',password='root',db='company')
# cursor=conn.cursor()
# cursor.execute("DELETE FROM employees WHERE emp_name='钱九'")
# cursor.execute("SELECT * FROM employees")
# res=cursor.fetchall()
# print(res)
sql1 = "CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20) NOT NULL,gender ENUM('男','女'),phone VARCHAR(20))"
sql2 = "INSERT INTO user (name, gender, phone) VALUES ('xiaoming','男','138'), ('linxue','女','139'), ('wuhan','男','137'),('hujian','男',158),('tangshan','女',179)"
sql3 = "SELECT * FROM user WHERE gender = '男'"
sql4 = "UPDATE user SET phone = %s WHERE name = %s"
sql5 = "DELETE FROM user WHERE id = 3"
try:
    conn=pymysql.connect(host='localhost',user='root',password='root',db='company')
    cursor=conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS user")
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4,('079','linxue'))
    cursor.execute(sql5)
    cursor.execute("SELECT * FROM user")
    res=cursor.fetchall()
    print(res)
    conn.commit()
except pymysql.MySQLError as e:
    conn.rollback()
    print(e)
finally:
    cursor.close()
    conn.close()
