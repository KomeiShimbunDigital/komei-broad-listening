# Talk to the City (TttC)

<img width="400" alt="image" src="https://github.com/AIObjectives/talk-to-the-city-reports/assets/3934784/57cc6367-0808-40f0-980a-540530ff0866">
<img width="400" alt="image" src="https://github.com/AIObjectives/talk-to-the-city-reports/assets/3934784/aaf45844-5a19-41c8-8943-78866db9f666">

## 概要

TttC は、コメントの CSV ファイルを処理し、以下を行う HTML レポートを生成する AI パイプラインです。

- 元のコメントに含まれる主要な論点を抽出
- 意味的な類似性に基づいて論点をクラスターに分類
- 各クラスターに対してラベルと要約を生成
- クラスターごとの論点を探るためのインタラクティブな地図を提供

TttC は、さまざまな種類のデータを取り込み、異なる言語でレポートを生成することが可能です。  
例：

- [Recursive Public](https://tttc.dev/recursive) は、Pol.is ツールを使用して収集されたデータを基に生成されたレポートです。入力には投票が含まれており、地図では合意レベルに基づいて論点をフィルタリングできます。
- [GenAI Taiwan](https://tttc.dev/genai) は、英語または中国語（マンダリン）で読めるレポートです。データは、台湾で Collective Intelligence Project によって行われた生成 AI に関する公開相談から得られたものです。

TttC は、AI の整合性に焦点を当てた非営利の研究機関である [AI Objectives Institute](http://aiobjectives.org) によって開発されています。

詳細については、こちらのブログ記事もご覧ください：[An open-source AI tool to scale deliberation](https://ai.objectives.institute/blog/talk-to-the-city-an-open-source-ai-tool-to-scale-deliberation).


## AI 安全性に関する注意事項

TttC は、生成 AI が公共の討議を支援する可能性を探る研究プロジェクトです。LLM（大規模言語モデル）はバイアスがあり、信頼できない結果を出すことが知られています。我々はこれらの問題を軽減するために積極的に取り組んでいますが、現段階では結果の保証はできません。重要な意思決定を行う際には、パイプラインの結果だけに依存せず、必ず結果を検証することをお勧めします。

## レポートの生成環境の構築

### 依存関係

このリポジトリを使用して、TttC レポートをお使いのマシンで生成できます。

- OpenAI API キー
- Python と JavaScript が実行できるマシン
- CSV ファイル形式のデータ
  - comment-body および comment-id の列が必要です
    - comment-body にはコメントの内容が入ります
    - comment-id にはコメントのIDが入ります
- (Google Tag Managerを埋め込む場合)GTM ID

OpenAI APIキーおよびGTM IDは、.env.exampleに記載した環境変数の名称で設定する必要があります。
設定する際は以下のコマンドを実行してください。
e.g. 
```
export OPENAI_API_KEY="your_openai_api_key"
export NEXT_PUBLIC_GTM_ID="your_gtm_id"
export NEXT_PUBLIC_PRIVACY_POLICY_URL="your_privacy_policy_url"
```

#### python環境の構築
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


本プロジェクトはPython 3.10での動作を推奨しています。Python 3.12を使用すると、以下のようなエラーが発生する場合があります：

```
ModuleNotFoundError: No module named 'distutils'
```

このエラーを回避するために、pyenvを使用してPython 3.10をインストールすることができます。以下の手順で環境をセットアップしてください：

1. pyenvのインストール（まだインストールしていない場合）:
```bash
curl https://pyenv.run | bash
```

2. pyenvの設定をシェルに追加（.bashrcや.zshrcに以下を追加）:
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

3. Python 3.10のインストールと設定:
```bash
pyenv install 3.10
pyenv local 3.10
```

4. 依存パッケージのインストール:
```bash
pip install -r scatter/requirements.txt
```


#### javascript環境の構築
```
cd next-app
npm install
```


### データの配置
* `pipeline/inputs`フォルダにデータを配置してください。必要な列 `comment-id` および `comment-body` が存在することを確認してください。


### 設定ファイルの作成
* `pipeline/configs`フォルダに設定ファイルを作成してください
  * 設定ファイルの例として`example-polis.json`があります。これをコピーして編集してください。
  * 設定パラメータの詳細は[こちら](#設定ファイルのパラメータ)をご覧ください。

### パイプラインの実行
以下のコマンドを実行し、パイプラインを実行してください。configファイルは作成した設定ファイルの名称に変更してください。
```
cd pipeline
python main.py configs/my-project.json
```

## 生成されたレポートの表示

生成されたレポートは`pipeline/outputs/my-project/report`にあります。プロジェクトのトップレベルディレクトリでhttpサーバーを実行してローカルで開くことができます。

```
npm install -g http-server
http-server -p 8080
open http://localhost:8080/pipeline/outputs/my-project/report/
```

上記の`my-project`をconfigファイルの名称に変更すると、レポートを表示できます。

レポートは任意の静的ホスティングサービス（e.g. Vercel）を使用してデプロイできます。

(!) HTMLファイルは相対パスを使用してアセットを読み込んでいることに注意してください。レポートは任意のパス/ルートにデプロイできますが、相対パスが正しく解決されるようにURLの末尾にスラッシュを含める必要がある場合があります。

## 入力データのカラム

以下は、パイプラインでサポートされる入力CSVファイルの必須およびオプションのカラムのリストです：

```
{
// REQUIRED
'comment-id': string // コメントの一意の識別子
'comment-body': string // コメントの主な内容

// OPTIONAL
'agree'?: number // 投票数
'disagree?': number // 投票数
'video?': string // 動画のリンク
'interview?': string // インタビューの名前
'timestamp?': string // 動画のタイムスタンプ
}
```

## 設定ファイルのパラメータ

以下は、設定ファイルでサポートされるパラメータのリストです：

```
{
  // 必須
  input: string // 入力ファイルの名前（.csv拡張子なし）
  question: string // 参加者に対して行うメインの質問

  // 任意
  name?: string // プロジェクトの短い名前
  intro?: string // プロジェクトの短い紹介（Markdown形式）
  model?: string // 使用するモデル（オーバーライドされない場合）、デフォルトは "gpt-3.5-turbo"
  extraction?: {
    model?: string // 抽出ステップのためのモデル名（グローバルモデルをオーバーライド）
    prompt_file?: string // プロンプトファイルの名前（.json拡張子なし）
    prompt?: string // 抽出ステップのためのプロンプトの全内容
    limit?: number // 処理する行の最大数（デフォルトは1000）
    workers?: number // 並行ワーカーの最大数（デフォルトは1）
    properties?: string[] // 抽出するプロパティのリスト（デフォルトは[]）。抽出されたプロパティは出力ファイルに追加されます。
    categories?: { 
      [key: string]: { // カテゴリのグループ名 (例: "sentiment", "genre")
        [key: string]: string // 各カテゴリの名前とその説明
      }
    } // argsに付与するカテゴリの定義。キーはカテゴリグループ名、値は各カテゴリの説明のオブジェクト。categoriesが存在する場合はLLMを用いたカテゴリ分類がextraction内部で実行される。
    category_batch_size?: number // 一度のバッチ処理で分類するコメントの数 (デフォルトは5)
  },
  embedding?: {
    model?: string // 埋め込みステップのためのモデル名。"text-embedding-3-small" と "text-embedding-3-large" をサポート。デフォルトは "text-embedding-3-small"
  },
  clustering: {
    clusters?: number // 生成するクラスターの数（デフォルトは8）
  },
  labelling: {
    model?: string // ラベリングステップのためのモデル名（グローバルモデルをオーバーライド）
    prompt_file?: string // プロンプトファイルの名前（.json拡張子なし）
    prompt?: string // ラベリングステップのためのプロンプトの全内容
    sample_size?: number // ラベル生成のためにクラスターごとに引き出される引数の数
  },
  takeaways: {
    model?: string // Takeawaysステップのためのモデル名（グローバルモデルをオーバーライド）
    prompt_file?: string // プロンプトファイルの名前（.json拡張子なし）
    prompt?: string // Takeawaysステップのためのプロンプトの全内容
    sample_size?: number // Takeaways生成のためにクラスターごとに引き出される引数の数
  },
  translation: {
    model?: string // Takeawaysステップのためのモデル名（グローバルモデルをオーバーライド）
    prompt_file?: string // プロンプトファイルの名前（.json拡張子なし）
    prompt?: string // Takeawaysステップのためのプロンプトの全内容
    languages?: string[] // 翻訳する言語のリスト（デフォルトは[]）
    flags?: string[] // UIで使用するフラグのリスト（デフォルトは[]）
  },
  aggregation: {
    sampling_num?: number // レポート上で可視化する件数（デフォルトは5000）
    hidden_parameters: {
      properties?: { [key: string]: string[] }  // プロパティのカテゴリごとに隠すプロパティのリスト
                                                // 例: { "source": ["X API"] }
    }
  },
  visualization: {
    replacements?: {replace: string, by: string}[] // UIに適用するテキスト置換のリスト
  }
}
```

## 生成された出力

パイプラインを正常に実行した後、以下のファイルが見つかります：

```
outputs
└── my-project
    ├── args.csv // 抽出された引数
    ├── clusters.csv // 引数のクラスター
    ├── embeddings.pkl // 埋め込み
    ├── labels.csv // クラスターのラベル
    ├── translations.json // 翻訳（JSON）
    ├── status.json // パイプラインのステータス
    ├── result.json // 生成されたすべてのデータ
    └── report // HTMLレポートとアセットのフォルダー

```

`result.json`には、`args.csv`、`clusters.csv`、`labels.csv`、および`translations.json`の内容が含まれています。これらのファイルはキャッシュの目的でのみ保持されています。わずかに異なるパラメータでパイプラインを再実行する場合に備えて、すべてのデータを再計算する必要がないようにするためです。

## 文化庁「AIと著作権」バブリックコメントデータセット

`dataset-aipubcom`ブランチに[文科省が公開した「AIと著作権に関する考え方について（素案）」に関するパブリックコメント](https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/hoseido/r05_07/)のデータを元に作成したデータセットおよび分析中間データ、生成されたレポートが入っています。Talk to the Cityの分析の各ステップを改善していく上で、サンプルとして扱える大規模なデータがあると便利だからです。たとえば、Webブラウザでの表示の改善ではrasults.jsonさえあればよく、クラスタリング手法の改善ではそこまでの処理で作られるargs.csvとembeddings.pklがあれば十分です。

このブランチではembeddings.pklのサイズが大きいことが理由でGit LFSがONになっています。以下は、LFSの簡単なガイドです。

### Git LFS の導入
プロジェクト内の大容量ファイル（例: `embedding.pkl`）は Git LFS で管理しています。  参加する方は、以下を実行してください。

1. **Git LFSのインストール**
    - **Mac**: `brew install git-lfs`
    - **Windows**: [公式インストーラー](https://git-lfs.github.com/)を使用
    - **Linux**: `sudo apt-get install git-lfs` 等
2. **初期化**
   ```bash
   git lfs install
   ```

### ファイルの取得確認
- 通常どおり `git pull` すれば LFS管理ファイルも取得されます  
- LFSが導入されていない環境だとポインタだけダウンロードされ、実ファイルが取得されないので注意


## Credits

Earlier versions of this pipeline were developed in collaboration with [@Klingefjord](https://github.com/Klingefjord) and [@lightningorb](https://github.com/lightningorb). The example of data input file was provided by the Recursive Public team (Chatham House, vTaiwan, OpenAI).

## License

GNU Affero General Public License v3.0