import pymysql

# 클라우드 DB에 접속. root 계정 이외의 계정을 생성

db = pymysql.connect(
    host='175.45.195.194',
    port=3306,
    user='dong',
    password='os123456',
    db='zabbix',
    charset='utf8'
)

cursors = db.cursor()

def hostlists(id):
    ID = id #리액트에서 로그인했을 경우에 username 정보를 넣어야 함

    param = (ID)
    sql = """select host from autoreg_host where host_metadata = (%s);"""
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()
    result = select

    post_list = []
    for i in range(len(result)):
        post_list.append(result[i][0])
    return post_list