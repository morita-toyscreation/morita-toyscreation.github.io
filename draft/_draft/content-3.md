9月 2, 2016

NginxでBasic認証




備忘録になります。Basic認証なので、この認証だけで安心ということはありませんが
管理画面認証などに入る前にさらにBasic認証などに利用します。

目次
1. .htpasswd 作成
2. Nginx設定ファイル修正

1. .htpasswd 作成
# htpasswd -c -b /etc/nginx/.htpasswd [ユーザ名] [パスワード]
2. Nginx設定ファイル修正
設定したいディレクトリに対してauth_basicを指定

# vi /etc/nginx/conf.d/default.conf
— サンプル

location /admin {
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/.htpasswd;
}
