2月 15, 2016

CentOS7 in PHP7




前回に引き続き、CentOS7にソフトウェアをインストールしていきます。
今回はPHP7をインストールしてNginxと連携させます。

PHP7インストール

1. リポジトリインストール
# yum -y install epel-release
# wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
# rpm -ivh ./remi-release-7.rpm

2. PHPインストール
# yum -y --enablerepo=epel,remi,remi-php70 install php70

3. パス設定
# source /opt/remi/php70/enable
※ パス設定が存在するのでそのまま実行

4. PHPパッケージインストール
Nginx連携やその他必須なPHPパッケージをインストールします。
# yum -y --enablerepo=epel,remi,remi-php70
install php70-php-mcrypt php70-php-mbstring php70-php-fpm
php70-php-gd php70-php-devel php70-php-mysqlnd php70-phpize

その他、必要なパッケージは以下にて検索が可能です。
# yum --enablerepo=epel,remi,remi-php70 search php70

5. 自動起動設定
# systemctl enable php70-php-fpm

6. 起動
# systemctl start php70-php-fpm

Nginx・PHP7連携

ブラウザで確認するために、必要最低限の設定を行います。

1. conf設定（最低限ver)
# vi /etc/nginx/conf.d/default.conf

server {
listen 80;
server_name localhost;

#charset koi8-r;
#access_log /var/log/nginx/log/host.access.log main;

root /var/www;
index index.php index.html index.htm;

location / {
try_files $uri $uri/ /index.php?$query_string;
}

# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#
location ~ \.php$ {
root /var/www;
fastcgi_pass 127.0.0.1:9000;
fastcgi_index index.php;
fastcgi_param SCRIPT_FILENAME $document_root/$fastcgi_script_name;
include fastcgi_params;
}
}

2. 確認
以下ファイルを配置してブラウザにてphpinfo内容が表示されていればインストール完了です。

# vi /var/www/index.php

echo phpinfo();

その他、本番実装では以下のファイルをチューニングすることによって
パフォーマンスに影響を与えます。それは、また別の機会にでも説明したいと思います。

php.ini
/etc/opt/remi/php70/php.ini
www.conf
/etc/opt/remi/php70/php-fpm.d/www.conf

次はMariaDB（MySQL互換）をインストールしPHPと連携してみたいと思います。