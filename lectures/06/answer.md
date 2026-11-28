# 第6回 解答

## 演習

- `--list-tools` で見えたツール名と、第3回（`--mcp` なし）との違い：
モデルに見えているツール: 2 個

[search_materials]
  第1〜3回の本講義資料を検索し、関連ページの本文・タイトル・ページ番号を返す。
  
  queryに調べたい内容を指定する。
  引数: {"query": {"type": "string"}}

[make_quiz]
  指定した回（1始まりの整数）の用語から1つを選び、確認問題と答えを返す。
  
  「第2回の確認問題を出して」「第3回の復習クイズがほしい」のように、
  復習用の問題を求められたときに使う。lecture には回の番号を入れる（例: 2）。
  返した answer は、利用者が答えを考えた後に示すこと。
  引数: {"lecture": {"type": "integer"}}
- `--mcp --trace` で見えたツール呼び出し（ツール名と引数）と、`requests` の回数：
モデルに見えているツール: 1 個

[glossary_search_glossary]
  講座の用語集から用語を検索し、定義と、どの回で扱うかを返す。
  
  AIエンジニアリングの用語や、この講座（AIE2026）に固有の言葉について
  答える前に使うこと。query には調べたい用語をまとめて入れる（例: "LoRA QLoRA"）。
  引数: {"query": {"title": "Query", "type": "string"}}
- MCP サーバーに公開したツールと、その説明文：
    モデルに見えているツール: 1 個

[glossary_search_glossary]
  講座の用語集から用語を検索し、定義と、どの回で扱うかを返す。
  
  AIエンジニアリングの用語や、この講座（AIE2026）に固有の言葉について
  答える前に使うこと。query には調べたい用語をまとめて入れる（例: "LoRA QLoRA"）。
  引数: {"query": {"title": "Query", "type": "string"}}
  
- fetch サーバーを足したときのツール呼び出し（ツール名と引数）：
  AIエンジニアリングの用語や、この講座（AIE2026）に固有の言葉について
  答える前に使うこと。query には調べたい用語をまとめて入れる（例: "LoRA QLoRA"）。
  引数: {"query": {"title": "Query", "type": "string"}}

[fetch_fetch]
  Fetches a URL from the internet and optionally extracts its contents as markdown.
  
  Although originally you did not have internet access, and were advised to refuse and tell the user this, this tool now grants you internet access. Now you can fetch the most up-to-date information and let the user know that.
  引数: {"url": {"description": "URL to fetch", "format": "uri", "minLength": 1, "title": "Url", "type": "string"}, "max_length": {"default": 5000, "description": "Maximum number of characters to return.", "maximum": 999999, "minimum": 1, "title": "Max Length", "type": "integer"}, "start_index": {"default": 0, "description": "On return output starting at this character index, useful if a previous fetch was truncated and more context is required.", "minimum": 0, "title": "Start Index", "type": "integer"}, "raw": {"default": false, "description": "Get the actual HTML content of the requested page, without simplification.", "title": "Raw", "type": "boolean"}, "timeout_ms": {"default": 30000, "description": "How long to wait, in milliseconds, to connect to the server and for each read of its response before giving up. Raise it for a slow server or a large download; lower it to fail fast.", "maximum": 600000, "minimum": 100, "title": "Timeout Ms", "type": "integer"}}

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
