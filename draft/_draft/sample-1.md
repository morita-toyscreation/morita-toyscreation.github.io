2月 10, 2016

CentOS7 in Nginx




前回はVirtualBoxにCentOS7をインストールしました。
CentOS7にNginx・PHP・MySQL・Redisをインストールしていきます。
今回はWebサーバー・Nginxをインストールしていきます。

1. 最低限の設定・更新作業
A. yum update にてソフトウェア更新
# yum -y update
yum -y install gcc make kernel-devel

B. selinux を無効
# vi /etc/selinux/config
SELINUX=disabled に変更

C. firewallを無効
# systemctl stop firewalld
# systemctl disable firewalld

※ selinux と firewallは開発環境のため無効にしています。
外部環境では行わないでください。

2. リポジトリインストール
# vi /etc/yum.repos.d/nginx.repo

[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/x86_64
gpgcheck=0
enabled=1

3. インストール
# yum -y install --enablerepo=nginx nginx

4. 自動起動設定
# systemctl enable nginx

5. 起動
# systemctl start nginx

6. ブラウザにて確認
IPはip adderにて確認、画面にてWelcome to nginx!と表示されれば設定完了です。
※ ネットワーク設定・確認はこちらを参考にしてください。

細かい設定やチューニングなど他にもやらなければいけないことは
沢山ありますが、簡易的に動かすのであればこれだけで完了です。
NginxはApacheより高速で設定が簡単といわれています。このさいに乗り換えてみてはいかがでしょうか？

次回はPHPをインストールして動作確認を行います。