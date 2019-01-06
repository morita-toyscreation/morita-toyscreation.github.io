2月 25, 2016

CentOS7 in Redis




前回・前々回とCentOS7にPHP・MySQLをインストールしてきました。
最後にKey-Valueとして人気があるRedisをインストールします。
Redisはキャッシュとしての利用やPub/Subとしてのプッシュ通信などソーシャルゲーム開発では外せないソフトウェアです。

Redisインストール

1. リポジトリはremiにてインストール
PHP時にすでにインストール済み

2. インストール
# yum -y install redis

3. phpredisインストール
# yum -y install git
# git clone https://github.com/phpredis/phpredis.git
# yum --enablerepo=epel,remi,remi-php70 -y install php70-phpize
# /opt/remi/php70/root/usr/bin/phpize
# ./configure --with-php-config=/opt/remi/php70/root/usr/bin/php-config
# make && make install

4. 設定ファイル修正
# vi /etc/opt/remi/php70/php.ini

ファイル末尾に以下を追記

extension=redis.so
5. PHP再起動
# systemctl stop php70-php-fpm
# systemctl start php70-php-fpm

6. 自動起動設定
# systemctl enable redis

7. 起動
# systemctl start redis

8. 確認・コマンド実行
# redis-cli

Redis+PHP連携

1. テストコード

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set("dog","baw-baw");
$res = $redis->get("dog");
echo $res;
ブラウザにて baw-bawと表示されていればRedisインストールが完了です。
CentOS7 in Nginx,PHP,MariaDB,Redisと一般的なソーシャルゲームを作るのに必要な
開発環境についてまとめてみました。
基本はこの環境でこれらをチューンニング・拡張していくことで
秒間100万PVでも捌ける環境になります。