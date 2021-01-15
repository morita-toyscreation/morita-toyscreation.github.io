Title: [Python] Pelicanのテーマ、プラグイン導入  
Date: 2021-01-11 00:00  
Modified: 2021-01-11 00:00  
Category: Tech  
Tags: トイズクリエイション, ToysCreation, Python, Pelican, GitHub    
Slug: pelican_in_v20210111  
Authors: ToysCreation.Inc morita  
Summary: [Python] Pelicanのテーマ、プラグイン導入  
Cover:  

**1. Pelican テーマ追加**  

Pelican は様々なテーマが提供されている。  
Pelican テーマ一覧をclone
 
```ps1
git clone --recursive https://github.com/getpelican/pelican-themes ../pelican-themes
```

pelicanconf.py に利用テーマを記載
今回は[Flex](https://github.com/alexandrevicenzi/Flex)を利用

```ps1
THEME = "../pelican-themes/Flex"  
```  
他にテーマごとに追加項目が変わるのでDocumentを参照  

**2. Pelican プラグイン追加**  

テーマ同様に様々なプラグインが提供されている。
Pelican プラグイン一覧をclone

```ps1
git clone --recursive https://github.com/getpelican/pelican-plugins ../pelican-plugins
```

pelicanconf.py に利用プラグインを記載

```ps1
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'i18n_subsites']  
```  
他にプラグインごとに追加項目が変わるのでDocumentを参照  

**3. Pelican テーマの変更** 

色やフォントを変更したい場合、pelicanconf.py にcustom.cssパスを追加

*content/static/custom.css*

```ps1
STATIC_PATHS = [..., 'static']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'
```  

**4. 追記**

2021年1月11日 時点 Makefileアップデートあり  
GitHubPages更新コマンド  

```ps1
make github
```  
