[anno-broadlistening](https://github.com/takahiroanno2024/anno-broadlistening)について、プロジェクト管理用のUI追加のほか、多少の修正、docker-composeでのホスティングなどを追加したレポジトリです。

## 追加項目
- プロジェクト管理用 UI
  - プロジェクトの新規追加、分析処理、結果閲覧、削除の実行
- 追加ファイル・ライブラリなど
  - Dockerfile, docker-compose.yml
  - FLASK

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


## Talk to the City Reports
Talk to the City（[TTTC](https://github.com/AIObjectives/talk-to-the-city-reports)）
CLIでレポートを出力するアプリケーションです。Pythonとnextをベースにしており、静的でインタラクティブな散布図レポートとサマリーを生成します。
