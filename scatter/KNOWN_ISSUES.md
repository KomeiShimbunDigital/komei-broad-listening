# 既知の問題点

## その他の注意点

1. langchainの非推奨警告
   - インポートパスの変更が推奨される
   - 例：`from langchain.embeddings import OpenAIEmbeddings` → `from langchain_community.embeddings import OpenAIEmbeddings`

2. パフォーマンスの考慮事項
   - トップページのデータサイズが大きい（約150kB）
   - 原因：分析結果のデータを静的に埋め込んでいる
   - 現状では仕様として許容
