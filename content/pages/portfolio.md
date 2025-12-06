Title: 開発実績
Date: 2018-03-25 00:00
Modified: 2018-03-25 00:00
Category: Pages
Tags: トイズクリエイション, ToysCreation, ポートフォリオ, PORTFOLIO
Slug: portfolio
Authors: ToysCreation.Inc morita
Summary: トイズクリエイションポートフォリオ
Order: 3

## 自社製品開発

### [プロニチ（プログラミング新聞）](https://prtimes.jp/main/html/rd/p/000000003.000075067.html) ※サービス終了 
### [Sociagate（ソシャゲート）](https://www.value-press.com/pressrelease/175565) ※サービス終了
### [ストーリー型将棋指し育成ゲーム「棋士プロ〜将棋めし編〜」](/kishipro.html#kishipro)

## 受託開発

<!-- 開発実績 -->
<style>
.works {
    border: solid 1px #585378;
    padding: 10px;
    margin-bottom: 10px;
    background-color: #FFF;
}
.works h3 {
    font-size: 1.2em;
}
</style>

<div class="works">

<h3>SNSマルチプラットフォーム対応・大規模データ分析基盤の構築</h3>

<p>
YouTube・Instagram・TikTok等の外部プラットフォームから取得する膨大なクリエイターデータの収集・統合を行うデータ基盤構築プロジェクトに、エンジニアとして参画。 
Apache Airflowによるワークフローのオーケストレーションと、Cloud Dataflow (Apache Beam) を用いた分散処理を組み合わせ、
高スループットかつ耐障害性の高いETLパイプラインを設計・実装しました。 
また、BigQueryを中心としたDWHの最適化を行い、社内BIツールでのレポート作成やデータ分析業務の高速化・安定化を実現しています。
<br /><br />

担当工程：  <br />
- パイプライン設計: Airflowを用いた複雑な依存関係を持つデータ処理フローの自動化と監視体制の構築<br />
- 分散処理実装: Apache Beamにより、非構造化データのクレンジングおよび正規化処理を並列化・高速化<br />
- データ活用: 社内向け分析レポートの自動生成およびKPI可視化の推進<br />
</p>

<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">UUUM株式会社 </td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;">社内システム</td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">12ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">
プログラム言語：Python<br />
DB：BigQuery インフラ：GCP ツール：Apache Beam, Airflow DAGs, Git/GitHub
        </td>
    </tr>
</table>

</div>

<div class="works">

<h3>不動産営業支援システム（SFA）の検索基盤高速化とアーキテクチャ刷新</h3>

<p>
不動産営業担当者が利用する営業支援ツール「イエリーチSales」のフルスタック開発を担当。 
膨大な顧客データや物件情報を扱う中でボトルネックとなっていた検索機能に対し、
クエリの最適化やインデックス設計の見直しを実施。
検索レスポンスを劇的に改善し、営業活動の効率化（DX）に貢献しました。 
また、機能拡張に耐えうるようシステム全体のリファクタリングを主導し、保守性の高いコードベースへの移行を実現しています。
<br /><br />

担当工程：  <br />
検索パフォーマンス改善: OpenSearchを導入し複雑な条件検索におけるDB負荷を軽減し、レスポンスタイムを短縮<br />
技術的負債の解消: 複雑化した営業ロジックを整理し、拡張性の高い設計へリファクタリング<br />
フルスタック対応: インフラ設定からUI実装まで、システム全域の課題解決をリード<br />
</p>

<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">株式会社ネクサスエージェント </td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;">社内システム</td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">18ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">
プログラム言語：Python フレームワーク：Django <br />
DB：MySQL,Redis,OpenSearch インフラ：AWS ツール：Git/GitHub
        </td>
    </tr>
</table>

</div>



<div class="works">

<h3>マブラヴ：ディメンションズ</h3>

<p>
DAU100万人を想定した負荷テストの実施、シナリオ〜インフラ構築の作成、その後のパフォーマンスチューニングを行いました。
また、AWS環境下にてログ基盤、KPI・BI構築を行いました。リリース後は運用、新規機能開発に携わりました。
</p>

<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">株式会社NextNinja</td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;"><a href='https://www.muvluv-dimensions.com/' target='_blank'>公式サイト</a></td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">12ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">
プログラム言語：PHP フレームワーク：Slim  <br />
DB：RDS/Athena インフラ：AWS ツール：Git/GitHub
        </td>
    </tr>
</table>

</div>


<div class="works">

<h3>上場ゲーム企業における全社共通・売上データ基盤の構築</h3>

<p>
スマートフォンゲームの複数プラットフォームに分散する売上データを集約し、決算業務および経営判断に資するデータ基盤を構築しました。    
データの収集から加工、DWH（BigQuery）への統合まで、一連のデータパイプラインの設計・開発を主導。  
GCPのサーバーレスアーキテクチャ（Cloud Run / Cloud Functions）を採用することで、スケーラビリティの確保と運用コストの最適化を実現しています。  
<br /><br />

担当工程：  <br />
- 要件定義からアーキテクチャ設計、実装、テストまでのフルサイクルを担当  <br />  
- BigQueryを中心としたデータウェアハウスの設計  <br />
- サーバーレス環境でのETL処理の実装  <br />
</p>

<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">Klab株式会社 </td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;">社内システム</td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">18ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">
プログラム言語：Python/C# フレームワーク：Flask  <br />
DB：BigQuery インフラ：GCP ツール：Git/GitHub
        </td>
    </tr>
</table>

</div>

<div class="works">

