"""第1回: 素のLLMに1回だけ質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする
    2026-10-26 追記
    実装,発展  uv run python -m app.ask --interactive #  会話履歴を保つ、トークン数の応答時間
    AIE_MODEL=gemini-3.6-flash uv run python -m app.ask --interactive #  モデル変更
    AIE_MODEL=gemini-3.8-flash uv run python -m app.ask --interactive # モデル変更

ツールも会話履歴も持たない「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse
import time

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def interactive() -> None:
    client = genai.Client(api_key=get_api_key())
    chat = client.chats.create(model=MODEL)

    print("会話を開始します。終了するには exit または quit を入力してください。")

    while True:
        try:
            question = input("\nあなた> ").strip()
        except EOFError:
            print()
            break

        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        try:
            started_at = time.perf_counter()
            response = chat.send_message(question)
            elapsed = time.perf_counter() - started_at
        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
            continue

        print(f"\n{response.text}")
        print(f"[応答時間] {elapsed:.2f} 秒")
        usage = response.usage_metadata
        if usage is not None:
            print(f"[入力トークン数] {usage.prompt_token_count}")
            print(f"[出力トークン数] {usage.candidates_token_count}")


def ask(question: str) -> str:
    client = genai.Client(api_key=get_api_key())
    started_at = time.perf_counter()
    response = client.models.generate_content(model=MODEL, contents=question)
    elapsed = time.perf_counter() - started_at

    print(f"[応答時間] {elapsed:.2f} 秒")
    usage = response.usage_metadata
    if usage is not None:
        print(f"[入力トークン数] {usage.prompt_token_count}")
        print(f"[出力トークン数] {usage.candidates_token_count}")

    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="会話履歴を保って続けて質問する",
    )
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    try:
        if args.interactive:
            interactive()
        else:
            print(f"[質問] {args.question}\n")
            print(ask(args.question))
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
