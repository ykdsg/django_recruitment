DRF-序列化 相关demo练习
https://q1mi.github.io/Django-REST-framework-documentation/tutorial/1-serialization_zh/
https://www.w3cschool.cn/lxraw/lxraw-8kq335ob.html

启动之后可以访问：
http://127.0.0.1:8000/snip/snippets/


删除数据库并重新开始。
rm -f tmp.db db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate