# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）："base_model": "Qwen/Qwen3.5-0.8B",
-   "seed": 42,
    "num_train_epochs": 20,  
    "warmup_steps": 6,
    "lr": 2e-4,
    "lora_r": 16,    
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
- 自分で学習を実行したか（`executed_training_myself`）：はい 
- {"label": "before", "n": 21, "format_rate": 0.09523809523809523, "content_rate": 0.0, "both_rate": 0.0, "seconds": 24.3}
- 学習前：`format_rate` = 0.09523809523809523　 / `content_rate` =　 0.0
- 学習後：`format_rate` =　 / `content_rate` =　
- 退行した質問：
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：
- 学習で変わったこと・変わらなかったこと：

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- 変えた設定やデータ：
- 結果（比較表や数字）：
- ファインチューニングが向く場面・向かない場面についての考察：
