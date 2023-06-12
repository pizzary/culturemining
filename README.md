culture-mining


- requirement
  ```
  pip install django
  pip install pymysql
  ``` 

- database
  - 创建数据库:
    ```create database english```
  - django连接数据库：在settings.py中设置为自己的database账号、密码
  - django迁移：
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
  - newspider.py连接数据库：在newspider.py中设置为自己的databse账号、密码# culture-mining
