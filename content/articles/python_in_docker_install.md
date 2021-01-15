Title: [Python] DockerにPython + Flask環境を構築  
Date: 2021-01-15 00:00  
Modified: 2021-01-15 00:00  
Category: Tech  
Tags: トイズクリエイション, ToysCreation, Docker, Python, Flask
Slug: python_in_docker_install  
Authors: ToysCreation.Inc morita  
Summary: [Python] DockerにPython + Flask環境を構築  
Cover:  

[週末ハッカソン](https://twitter.com/hashtag/%E9%80%B1%E6%9C%AB%E3%83%8F%E3%83%83%E3%82%AB%E3%82%BD%E3%83%B3) で
WEBサイトを作ろうと思いDockerにPython + Flask環境を構築した

**ダウンロード・インストール**  

Get Docker for Macからダウンロード  
[https://docs.docker.com/docker-for-mac/install/]()

ダウンロードしたDocker.dmgを展開してインストール完了  

インストール後にチュートリアル開始    
NEXT STEP を押していき動作確認  

**Python + Flask環境**    

Dockerfile  
```Dockerfile
FROM python:3.7.4

WORKDIR /app
ADD . /app

RUN apt-get update && apt-get clean;

RUN pip install -r requirements.txt

ENV TZ = "Asia/Tokyo"
ENV FLASK_APP /app/app.py
ENV PYTHONPATH $PYTHONPATH:/app

ENV PORT 8080
EXPOSE 8080

CMD ["python", "app.py"]
```

サンプル用アプリ  
コードの中身が知りたい方は[Document](https://flask.palletsprojects.com/en/1.1.x/)を参照してください。  
```HTML
weekend-hackathon/  
|-- app  
|   |-- views  
|   |	 `-- sample.py  
|   `-- __init__.py  
|-- app.py  
|-- Dockerfile  
`-- requirements.txt  
```

*weekend-hackathon/requirements.txt*  
```HTML
Flask==1.1.2
```

*weekend-hackathon/app/views/sample.py*  
```Python
from flask import Blueprint

sample = Blueprint("sample", __name__)


@sample.route("/")
def index():
    print("sample.index")
    return "sample.index"

```

*weekend-hackathon/app/\_\_init\_\_.py*  
```Python
from flask import Flask
from app.views.sample import sample


def get_app():
    app = Flask(__name__)
    _register_blueprint(app)
    return app


def _register_blueprint(app):
    app.register_blueprint(sample)

```

*weekend-hackathon/app.py*  

```Python
import app

app = app.get_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```

**Docker ビルド**
```
$ docker build -t weekend-hackathon .
```

**Flask起動**
```
$ docker run --name weekend-hackathon -p 8080:8080 -v ~/Sites/weekend-hackathon/:/app -it --rm weekend-hackathon
```

http://localhost:8080/にアクセス  
`sample.index` が表示される。


**参考コマンド**  

1. イメージ確認 : ```docker images```  
2. コンテナ確認 : ```docker ps```  
3. コンテナ確認（停止） : ```docker ps -a```  
4. コンテナ起動 : ```docker start xxxxx```  
5. コンテナ接続 : ```docker exec -it xxxxx /bin/bash```    
6. コンテナ停止 : ```docker stop xxxxx```  
7. コンテナ削除 : ```docker rm xxxxx```  
8. イメージ削除 : ```docker rmi xxxxx```  
