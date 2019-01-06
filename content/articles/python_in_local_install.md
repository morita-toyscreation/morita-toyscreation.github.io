Title: [Python] MacにPythonのローカル開発環境を構築  
Date: 2019-01-01 00:00  
Modified: 2019-01-01 00:00  
Category: Tech  
Tags: トイズクリエイション, ToysCreation, Python, ローカル開発環境  
Slug: python_in_local_install  
Authors: ToysCreation.Inc morita  
Summary: [Python] MacにPythonのローカル開発環境を構築  
Cover:  

**Xcodeインストール**
```ps1
$ sudo xcode-select --install
```

**Homebrewインストール**
```ps1
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

**Pythonインストール**  
※ pipなどのツール群も一緒にインストールしてくれるのでインストール
```ps1
$ brew install python
```

その他必要そうなソフトウェア
```ps1
$ brew install libevent
$ brew install xz
```

**pyenvインストール**
```ps1
$ brew install pyenv-virtualenv
```

pyenvにパスを通す
```ps1
$ vi ~/.bash_profile
	
export PYENV_ROOT=${HOME}/.pyenv
if [ -d "${PYENV_ROOT}" ]; then
export PATH=${PYENV_ROOT}/bin:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
fi
```

pyenvインストールリスト取得
```ps1
$ pyenv install -l
```

pyenvバージョンインストール  
※ 一旦2系、3系の最新をインストール
```ps1
$ pyenv install 2.7.14
$ pyenv install 3.63
```

**バージョン対応**

全体
```ps1
$ pyenv global [バージョン]
```

対象ディレクトリ以下
```ps1
$ eval "$(pyenv init -)"
$ pyenv local [バージョン]
$ pyenv shelll [バージョン]
```

**Virtualenvインストール**  
入れ方と使い方を確認、環境を汚さないために推奨

仮想環境作成
```ps1
$ pyenv virtualenv [バージョン] [仮想環境名]
$ pyenv virtualenv 3.6.3 virtualenvTest
```

仮想環境と開発ディレクトリ紐付け
```ps1
$ mkdir virtualenvTest
$ cd virtualenvTest
$ pyenv local virtualenvTest
```
