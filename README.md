# Python DB sample

To install dependencies:
```
pip install -r requirememts.txt
```

To start mysql:
```
export MYSQL_ROOT_PASSWORD=MYSQL_ROOT_PASSWORD
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD -p 3306:3306 -p 33060:33060 -d mysql:8.0.13
```

# Documentation

https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/
https://docs.sqlalchemy.org/en/latest/core/engines.html
