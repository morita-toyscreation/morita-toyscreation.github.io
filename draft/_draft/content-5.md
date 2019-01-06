8月 30, 2016

快適に開発するためのクライアント開発環境構築（Bower・Gulp・Less・TypeScript）




トイズクリエイションではゲーム開発に必要なティザーサイトや管理ツールなどの開発も受注しております。

ティザーサイトや管理ツールなどはゲーム本開発ではないので
どうしても開発環境に対して手を抜くことが多くなってしまいがちですが
管理ツールなどは運用・更新が入る部分でもあるのでしっかりと使いやすい開発環境を用意しておくことも重要かと考えています。

本記事では弊社で実際に利用したクライアント開発環境の構築方法に関して
備忘録的にご紹介しようと思います。

各項目の詳細や仕様などは省き、導入を端的にまとめたものになりますので
詳しく知りたい人は記事最下部にリンクを貼っておきますのでご参照ください。

新たなクライアント開発環境が必要の際にこのサイトを参考にしていただければと思っております！

目次
パッケージ管理 … Bower
コンパイル・ビルド … Gulp
CSS拡張言語 … Less
JavaScript拡張言語 … TypeScript
CSSフレームワーク … BootStrap
JSフレームワーク … JQuery
※ Angular/React関連の話は今回はいたしません。
Bower パッケージ管理 導入
1. homebrewでnode/npmとbowerインストール

# brew install node
# npm install bower -g
2. Bower設定
ディレクトリ作成

# mkdir test && cd test
# bower init
? name test
? description test
? main file index.js
? keywords test
? authors Morita Takashi &lt;z.takashi.morita@gree.net&gt;
? license MIT
? homepage
? set currently installed components as dependencies? Yes
? add commonly ignored files to ignore list? Yes
? would you like to mark this package as private which prevents it from being accidentally published to the registry? Yes
? Looks good? Yes
設定は結構適当、Looks good? Yesにて対象ディレクトリにbower.jsonが作成

3. Bowerインストール

# bower install jquery
# bower install bootstrap
Gulp コンパイル・ビルド 導入
1. Glupインストール

# npm install -g gulp
グローバルにも保存

# npm init
package.json作成

# npm install --save-dev gulp
2. 確認

# gulp -v
3. プラグイン追加

# npm install --save-dev gulp-concat
# npm install --save-dev gulp-rename
# npm install --save-dev gulp-uglify
# npm install --save-dev gulp-filter
# npm install --save-dev gulp-bower-files
# npm install --save-dev main-bower-files
4. gulpfile作成（サンプル）

# vi gulpfile.js
サンプル

var gulp = require('gulp');
gulp.task('hoge', function() {
console.log('HelloWorld!');
});
# gulp hoge
[14:27:29] Using gulpfile ~/Sites/test/gulpfile.js
[14:27:29] Starting ‘hoge’…
HelloWorld!
[14:27:29] Finished ‘hoge’ after 139 μs

Less CSS拡張言語 導入
1. Glupプラグイン追加

# npm install --save-dev gulp-less
# npm install --save-dev gulp-autoprefixer
# npm install --save-dev gulp-minify-css
2. CSS・LESSディレクトリ作成

# mkdir less && mkdir css
3. LESSサンプル作成

# cd less
# vi sample.less
サンプル（公式）

@base: #f938ab;
.box-shadow(@style, @c) when (iscolor(@c)) {
  box-shadow:         @style @c;
  -webkit-box-shadow: @style @c;
  -moz-box-shadow:    @style @c;
}
.box-shadow(@style, @alpha: 50%) when (isnumber(@alpha)) {
  .box-shadow(@style, rgba(0, 0, 0, @alpha));
}
.box {
  color: saturate(@base, 5%);
  border-color: lighten(@base, 30%);
  div { .box-shadow(0 0 5px, 30%) }
}
4. gulpfile作成

# vi gulpfile.js
var gulp = require('gulp');
var less = require('gulp-less');

gulp.task('css-compile', function() {
  return gulp.src('less/*.less')
    .pipe(less())
    .pipe(gulp.dest('css/'));
});
5. 実行
コマンド実行にてcss直下にsample.cssが出力されます。

# gulp css-compile
TypeScript JavaScript拡張言語 導入
1. TypeScript Glupプラグイン追加

# npm install typescript gulp-typescript --save-dev
2. ts・jsディレクトリ作成

# mkdir ts && mkdir js
3. TypeScriptサンプル作成

サンプル

class Greeter {
    constructor(public greeting: string) { }
    greet() {
        return this.greeting ;
    }
};
var greeter = new Greeter("Hello, world!");
document.body.innerHTML = greeter.greet();
4. gulpfile作成

# vi gulpfile.js
var gulp = require('gulp');
var typescript = require('gulp-typescript');

gulp.task('js-compile', function() {
  return gulp.src('ts/*.ts')
    .pipe(typescript())
    .pipe(gulp.dest('js/'));
});
5. 実行
コマンド実行にてjs直下にsample.jsが出力されます。

# gulp js-compile
参考サイト
公式サイト
Bower公式サイト
Gulp公式サイト
Less公式サイト
TypeScript公式サイト