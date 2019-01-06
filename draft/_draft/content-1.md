9月 5, 2016

Nginxパフォーマンスチューニング（設定ファイル最適化）

トイズクリエイションではPHPアプリケーションのウェブサーバーとしてNginxを利用しています。
Nginxは軽量・高速に動作すると言われており、ゲームのようなパフォーマンスを求められる環境でよく利用されています。
今回はNginx設定ファイルの最適化を紹介していきたいと思います！

1. Nginx設定ファイル変更
# vi /etc/nginx/nginx.conf
2. Nginx設定ファイル参考
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log;
pid        /var/run/nginx.pid;

worker_rlimit_nofile 1024;

events {
    worker_connections  1024;
    multi_accept on;
    use epoll;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile	on;
    tcp_nopush	on;

	server_tokens   off;

	gzip  on;
	gzip_types text/css text/javascript;

    include /etc/nginx/conf.d/*.conf;
}
3. 設定紹介
worker_processes … CPUコア数に合わせます。
CPUコア数確認

# grep processor /proc/cpuinfo | wc -l
1
worker_rlimit_nofile … ワーカプロセスが同時に使えるファイル数です。サーバの最大プロセス数を設定します。
最大プロセス数確認

# ulimit -n
1024
worker_connections … ワーカー最大同時接続数
worker_processes×worker_connections を設定します。
今回の場合は 1*1024 で1024を設定します。

multi_accept … リクエストを同時受付

use epoll … I/O イベント通知機能、selectなど選択できますがepollを利用

tcp_nopush … レスポンスヘッダとファイル内容をまとめて送信

gzip on … gzip圧縮

gzip_types … gzip圧縮するコンテンツ追加

以上、Nginxを利用する際に参考にしてみてください！