import pprint
import os

def Parsing(ID, ServerID):

    Txtfile_name = ID + '_' + ServerID

    #if os.path.exists('C:/Users/82102/Desktop/OIDC/parsing_test.txt'):             
    if os.path.exists("C:/Users/user/Desktop/test/%s.txt"%(Txtfile_name)):                    #배포용
        result = []
        
        #textfile = open("C:/Users/82102/Desktop/OIDC/parsing_test.txt", 'r')
        textfile = open("C:/Users/user/Desktop/test/%s.txt"%(Txtfile_name), 'r')              #배포용
        index = textfile.readlines()
        textfile.close()

        for i in range(len(index)):
            if "----------- SCAN SUMMARY -----------" in index[i+2]:
                break
            result.append(index[i+1].replace(' FOUND\n',''))

        pprint.pprint(result)

        virus_num = len(result)
        print("Virus 감염수 : %s"%virus_num)
    else :
        result = []
        virus_num = "파일이 없습니다."
        print(virus_num)

    return result

#00시가 지나 보안 검사 실행 후 검사 결과 파일이 있다면, 리스트(result)에 감염 바이러스 경로가 저장됨, virus_num 변수에 리스트 수(virus 수)를 계산하여 저장
#서버 추가 후 00시가 지나지 않아 검사 파일이 없다면, 리스트(result)는 비어있고, virus_num 변수에 "파일이 없습니다"라는 말이 저장됨