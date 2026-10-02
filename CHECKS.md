# Verification Checks

| Check | Expected | Observed | Pass/fail |
|---|---|---|---|
| Question through OpenRouter | An answer and a usage line | Received sentence answer and token usage line | Pass |
| Usage record matches | Same model; same or close token counts | Verified on OpenRouter activity page | Pass |
| System prompt changed | Answer style changes accordingly | Response updated based on revised instructions | Pass |
| max_tokens = 20 | Truncated or empty answer; tokens still billed | Answer truncated early due to token cap | Pass |
| Model swapped | Different model name in usage; answer may differ | Successfully called alternate model via CHAT_MODEL | Pass |
| Two-model comparison | Compare token counts and costs | Tested anthropic/claude-3.5-haiku vs nvidia/nemotron-3-ultra-550b-a55b:free; Nemotron was $0.00 (free tier), Haiku logged standard input/output token pricing | Pass |
