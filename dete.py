# __author : Ellis
# __date : 2018/9/21

from aip import AipOcr

APP_ID = '14257663'
API_KEY = '6lzhorFWdLGebPTein7K3Hyx'
SECRET_KEY = 'acDVkr2yUfcGbcY6nYgBCdLjAAdUOgDy'
aipOcr  = AipOcr(APP_ID, API_KEY, SECRET_KEY)


filePath ='C:\\Users\\95720\\Desktop\\1537763962(1).png'
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

result = aipOcr.basicAccurate(get_file_content(filePath), options)
#message = aipOcr.basicGeneral(get_file_content(filePath), options)
print(result)