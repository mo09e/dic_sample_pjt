# README
- サンプルのブログアプリケーションです。
- 使用方法をご確認の上、コマンドを実行するとアプリケーションを動かすことができます。

## バージョン
- django 3.0.4
- Python 3.9.7
- psycopg 2.8.6
___

## 使用方法
1. まずアプリケーションを任意の場所にクローンし、ディレクトリを移動します。
```
$ git clone git@github.com:mo09e/dic_sample_pjt.git
$ cd dic_sample_pjt
```
2. シークレットキーを準備します。
```
$ touch dic_sample_pjt/local_settings.py
$ python dic_sample_pjt/get_random_secret_key.py
SECRET_KEY = 'SECRET_KEYが生成されます'
```
3. ２で作成したシークレットキーを、`local_settings.py`にペーストします。

```python:dic_sample_pjt/local_settings.py
SECRET_KEY = '新しく生成されたSECRET_KEYをペースト'
```

3. PostgreSQLに接続し、下記のコマンドを実行してください。
```
$ psql postgres
postgres=# CREATE DATABASE dic_sample_pjt;
postgres=# CREATE USER django_user WITH PASSWORD 'password';
postgres=# \q
```
4. マイグレーションを実行してください。
```
$ python manage.py migrate
```
5. サーバーを立ち上げ、アプリケーションを起動してください。
```
$ python manage.py runserver
```
6. サーバーを起動させた状態で、以下のURLをコピーし、ブラウザのアドレスバーに貼り付けてください。
```
http://localhost:8000/blog/post_list
```