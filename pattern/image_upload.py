import json
import os
import io
import requests
import psycopg2
import pymysql
import base64

# 连接到MySQL数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user="root",
    passwd="20020309",
    db="culture"
)
cursor = conn.cursor()

def process_image_url(image_url):
    # 查找 [1024] 的索引
    index = image_url.find('[1024]')
    # 如果找到了 [1024]
    if index != -1:
        # 移除 [1024]
        processed_url = image_url[:index] + image_url[index + 6:]
        return processed_url
    else:
        # 没有 [1024]，直接返回原始URL
        return image_url

# 图像文件夹路径
folder_path = '/Users/pengshirui/Desktop/pic'
json_path = '/Users/pengshirui/Desktop/culturemining/pattern/dpm-zhixiu-new.json'
# 遍历文件夹中的图像文件
i = 0
with open(json_path, 'r') as json_file:
    json_data = json.load(json_file)

for obj in json_data:
    i = i + 1
    print(i)
    # Extract the required fields from the JSON data
    id = obj['id']
    name = obj['name']
    category = obj['category']
    species = obj['species']
    url = obj['url']
    img = obj['data-img'][0]
    img = process_image_url(img)
    dynasty = obj['dynasty']
    content = obj['content']
    patterns = ' '.join(obj['patterns'])

    response = requests.get(img)
    img_bytes = response.content
    #print(img_bytes)
    #img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    # Insert the image and JSON data into the database
    cursor.execute('INSERT INTO pattern_patternbank (id, name, category, species, url, img, dynasty, content, patterns, img_bytes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, name, category, species, url, img, dynasty, content, patterns, img_bytes))
    conn.commit()

# 关闭数据库连接
conn.close()
