import boto3
import os

service_name = 's3'
endpoint_url = 'https://kr.object.ncloudstorage.com'
region_name = 'kr-standard'
access_key = 'm5bIyITDeH0kEW8K3sZ4'
secret_key = 'LS6N46NhCZmxOqbbsIDi42gQdbc1Lzk24qIyk12x'

def batch(ID, OS, ServerID):

    Centos7 = '#!/bin/bash \nrpm -Uvh http://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm \nyum -y install zabbix-agent zabbix-sender \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.194.199\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.194.199:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ServerID)
    Centos6 = '#!/bin/bash \nrpm -Uvh https://repo.zabbix.com/zabbix/5.0/rhel/6/x86_64/zabbix-release-5.0-1.el6.noarch.rpm \nyum -y install zabbix-agent zabbix-sender \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.194.199\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.194.199:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ServerID)
    Ubuntu2004 = '#!/bin/bash \nwget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+focal_all.deb \ndpkg -i zabbix-release_5.0-1+focal_all.deb \napt update \napt install zabbix-agent -y \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.194.199\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.194.199:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ServerID)
    Ubuntu1804 = '#!/bin/bash \nwget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+bionic_all.deb \ndpkg -i zabbix-release_5.0-1+bionic_all.deb \napt update \napt install zabbix-agent -y \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.194.199\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.194.199:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ServerID)
    Ubuntu1604 = '#!/bin/bash \nwget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+xenial_all.deb \ndpkg -i zabbix-release_5.0-1+xenial_all.deb \napt update \napt install zabbix-agent -y \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.194.199\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.194.199:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ServerID)


    if OS == 'Centos7':
        OS = Centos7
    elif OS == 'Centos6':
        OS = Centos6
    elif OS == 'Ubuntu2004':
        OS = Ubuntu2004   
    elif OS == 'Ubuntu1804':
        OS = Ubuntu1804  
    elif OS == 'Ubuntu1604':
        OS = Ubuntu1604                

    f = open('%s.bat'%ID, 'w')
    f.write(OS)
    f.close()                                                           #local에 batch 파일 저장
                                              #NBP S3 Upload Code
    s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key)
    bucket_name = 'oidc'
    object_name = '%s.bat'%ID                                       #파일 이름(파일명 : ID)
    local_file_path = 'C:/Users/user/Desktop/NBP_back/cloud/%s.bat'%ID      #local 위치 
    #local_file_path = '/root/%s.bat'%ID                             #서버상 위치

    s3.upload_file(local_file_path, bucket_name, object_name, ExtraArgs={'ACL':'public-read'})
    
    if os.path.exists(local_file_path):                              #local에 저장한 file 삭제
        os.remove(local_file_path)

    #서버에서 agent 설치하는 법(metadata는 id로 설정되있음)
    #1. 서버에서 curl -O(centos), wget(ubuntu) 's3 url' 을 입력하여 bat 파일 다운로드
    #2. chmod 755 'bat file명' -->bat file 권한을 access 할 수 있게 변경
    #3. ./'file명'으로 실행(agent 설치&설정)