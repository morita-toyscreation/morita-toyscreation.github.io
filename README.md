### ローカル確認
```
$ make devserver
```
ブラウザで確認できます。
http://localhost:8000/

### 開発サーバー停止
```
$ make stopserver
```

### MarkdownをHTMLに変換
```
$ pelican content -o output -s pelicanconf.py
```

### pelicanブランチをPush
```
$ git add .
$ git commit -m "first web site."
$ git push origin pelican
```

### Github Pages用デプロイ
```
$ ghp-import output -b master -m "Published."
```

### masterブランチをPush
```
$ git checkout master
$ git add .
$ git commit -m "Published."
$ git push origin master
```
