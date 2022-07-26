import pymysql

def autosql(username):

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

    #사용자의 ID와 똑같이 ID, MetaData, UserGroup, HostGroup 생성해줄 예정 
    #입력받아야하는 것들
    ID = username
    lastname = '성민'
    firstname = '김'

    #기본키 생성할 때 이 번호부터 시작하기
    # 1.호스트 그룹
    sql = """select max(groupid) from hstgrp;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    hstgrp = select[0][0]+1
    #print(hstgrp)

    # 2. 유저 그룹
    sql = """select max(usrgrpid) from usrgrp;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    usrgrp = select[0][0]+1 # 이 번호부터 Query 작성 시에 사용하면 된다.
    #print(usrgrp)

    # 3. rights : 유저 그룹이 볼 수 있는 호스트 그룹 지정할 때 사용
    sql = """select max(rightid) from rights;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    rights = select[0][0]+1 # 이 번호부터 Query 작성 시에 사용하면 된다.
    #print(rights)

    # 4. 유저
    sql = """select max(userid) from users;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    users = select[0][0]+1 


    # 5. 유저그룹
    sql = """select max(id) from users_groups;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    users_groups = select[0][0]+1 

    # 6. 액션
    sql = """select max(actionid) from actions;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    actions = select[0][0]+1 


    # 7. condition
    sql = """select max(conditionid) from conditions;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    conditions = select[0][0]+1 
    #print(conditions)

    # 8. operations
    sql = """select max(operationid) from operations;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    operations = select[0][0]+1 
    #print(operations)

    # 9. opgroup
    sql = """select max(opgroupid) from opgroup;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    opgroup = select[0][0]+1 
    #print(opgroup)

    # 10. optemplate
    sql = """select max(optemplateid) from optemplate;"""
    cursors.execute(sql)
    select = list(cursors.fetchall())
    db.commit()
    optemplate = select[0][0]+1 
    #print(optemplate)

    #Hostgroup 생성
    param = (hstgrp, ID) # 튜플로 만들어야 sql문에 변수 대입식으로 활용 가능
    sql = """insert into hstgrp values(%s, %s, '0', '0'); """ #변수를 추가해주고 싶을 때 %s로 하며, param 튜플을 활용 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #Usergroup 생성
    param = (usrgrp, ID) # 튜플로 만들어야 sql문에 변수 대입식으로 활용 가능
    sql = """insert into usrgrp values(%s, %s, '0', '0', '0'); """ #변수를 추가해주고 싶을 때 %s로 하며, param 튜플을 활용 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #rights 생성
    param = (rights, usrgrp, hstgrp) # usergroup id, hostgroup id
    sql = """insert into rights values(%s, %s, 2, %s); """ #변수를 추가해주고 싶을 때 %s로 하며, param 튜플을 활용 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #Users 생성
    param = (users, ID, lastname, firstname) # usergroup id, hostgroup id
    sql = """insert into users values (%s, %s, %s, %s, '$2y$10$znsGAi9CNY8wKsHO9c0touImWcujmkGab39f4edlRzJ84zBcik/Dq', '', '0', '0', 'ko_KR', '30s', '1', 'default', '0', '', '0', '50'); """ #변수를 추가해주고 싶을 때 %s로 하며, param 튜플을 활용 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #users_groups 생성
    param = (users_groups, usrgrp, users) # usergroup id, hostgroup id
    sql = """insert into users_groups values (%s, %s, %s); """ #변수를 추가해주고 싶을 때 %s로 하며, param 튜플을 활용 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #actions 생성
    param = (actions, ID) # usergroup id, hostgroup id
    sql = """insert into actions values (%s, %s, '2', '0', '0', '1h', '', '1');""" 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #conditions 생성
    param = (conditions, actions, ID) # usergroup id, hostgroup id
    sql = """insert into conditions values (%s, %s, '24', '2', %s, ''); """ 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #operations 생성
    param = (operations, actions) # usergroup id, hostgroup id
    sql = """insert into operations values (%s, %s, '2', '0', '1', '1', '0', '0'); """ 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    param = (operations+1, actions)
    sql = """insert into operations values (%s, %s, '4', '0', '1', '1', '0', '0'); """ 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    param = (operations+2, actions)
    sql = """insert into operations values (%s, %s, '6', '0', '1', '1', '0', '0'); """ 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    param = (operations+3, actions)
    sql = """insert into operations values (%s, %s, '8', '0', '1', '1', '0', '0'); """ 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #opgroup 생성
    param = (opgroup, operations+1, hstgrp) 
    sql = """insert into opgroup values (%s, %s, %s); """ 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    #optemplate 생성
    param = (optemplate, operations+2) 
    sql = """insert into optemplate values (%s, %s, '10001'); """ 
    cursors.execute(sql, param)
    select = list(cursors.fetchall())
    db.commit()

    print('SQL 자동화 완료')
    return ID