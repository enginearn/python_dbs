# python_dbs

## Preparation

Install DBs on your machine locally or using docker.
Example docker version of these DBs preparations are below:

<details>

[docker-mysql](https://github.com/enginearn/docker-mysql-latest-jp)

[docker-mongodb](https://github.com/enginearn/docker-mongodb-latest)

[docker-postgresql](https://github.com/enginearn/docker-postgresql-latest)

</details>

## Install DB Packages

<details>
<summary>mysql</summary>

``` Powershell
pip install mysql
Collecting mysql
  Downloading mysql-0.0.3-py3-none-any.whl (1.2 kB)
Collecting mysqlclient
  Using cached mysqlclient-2.1.1-cp310-cp310-win_amd64.whl (178 kB)
Installing collected packages: mysqlclient, mysql
Successfully installed mysql-0.0.3 mysqlclient-2.1.1
```

</details>

<details>
<summary>pymongo dnspython</summary>

``` Powershell
pip install pymongo dnspython
Collecting pymongo
  Using cached pymongo-4.1.1-cp310-cp310-win_amd64.whl (365 kB)
Collecting dnspython
  Downloading dnspython-2.2.1-py3-none-any.whl (269 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 269.1/269.1 kB 4.2 MB/s eta 0:00:00
Installing collected packages: pymongo, dnspython
Successfully installed dnspython-2.2.1 pymongo-4.1.1
```

</details>

<details>
<summary>psycopg 3.x</summary>

``` PowerShell
pip install psycopg[binary]
Collecting psycopg[binary]
  Downloading psycopg-3.0.15-py3-none-any.whl (144 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 144.1/144.1 kB 1.4 MB/s eta 0:00:00
Collecting tzdata
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)
Collecting psycopg-binary==3.0.15
  Downloading psycopg_binary-3.0.15-cp310-cp310-win_amd64.whl (2.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.9/2.9 MB 1.3 MB/s eta 0:00:00
Installing collected packages: tzdata, psycopg-binary, psycopg
Successfully installed psycopg-3.0.15 psycopg-binary-3.0.15 tzdata-2022.1
```

</details>

## Connect to DB

This script connects to the DBs on each Docker container from your local PC.

<details>
<summary>MySQL</summary>

``` Python
def mysql_connect():
    try:
        mysql_cn = mysql.connect(user='root', password='secret', host='localhost', port=3307)
        print("Connected to MySQL!")
        return mysql_cn

    except mysql.Error as e:
        print(f"MySQL: {e}")
        return None
```

</details>

<details>
<summary>Mongdb</summary>

``` Python
def mongo_connect():
    try:
        client = pymongo.MongoClient("localhost", 27017)
        print("Connected to MongoDB!")
        return client

    except pymongo.errors.ConnectionFailure as e:
        print(e)
        return None
```

</details>

<details>
<summary>postgres</summary>

``` Python
def postgres_connect():
    try:
        psql_cn = psycopg.connect("user=postgres password=mysecretpassword port=5432 host=localhost")
        print("Connected to PostgreSQL!")
        return psql_cn

    except psycopg.Error as e:
        print(f"postgres: {e}")
        return None
```

</details>
