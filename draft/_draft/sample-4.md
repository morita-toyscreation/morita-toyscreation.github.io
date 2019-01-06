2月 20, 2016

CentOS7 in MariaDB




前回はPHPをインストールしてNginxと連動してみました。
今回はMariaDB（MySQL互換RDS）をインストールして
PHPとMariaDB連携を行いたいと思います。

MariaDBインストール

1. リポジトリ追加
# vi /etc/yum.repos.d/mariadb.repo

[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.0/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
2. インストール
# yum -y install MariaDB-devel MariaDB-client MariaDB-server

3. 自動起動設定
# systemctl enable mysql

4. 起動
# systemctl start mysql

インストールはこれで完了です。
次にPHP連携を行います。

MariaDB+PHP連携

1. 仮データベース作成
# mysql -u root

2. ユーザー作成

> create user toys;
> set password for toys = password('Toys2016');
> grant all PRIVILEGES ON *.* TO toys@'%';
> grant all PRIVILEGES ON *.* TO toys@'localhost' identified by 'Toys2016';
※ ID/PWDは各々自由に入力してください。

3. DB作成

> create database toys_test;
> create table toys_test.test(id int);
> insert into toys_test.test value (1),(2),(3);
4. パッケージ追加
# yum --enablerepo=epel,remi,remi-php70 -y install php70-php-mysqlnd

5. PHPサンプル実行

<?php

$mysqli = new mysqli('localhost', 'toys', 'Toys2016', 'toys_test');

if ($mysqli->connect_error) {
    die('Connect Error (' . $mysqli->connect_errno . ') '
            . $mysqli->connect_error);
}

$sql = "SELECT id FROM toys_test.test";
if ($result = $mysqli->query($sql)) {
    while ($row = $result->fetch_assoc()) {
        echo $row["id"] . "<br>";
    }
    $result->close();
}
6. 動作確認
ブラウザにて1,2,3と表示されると完了です。

以上でMariaDBを使えるようになりました。
パフォーマンスチューニングや冗長化（マルチマスタ化）などの設定をしないと
本番環境下では使えませんが開発環境下ではこれで問題ありません。
チューニング等はまた別の機会に説明したいと思います。

※ チューニングファイル
vi /etc/my.cnf.d/server.cnf