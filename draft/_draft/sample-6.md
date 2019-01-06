2月 29, 2016

VirtualBox共有フォルダ設定




VirtualBoxで開発する際にファイル変更を即時、
VirtualBoxに反映する方法として共有フォルダーを利用する方法があります。
共有フォルダーを設定するとMacやWinで好きなエディターでプログラミングすることができます。

1. VirutalBoxにて共有フォルダー設定を行います。
マウントしたいディレクトリを選択します。
スクリーンショット 2016-03-20 17.26.33

2. Guest Additionsのインストール
まず、メニューの[デバイス]から[Guest Additionsのインストール]を選択。
ディレクトリにマウントする。
# mkdir /mnt/cdrom
# mount -r /dev/cdrom /mnt/cdrom

3. VBoxLinuxAdditions.runを実行する。
# yum -y install bzip2
# sh /mnt/cdrom/VBoxLinuxAdditions.run
# umount /mnt/cdrom
※ bzip2が必要なのでインストールしていない場合は追加でインストール

4. 対象ディレクトリを作成
# mkdir /home/toys/sociagate/www
# mount -t vboxsf sociagate /home/toys/sociagate/www
※ 各々必要な環境下に用意してください。

5. 起動時に自動マウントするように設定
現状ですと再起動時にマウントが外れてしまうため
rc.localに上記のマウントコマンドを記入します。

# chmod u+x /etc/rc.local
# vi /etc/rc.local

mount -t vboxsf sociagate /home/toys/sociagate/www
ローカル・ディレクトリにファイルを配置してみてください、
設定したディレクトリにファイルが増えていれば設定完了です。