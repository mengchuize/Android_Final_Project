import base64picture
import mysql.connector
import json
mydb = mysql.connector.connect(
    host="localhost", user='root', password='123456', database='androidprj')


#获得users
def getdbuser():
    conn = mydb.cursor()
    sql = "select * from user"
    conn.execute(sql)
    result = conn.fetchall()
    conn.close()
    jsondata=[]
    for user in result:
        data={}
        data['UserID']=str(user[0])
        data['UserName']=str(user[1])
        data['UserAge']=str(user[2])
        data['UserSex']=str(user[3])
        data['UserAddress']=str(user[4])
        data['UserImage']=base64picture.convert(str(user[5]))
        jsondata.append(data)
        jsondatas=json.dumps(jsondata,ensure_ascii=False)
    return jsondatas

#获得Photo
def getdbphoto():
    conn = mydb.cursor()
    sql = "select * from photo"
    conn.execute(sql)
    result = conn.fetchall()
    conn.close()
    jsondata = []
    for photo in result:
        data = {}
        data['PhotoID'] = str(photo[0])
        data['UserName'] = str(photo[1])
        data['PhotoPath'] = str(photo[2])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas

#获得Video
def getdbvideo():
    conn = mydb.cursor()
    sql = "select * from video"
    conn.execute(sql)
    result = conn.fetchall()
    conn.close()
    jsondata = []
    for video in result:
        data = {}
        data['VideoID'] = str(video[0])
        data['videoPath'] = str(video[1])
        data['userName'] = str(video[2])
        data['videoLove'] = str(video[3])
        data['videoMessage'] = str(video[4])
        data['videoShare'] = str(video[5])
        data['videoDesc'] = str(video[6])
        data['imagebase64'] = base64picture.convert(str(video[7]))
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas