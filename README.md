# Komei Broad Listening Tools

## 改良の概要
komei-broad-listeningは、安野たかひろ氏の選挙対策チームが改良した「Talk to the City（[TTTC](https://github.com/AIObjectives/talk-to-the-city-reports)）」の改良版である「[anno-broadlistening](https://github.com/takahiroanno2024/anno-broadlistening)」をベースに、以下の主要な改良を加えたプロジェクトです。anno-broadlisteningの機能強化版として、UIの改善、Docker環境の整備、プロジェクト管理機能の追加などの改良を実施。これにより、ユーザーはより直感的で効率的なデータ分析と管理をできるようにしました。

### 1. **プロジェクト管理用のUI追加**   
    Flaskを用いたWebベースの管理画面を新たに実装し、プロジェクトの新規追加、分析処理、結果閲覧、削除などをブラウザ上で操作可能にしました。
    [!管理画面](/docs_komei/images/management_screen.png)

### 2. **Docker環境の整備**    
    Dockerfileおよびdocker-compose.ymlを追加し、環境構築を簡素化。これにより、ローカル環境でのセットアップやデプロイを容易にしました。
    
### 3. **プロジェクトのホスティング機能**    
    複数のプロジェクトを一元管理できるようになり、各プロジェクトの分析結果を統合的に閲覧・管理することができます。

## 主な改良点（ファイル変更を含む）

### 1. LangChainの実装更新
- **コミット**: `c882d22`, `61c5f02`
- **内容**: 古いLangChainのコードを現在のバージョンに適合させるための書き換え。API仕様や構造の変更に対応するコード修正。

### 2. UIの整理・表示改善
- **コミット**: `6107c72`, `b12a730`
- **ファイル**: `templates/`, `static/`, およびFlaskルーティングファイル
- **内容**: UI画面の構成変更、結果表示のロジック整理。視認性や操作性向上を意識した改善。

### 3. コンソール機能の追加
- **コミット**: `f8170be`
- **内容**: Webコンソールあるいはログ表示に関する機能を追加し、バックエンド処理の可視化を強化。

### 4. 翻訳処理の修正
- **コミット**: `f722bbc`
- **ファイル**: 翻訳API連携部分
- **内容**: 翻訳処理のバグ修正または翻訳対象の調整。

### 5. node_modulesの保存とデバッグ用コメント解除
- **コミット**: `2805a8b`, `0483fda`
- **内容**: `node_modules`一時保存（おそらく動作確認やビルドのため）、コード上のコメントアウトを解除し、機能を有効化。

## 使い方
1. 当レポジトリをローカルにクローン
2. 環境変数ファイルの作成
```
cd komei-broad-listening
echo "OPENAI_API_KEY=sk-..." >> .env

# .envが作成できているか確認
cat .env
```
3. Dockerのビルドと起動
```
docker-compose up --build
```
4. 管理画面にアクセス: http://localhost:8080

## anno-broadlisting
anno-broadlisteningとTTTCの改良点については[DIFFERENCES.md](/DIFFERENCES.md)を参照
その他、ドキュメントファイルなどはanno-broadlisteningをそのまま引き継いでいます。

## Talk to the City Reports
Talk to the City（[TTTC](https://github.com/AIObjectives/talk-to-the-city-reports)）
CLIでレポートを出力するアプリケーションです。Pythonとnextをベースにしており、静的でインタラクティブな散布図レポートとサマリーを生成します。
