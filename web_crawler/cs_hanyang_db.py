import pymysql


db_name = "web_info_db"
table_name = "cs_hanyang"

#cs_hanyang table
# +--------+-------------+------+-----+---------+----------------+
# | Field  | Type        | Null | Key | Default | Extra          |
# +--------+-------------+------+-----+---------+----------------+
# | _id    | int(11)     | NO   | PRI | NULL    | auto_increment |
# | number | varchar(32) | NO   |     | NULL    |                |
# | title  | varchar(32) | NO   |     | NULL    |                |
# | date   | varchar(12) | NO   |     | NULL    |                |
# +--------+-------------+------+-----+---------+----------------+

# connection to mysql server
connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='wjs231100',
                                 charset='utf8')
cursor = connection.cursor()

# def create_table():

def commit():
    connection.commit()

def close():
    connection.close()

def get_latest():
    sql = "SELECT " + "* " + "FROM " + table_name + " ORDER BY _id " + "DESC " + "LIMIT 1;"
    # print(sql)
    exec_sql(sql)
    result = cursor.fetchall()
    ret = ()
    
    for r in result:
        # print(r[1].encode('utf-8'))
        # print(r[2].encode('utf-8'))
        # print(r[3])
        # ret.append(r[1].encode('utf-8'))
        # print(ret)
        ret = (r[1],r[2],r[3])
    return ret

def exec_sql(sql):
    cursor.execute("set names utf8")
    cursor.execute(sql)
    # result = cursor.fetchall()
    # for r in result:
    #     print(r)

def show_db():
    sql = "SHOW DATABASES"
    exec_sql(sql)

def create_table(): 
    # sql = "SELECT * FROM information_schema.tables \
    #        WHERE table_schema = 'cs_hanyang'\
    #        AND table_name = 'testtable' "
    sql = "CREATE TABLE " + table_name + " (\
                                   _id INT PRIMARY KEY AUTO_INCREMENT,\
                                   number VARCHAR(32) NOT NULL,\
                                   title VARCHAR(32) NOT NULL,\
                                   date VARCHAR(12) NOT NULL\
                                    ) ENGINE=INNODB;"
    exec_sql(sql)
    # sql = "DESCRIBE cs_hanyang"
    # exec_sql(sql)

def use_db():
    sql = "USE " + db_name
    exec_sql(sql)

def create_db():
    sql = "CREATE DATABASE " + db_name + " default CHARACTER SET UTF8"
    exec_sql(sql)

def init():
    create_db()
    use_db()
    create_table()

def insert(number, title, date):
    val = "VALUES(" + "'" +number + "'" +", " + "'" +title + "'" +", "  +str(date) +")"
    # print(val)
    sql = "INSERT INTO " + table_name + " (number, title, date) " + val
    print(sql)
    exec_sql(sql)
