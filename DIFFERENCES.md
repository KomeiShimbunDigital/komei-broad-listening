# Differences between anno-broadlistening and talk-to-the-city-reports



This document outlines the key differences between this `anno-broadening` and the original [talk-to-the-city-reports](https://github.com/AIObjectives/talk-to-the-city-reports).
このドキュメントは、anno-broadeningとtalk-to-the-city-reportsの間の主な違いを文書化したものです。

Each section below contains detailed information about the changes, including relevant commit references and code examples.
以下の各セクションには、関連するコミット参照とコード例を含む変更の詳細情報が含まれています。

## UI Enhancements / UIの改善

### Collision Detection / 衝突検出
- Fixed circle overlap issues in visualization / 可視化における円の重なり問題を修正
- Improved readability of dense data points / 密集したデータポイントの可読性向上
- Commits: 
  - [`12ad649`](https://github.com/takahiroanno2024/anno-broadlistening/commit/12ad649) - "Fixes #10 #13 - fix collision detection" / 衝突検出の修正
  - [`2f90613`](https://github.com/takahiroanno2024/anno-broadlistening/commit/2f90613) - "Fixes #10 #13 - fix collision detection" / 衝突検出の修正

### Favorite List / お気に入りリスト
- Added ability to bookmark important items / 重要なアイテムをブックマークする機能を追加
- Improved navigation for frequently accessed content / よく使用するコンテンツへのナビゲーション改善
- Commit: [`5bd367c`](https://github.com/takahiroanno2024/anno-broadlistening/commit/5bd367c) - "Fixes #17 - default hidden favorite list" / お気に入りリストのデフォルト非表示化

### Fullscreen Tools / フルスクリーンツール
- Enhanced visualization tools for better data exploration / より良いデータ探索のための可視化ツールの強化
- Improved UI layout for fullscreen mode / フルスクリーンモードのUIレイアウト改善
- Commits:
  - [`f08e365`](https://github.com/takahiroanno2024/anno-broadlistening/commit/f08e365) - "Fixes #7 - fix fullscreen tools ui" / フルスクリーンツールUIの修正
  - [`8ce30ed`](https://github.com/takahiroanno2024/anno-broadlistening/commit/8ce30ed) - "Fixes #7 - fix fullscreen tools ui" / フルスクリーンツールUIの修正

### Search and Highlighting / 検索とハイライト
- Added real-time search highlighting / リアルタイム検索ハイライトの追加
- Improved visibility of search results / 検索結果の視認性向上
- Commit: [`f2c7c09`](https://github.com/takahiroanno2024/anno-broadlistening/commit/f2c7c09) - "add search-highlight" / 検索ハイライトの追加

## Performance Improvements / パフォーマンスの改善

### Hidden Circles Optimization / 隠れた円の最適化
- Implemented smart circle hiding for better performance / パフォーマンス向上のための円の非表示最適化
- Reduced unnecessary rendering of obscured elements / 隠れた要素の不要なレンダリングを削減
- Commit: [`f96dd6c`](https://github.com/takahiroanno2024/anno-broadlistening/commit/f96dd6c) - "hide obscured circles" / 隠れた円を非表示化

### Rendering Improvements / レンダリングの改善
- Fixed infinite update issue in DesktopMap / DesktopMapの無限更新問題を修正
- Improved re-render logic / 再レンダリングロジックの改善
- Commits:
  - [`f69d06c`](https://github.com/takahiroanno2024/anno-broadlistening/commit/f69d06c) - "fix DesktopMap setZoomState infinite update" / ズーム状態の無限更新を修正
  - [`6014b8e`](https://github.com/takahiroanno2024/anno-broadlistening/commit/6014b8e) - "fix re-render" / 再レンダリングの修正

### Error Handling / エラー処理の改善
- Added validation for classification results / 分類結果の検証を追加
- Improved error messages for better debugging / デバッグのためのエラーメッセージ改善
- Added fast-fail mechanisms / 早期失敗メカニズムの追加
- Commits:
  - [`98a3d45`](https://github.com/takahiroanno2024/anno-broadlistening/commit/98a3d45) - "add validetion for classification result" / 分類結果の検証を追加
  - [`30ba952`](https://github.com/takahiroanno2024/anno-broadlistening/commit/30ba952) - "add better error message" / エラーメッセージの改善
  - [`a827cc6`](https://github.com/takahiroanno2024/anno-broadlistening/commit/a827cc6) - "add fast-fail" / 早期失敗の追加

## Code Organization / コードの整理

### ESLint Configuration and Code Quality / ESLint設定とコード品質
- Added ESLint plugin for import order management (eslint-plugin-import) / インポート順序管理のためのESLintプラグインを追加
- Implemented stricter ESLint rules / より厳格なESLintルールを実装
- Commit: [`dae38e9`](https://github.com/takahiroanno2024/anno-broadlistening/commit/dae38e9) - "add eslint" / ESLintの追加
- Commit: [`1497e7d`](https://github.com/takahiroanno2024/anno-broadlistening/commit/1497e7d) - "apply eslint" / ESLintの適用

### Dependency Updates / 依存関係の更新
```diff
// scatter/next-app/package.json
dependencies:
+ "@use-gesture/react": "^10.3.1"
+ "classnames": "^2.5.1"
+ "lucide-react": "^0.469.0"
~ "next": "^14.2.15" (upgraded from 13.5.4)
```
These updates bring:
- Improved gesture handling for better UI interactions / より良いUIインタラクションのためのジェスチャー処理の改善
- Modern icon system with Lucide React / Lucide Reactによるモダンなアイコンシステム
- Latest Next.js features and security updates / 最新のNext.js機能とセキュリティアップデート

### Code Quality Improvements / コード品質の改善
- Added TypeScript type definitions for better type safety / より良い型安全性のためのTypeScript型定義の追加
- Implemented consistent code formatting / 一貫性のあるコードフォーマットの実装
- Added automated testing infrastructure / 自動テストインフラストラクチャの追加
  - Commit: [`8119f05`](https://github.com/takahiroanno2024/anno-broadlistening/commit/8119f05) - "use argparse, add --skip-interaction" / テスト自動化のための対話スキップオプション追加

## Additional Features / 追加機能

### Property Filtering / プロパティフィルタリング
- Added support for filtering data by multiple properties / 複数のプロパティによるデータフィルタリングのサポートを追加
- Improved data exploration capabilities / データ探索機能の向上
- Commits:
  - [`c1591d5`](https://github.com/takahiroanno2024/anno-broadlistening/commit/c1591d5) - "add Property Filter" / プロパティフィルターの追加
  - [`97f0d22`](https://github.com/takahiroanno2024/anno-broadlistening/commit/97f0d22) - "add multiple properties to example input" / 複数プロパティの例を追加
  - [`8e26b16`](https://github.com/takahiroanno2024/anno-broadlistening/commit/8e26b16) - "add descriptions about properties parameter in README" / プロパティパラメータの説明を追加

### Enhanced Error Messages / エラーメッセージの改善
- Added more descriptive error messages / より詳細なエラーメッセージを追加
- Improved error handling for better debugging / デバッグのためのエラー処理改善
- Commits:
  - [`30ba952`](https://github.com/takahiroanno2024/anno-broadlistening/commit/30ba952) - "add better error message" / エラーメッセージの改善
  - [`174ac61`](https://github.com/takahiroanno2024/anno-broadlistening/commit/174ac61) - "move cleaning logics to new file and add tests" / クリーニングロジックの整理とテスト追加

### Model Selection and Configuration / モデル選択と設定
- Added ability to select embedding model in config / 設定で埋め込みモデルを選択可能に
- Added model description in embedding process / 埋め込みプロセスにモデルの説明を追加
- Commits:
  - [`024ad97`](https://github.com/takahiroanno2024/anno-broadlistening/commit/024ad97) - "select embedding model in config" / 埋め込みモデルの選択を設定可能に
  - [`003217d`](https://github.com/takahiroanno2024/anno-broadlistening/commit/003217d) - "add model description in embedding process" / 埋め込みプロセスにモデルの説明を追加

## Documentation Updates / ドキュメントの更新

### README Improvements / READMEの改善
- Added detailed setup instructions / 詳細なセットアップ手順の追加
- Updated dependency information / 依存関係情報の更新
- Added Python version requirements / Python バージョン要件の追加
- Commits:
  - [`d469d1b`](https://github.com/takahiroanno2024/anno-broadlistening/commit/d469d1b) - "add pyenv descriptin (fix to python 3.10)" / Python バージョン要件の追加
  - [`cf6c751`](https://github.com/takahiroanno2024/anno-broadlistening/commit/cf6c751) - "update README(about dataset-aipubcom and Git LFS)" / データセットとGit LFSについての更新

### Issue Templates / Issue テンプレート
- Added standardized templates for bug reports and feature requests / バグ報告と機能リクエストの標準テンプレートを追加
- Improved issue tracking and management / Issue追跡と管理の改善
- Commit: [`1102ee4`](https://github.com/takahiroanno2024/anno-broadlistening/commit/1102ee4) - "add issue templates" / Issueテンプレートの追加

### Code Organization / コードの整理
- Added TypeScript type definitions / TypeScript型定義の追加
- Improved code documentation / コードドキュメントの改善
- Better file structure and organization / より良いファイル構造と整理
- Commits:
  - [`174ac61`](https://github.com/takahiroanno2024/anno-broadlistening/commit/174ac61) - "move cleaning logics to new file and add tests" / クリーニングロジックの整理とテスト追加
  - [`29a6862`](https://github.com/takahiroanno2024/anno-broadlistening/commit/29a6862) - "update next-app README" / Next.jsアプリのREADME更新

