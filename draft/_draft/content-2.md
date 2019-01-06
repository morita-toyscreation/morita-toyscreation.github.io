9月 2, 2016

LAMP環境化でそれぞれの時間設定を揃える方法


備忘録になります。LAMPと書いていますが、CentOS7 / Nginx / MySQL（MariaDb） / PHP が対象です。
それぞれ、同じtimezoneに設定しないとデータベースの時間が意図せぬものになったりと不具合の原因になり兼ねないので
しっかりと対応しましょう。

目次
1. CentOS
2. PHP
3. MySQL
4. CentOS
CentOS
1. インストール

# yum install ntpdate
2. 日時を合わせる

# ntpdate ntp.nict.jp
# timedatectl set-timezone Asia/Tokyo
3. 確認

# timedatectl status
Local time: 金 2016-09-02 17:21:52 JST
Universal time: 金 2016-09-02 08:21:52 UTC
RTC time: 金 2016-09-02 08:21:51
Time zone: Asia/Tokyo (JST, +0900)
NTP enabled: yes
NTP synchronized: yes
RTC in local TZ: no
DST active: n/a
4. サービス登録

# systemctl start ntpd
# systemctl enable ntpd
PHP
※ PHPはあらかじめインストールされているものとします。

1. 設定

# vi /etc/opt/remi/php70/php.ini
[Date]
; Defines the default timezone used by the date functions
; http://php.net/date.timezone
date.timezone = "Asia/Tokyo"
2. PHP再起動

# systemctl reload php70-php-fpm
3. PHPタイムゾーン確認

# php70 -i | grep timezone
Default timezone = Asia/Tokyo
date.timezone = Asia/Tokyo; Asia/Tokyo

MySQL
1. 設定

# vi /etc/opt/remi/php70/php.ini
[mysqld]
default-time-zone = 'Asia/Tokyo'
2. MySQL再起動

# systemctl restart mariadb
3. 確認

# mysql -h xxx.com -P 3306 -u xxx -p
show variables like '%time_zone%';
+------------------+------------+
| Variable_name | Value |
+------------------+------------+
| system_time_zone | JST |
| time_zone | Asia/Tokyo |
+------------------+------------+