<h3>ラブライブ！スクールアイドルフェスティバルALL STARS</h3>

<p>
バックエンド・クライアントプログラミング（サーバー連携）を担当しました。
共通UI、共通機能、ホーム、ログインボーナス、アイドル一覧・詳細、ガチャ、アクセサリー機能を主に担当しました。
</p>

<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">Klab株式会社 </td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;"><a href='https://lovelive-as.bushimo.jp/' target='_blank'>公式サイト</a></td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">10ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">
プログラム言語：Python/C# フレームワーク：Flask/Unity3D  <br />
DB：MySQL/Redis インフラ：AWS ツール：Git/GitHub
        </td>
    </tr>
</table>

</div>

<div class="works">

<h3>翻訳支援ツール</h3> 
    
<p>
スマートフォンゲームのローカライズで利用するための翻訳支援ツールのリニューアル開発・運用を行いました。  
英語・中国語（簡体字）などさまざまな言語をサポートし、翻訳のバージョン、差分管理などができるツールです。  
</p>
    
<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">Klab株式会社 </td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;">社内システム</td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">3ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">        
プログラム言語：Python/Java フレームワーク：Flask/ApachePOI  <br />
DB：MySQL/Redis インフラ：AWS ツール：Git/GitHub
        </td>
    </tr>
</table>

</div>


<div class="works">

<h3>英語おもてなしガイド<VR対応></h3> 
    
<p>
スマートフォン、VRで学習可能な英語学習アプリを開発しました。
開発初期より参画しバックエンド・インフラ選定〜要件定義などを行いました。
インフラ設計・構築、API・DB設計は弊社で実装はベトナムオフショアメンバー２名をマネジメントし実装を行いました。
</p>
    
<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">株式会社ポケットクエリーズ</td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;"><a href='https://itunes.apple.com/jp/app/id1254402969' target='_blank'>AppStore</a></td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">6ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">        
プログラミング言語：PHP/C# フレームワーク：FuelPHP/Unity3D<br />
DB：MySQL/Redis インフラ：AWS ツール：Git/GitHub 
        </td>
    </tr>
</table>

</div>


<div class="works">

<h3>SINoALICE ーシノアリスー</h3> 
    
<p>
バックエンド・クライアントプログラミング（サーバー連携）を担当しました。
クエスト・ギルド機能を主に担当しました。
AppStoreトップセールスで１位も獲得しました。
</p>
    
<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">株式会社ポケラボ</td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;"><a href='http://sinoalice.jp/' target='_blank'>公式サイト</a></td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">12ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">        
プログラミング言語：PHP/C# フレームワーク：オリジナルサーバーフレームワーク/Unity3D<br />
DB：MySQL/Redis インフラ：AWS ツール：Git/GitHub 
        </td>
    </tr>
</table>

</div>


<div class="works">

<h3>銀鍵のアルカディアトライブ</h3> 
    
<p>
デジタルカードゲームとオフラインカードゲームを連携して遊ぶことができるゲームを開発しました。
開発初期より参画しバックエンド・インフラ選定〜要件定義を行いました。
API・DB・リアルタイム設計を弊社で実装はフリーランスメンバー（業務委託）3名、ベトナムオフショア2名をマネジメントし実装を行いました。
</p>
    
<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">株式会社グリー</td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;">サービス終了</td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">16ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">        
プログラミング言語：PHP/Node.js/C# フレームワーク：FuelPHP/Unity3D<br />
DB：MySQL/Redis インフラ：Azure ツール：Git/GitHub 
        </td>
    </tr>
</table>

</div>


<div class="works">

<h3>メイデンクラフト</h3> 
    
<p>
魔法少女をテーマにしたスマートフォンゲームの開発をしました。
開発途中より参画しました。Ruby on Railsで実装頓挫していたプロジェクトをPHPにて再実装しました。
サーバープログラミングを担当しAPI・DB設計、実装を行いました。
企画・開発は株式会社GeNERACE、開発協力として株式会社ファーストインパクト、株式会社トイズクリエイションが参加しました。
※ 弊社は株式会社ファーストインパクトから受注
</p>
    
<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">株式会社ファーストインパクト</td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;">サービス終了</td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">5ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">        
プログラミング言語：PHP/C# フレームワーク：FuelPHP/Unity3D<br />
DB：MySQL/Redis インフラ：AWS ツール：Git/GitHub 
        </td>
    </tr>
</table>

</div>

<div class="works">

<h3>WEBサービス（Erumaer）</h3> 
    
<p>
フィギュア・ホビーのまとめサイトの開発・運用をしました。
開発初期より参画しソフトウェア・インフラ選定〜要件定義を行いました。
インフラ・サーバープログラミングを担当しAPI・DB設計、実装を行いました。
</p>
    
<table>
    <tr>
        <th style="width: 20%;">企業名</th>
        <td style="width: 80%;">株式会社ホビーサーチ</td>
    </tr>
    <tr>
        <th style="width: 20%;">参考サイト</th>
        <td style="width: 80%;"><a href='https://www.1999.co.jp/erumaer/' target='_blank'>公式サイト</a></td>
    </tr>
    <tr>
        <th style="width: 20%;">作業期間</th>
        <td style="width: 80%;">12ヶ月</td>
    </tr>
    <tr>
        <th style="width: 20%;">仕様技術</th>
        <td style="width: 80%;">        
プログラミング言語：PHP/JavaScript フレームワーク：Codeigniter<br />
DB：MySQL/Redis インフラ：AWS ツール：Git/GitHub 
        </td>
    </tr>
</table>

</div>
