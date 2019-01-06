Title: VirtualBox in CentOS7構築
Date: 2016-02-01 00:00
Modified: 2016-02-01 00:00
Category: Tech
Tags: トイズクリエイション, ToysCreation, VirtualBox, CentOS7
Slug: virtualbox_in_centos7
Authors: ToysCreation.Inc morita
Summary: VirtualBox in CentOS7構築
Cover:



メモ：

VirtualBoxインストール
http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html?ssSourceSiteId=otnjp
各OSのVirtualBoxを選択、インストールはdmgとpkgをクリックしていけば完了します。




弊社では開発環境にVirtualBoxを利用しています。  
普段はVagrantにて構築することが多いですが、  
基本に帰るということで今回はisoイメージより最新のCentOS7のインストール手順を掲載します。  

1. CentOS7イメージをダウンロード  
サーバー用途なのでミニマルをインストール  
[https://wiki.centos.org/Download](https://wiki.centos.org/Download)  

2. VirtualBoxより新規をクリック画面の流れのまま進んでいきます。  
完了後、左に新規マシンが追加されます。  
設定・ネットワーク設定をクリック、割り当てをブリッジアダプターに変更しOKをクリックします。  

3. VirtualBox起動  
起動をクリックしディスク選択に先ほどダウンロードしたisoを選択してください。  

4. インストール設定  
画面のままで大丈夫です。言語「日本語選択」キーボード「US」など自分環境下に合わせて設定を行います。<br />  
各設定の細かい内容は省略しますが、以下2点は必ず行います。  
    1. デバイスを選択、そのまま完了をクリックします。  
    2. ネットワークを選択、イーサーネットをONにして完了をクリックします。  
設定を完了しインストール開始をクリックにてインストールが開始されます。  
インストール中にユーザー作成などができますので、状況に応じて作成します。  

5. インストール後、再起動が求められるので再起動をクリック  
黒い画面が立ち上がりますので、設定したユーザー名・パスワードにてログインすることを確認します。  

6. ネットワーク確認  
コマンドにて ip aaddr を入力 enp0s3 inetに表示されたIPが仮想マシン接続IPになります。  
ためしに、PCないターミナルにてSSHし接続できるか試してみてください。  


いかがでしょうか？  
このようにVirtualBoxとCentOS7を使えば簡単に仮想マシン内にCentOSを立ち上げることができました。  
次回はこの仮想マシン内にNginx・PHPを入れていきたいと思います。  
