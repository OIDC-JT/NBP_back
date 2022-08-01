import boto3
import os

service_name = 's3'
endpoint_url = 'https://kr.object.ncloudstorage.com'
region_name = 'kr-standard'
access_key = 'm5bIyITDeH0kEW8K3sZ4'
secret_key = 'LS6N46NhCZmxOqbbsIDi42gQdbc1Lzk24qIyk12x'


def Security_batch(ID, OS, ServerID):
    #ID = 'jaechan'
    #OS = 'Centos'
    #ServerID = "server1"
    
    Txtfile_name = ID + '_' + ServerID
    object_name = Txtfile_name+'_test.bat'                                        #파일 이름
    object_name1 = Txtfile_name+'_clnt.c'                                         #파일 이름


    cfile_socket = """/* client.c */

    #include <stdio.h>
    #include <stdlib.h>
    #include <fcntl.h>
    #include <string.h>
    #include <unistd.h>
    #include <arpa/inet.h>
    #include <sys/socket.h>
    #include <sys/types.h>
    #include <netinet/in.h>

    #define IP "175.45.194.207"		//Django Server IP
    #define PORT 51					//Django Server Port

    void error_handling(char *message);
    int main(){

            int serv_sock, fd;
            int str_len, len;
            struct sockaddr_in serv_addr;
            char message[30], buf[BUFSIZ];
            FILE* file = NULL;

            char filename[1024] = "%s.txt";

            serv_sock = socket(PF_INET, SOCK_STREAM, 0);

            if(serv_sock == -1)
                    error_handling("socket() error");

            memset(&serv_addr, 0, sizeof(serv_addr));
            serv_addr.sin_family=AF_INET;
            serv_addr.sin_addr.s_addr=inet_addr(IP);
            serv_addr.sin_port=htons(PORT);

            if(connect(serv_sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))==-1)
                    error_handling("connect() error!");

            str_len=read(serv_sock, message, sizeof(message)-1);

            if(str_len==-1)
                    error_handling("read() error!");
            printf("Message from server: %%s \\n", message);

            // jpg
            size_t fsize, nsize = 0;
            size_t fsize2;

        /* 전송할 파일 이름을 작성합니다 */
            file = fopen("%s.txt" /* 파일이름 */, "rb");
            send(serv_sock, &filename, 1024, 0);		//파일 이름 보내기

        /* 파일 크기 계산 */
        // move file pointer to end
            fseek(file, 0, SEEK_END);
            // calculate file size
            fsize=ftell(file);
            // move file pointer to first
            fseek(file, 0, SEEK_SET);

            // send file contents
            while (nsize!=fsize) {
                    // read from file to buf
                    // 1byte * 256 count = 256byte => buf[256];
                    int fpsize = fread(buf, 1, 256, file);
                    nsize += fpsize;
                    send(serv_sock, buf, fpsize, 0);
            }

            fclose(file);
            close(serv_sock);
            return 0;
    }

    void error_handling(char *message){
            fputs(message, stderr);
            fputc('\\n', stderr);
            exit(1);
    }"""%(Txtfile_name, Txtfile_name)

    Centos ='#!/bin/bash \nsetsebool -P antivirus_can_scan_system 1 \nyum install -y epel-release \nyum install -y clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd \ncp /usr/share/doc/clamd.conf /etc/clamd.d/ \nsed -i -e \"s/^Example/#Example/\" /etc/clamd.d/clamd.conf \nsed -i -e \"s/^Example/#Example/\" /etc/clamd.d/scan.conf \nsed -i -e \"s/^Example/#Example/\" /etc/freshclam.conf \nfreshclam \necho \"[Unit]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Description = freshclam scanner\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"After = network.target\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"[Service]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Type = forking\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"ExecStart = /usr/bin/freshclam -d -c 4\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Restart = on-failure\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"PrivateTmp = true\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"RestartSec = 20sec\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"[Install]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"WantedBy=multi-user.target\" >> /usr/lib/systemd/system/clam-freshclam.service \nsystemctl enable clam-freshclam \nsystemctl enable clamd@scan \nsystemctl start clam-freshclam \nsystemctl start clamd@scan \nsystemctl status clam-freshclam \nsystemctl status clamd@scan \necho \"#!/bin/sh\" > /usr/local/bin/clamscan.sh \necho "SDATE=$(date \"+%%%%Y-%%%%m-%%%%d %%%%H:%%%%M:%%%%S\")\" >> /usr/local/bin/clamscan.sh \necho \"echo $\'Start Date :\' $SDATE > /root/%s.txt\" >> /usr/local/bin/clamscan.sh \necho \"clamscan -ri / >> /root/%s.txt\" >> /usr/local/bin/clamscan.sh \nchmod 755 /usr/local/bin/clamscan.sh \ncat <(crontab -l) <(echo \"00 00 * * * /usr/local/bin/clamscan.sh\") | crontab - \ngcc %s_clnt.c -o %s_clnt \nmv %s_clnt /root \ncat <(crontab -l) <(echo \"10 00 * * * /root/%s_clnt\") | crontab -'%(Txtfile_name, Txtfile_name, Txtfile_name, Txtfile_name, Txtfile_name, Txtfile_name) #배포용
    #Centos ='#!/bin/bash \nsetsebool -P antivirus_can_scan_system 1 \nyum install -y epel-release \nyum install -y clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd \ncp /usr/share/doc/clamd.conf /etc/clamd.d/ \nsed -i -e \"s/^Example/#Example/\" /etc/clamd.d/clamd.conf \nsed -i -e \"s/^Example/#Example/\" /etc/clamd.d/scan.conf \nsed -i -e \"s/^Example/#Example/\" /etc/freshclam.conf \nfreshclam \necho \"[Unit]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Description = freshclam scanner\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"After = network.target\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"[Service]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Type = forking\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"ExecStart = /usr/bin/freshclam -d -c 4\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Restart = on-failure\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"PrivateTmp = true\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"RestartSec = 20sec\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"[Install]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"WantedBy=multi-user.target\" >> /usr/lib/systemd/system/clam-freshclam.service \nsystemctl enable clam-freshclam \nsystemctl enable clamd@scan \nsystemctl start clam-freshclam \nsystemctl start clamd@scan \nsystemctl status clam-freshclam \nsystemctl status clamd@scan \necho \"#!/bin/sh\" > /usr/local/bin/clamscan.sh \necho "SDATE=$(date \"+%%%%Y-%%%%m-%%%%d %%%%H:%%%%M:%%%%S\")\" >> /usr/local/bin/clamscan.sh \necho \"echo $\'Start Date :\' $SDATE > /root/%s.txt\" >> /usr/local/bin/clamscan.sh \necho \"clamscan -ri / >> /root/%s.txt\" >> /usr/local/bin/clamscan.sh \nchmod 755 /usr/local/bin/clamscan.sh \ncat <(crontab -l) <(echo \"00 00 * * * /usr/local/bin/clamscan.sh\") | crontab - \ngcc %s_clnt.c -o %s_clnt \ncat <(crontab -l) <(echo \"10 00 * * * /root/%s_clnt\") | crontab -'%(Txtfile_name, Txtfile_name, Txtfile_name, Txtfile_name, Txtfile_name) #연구 중인 batch 파일
    #Centos ='#!/bin/bash \nsetsebool -P antivirus_can_scan_system 1 \nyum install -y epel-release \nyum install -y clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd \ncp /usr/share/doc/clamd.conf /etc/clamd.d/ \nsed -i -e \"s/^Example/#Example/\" /etc/clamd.d/clamd.conf \nsed -i -e \"s/^Example/#Example/\" /etc/clamd.d/scan.conf \nsed -i -e \"s/^Example/#Example/\" /etc/freshclam.conf \nfreshclam \necho \"[Unit]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Description = freshclam scanner\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"After = network.target\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"[Service]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Type = forking\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"ExecStart = /usr/bin/freshclam -d -c 4\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"Restart = on-failure\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"PrivateTmp = true\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"RestartSec = 20sec\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"[Install]\" >> /usr/lib/systemd/system/clam-freshclam.service \necho \"WantedBy=multi-user.target\" >> /usr/lib/systemd/system/clam-freshclam.service \nsystemctl enable clam-freshclam \nsystemctl enable clamd@scan \nsystemctl start clam-freshclam \nsystemctl start clamd@scan \nsystemctl status clam-freshclam \nsystemctl status clamd@scan \necho \"#!/bin/sh\" >> /usr/local/bin/clamscan.sh \necho "SDATE=$(date \"+%%%%Y-%%%%m-%%%%d %%%%H:%%%%M:%%%%S\")\" > /usr/local/bin/clamscan.sh \necho \"echo $\'Start Date :\' $SDATE > /root/%s.txt\" >> /usr/local/bin/clamscan.sh \necho \"clamscan -ri /root >> /root/%s.txt\" >> /usr/local/bin/clamscan.sh \nchmod 755 /usr/local/bin/clamscan.sh \ncat <(crontab -l) <(echo \"00 00 * * * /usr/local/bin/clamscan.sh\") | crontab - \ngcc %s_clnt.c -o %s_clnt \ncat <(crontab -l) <(echo \"10 00 * * * /root/%s_clnt\") | crontab -'%(Txtfile_name, Txtfile_name, Txtfile_name, Txtfile_name, Txtfile_name)

    if OS =='Centos':
        OS = Centos

    f = open(object_name,'w')
    f.write(OS)
    f.close

    f = open(object_name1, 'w')
    f.write(cfile_socket)
    f.close()


    if __name__ == "__main__":                                          #NBP S3 Upload Code
        s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key)

        bucket_name = 'oidc-security'

        #local_file_path = 'C:/Users/82102/Desktop/OIDC/'+object_name        #local 위치 
        local_file_path = '/root/'+object_name                              #서버상 위치(배포용)

        #local_file_path1 = 'C:/Users/82102/Desktop/OIDC/'+object_name1                #local 위치 
        local_file_path1 = '/root/'+object_name1                                      #서버상 위치(배포용)

        s3.upload_file(local_file_path, bucket_name, object_name, ExtraArgs={'ACL':'public-read'})
        s3.upload_file(local_file_path1, bucket_name, object_name1, ExtraArgs={'ACL':'public-read'})
        
        if os.path.exists(local_file_path1):                                #local에 저장한 file 삭제
            os.remove(local_file_path1)

        if os.path.exists(local_file_path):                              	#local에 저장한 file 삭제
            os.remove(local_file_path)