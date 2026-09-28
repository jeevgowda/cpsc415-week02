# Verification Checks

| Check | Expected | Observed | Pass/fail |
|---|---|---|---|
| Question through OpenRouter | An answer and a usage line | Received sentence answer and token usage line | Pass |
| Usage record matches | Same model; same or close token counts | Verified on OpenRouter activity page | Pass |
| System prompt changed | Answer style changes accordingly | Response updated based on revised instructions | Pass |
| max_tokens = 20 | Truncated or empty answer; tokens still billed | Answer truncated early due to token cap | Pass |
| Model swapped | Different model name in usage; answer may differ | Successfully called alternate model via CHAT_MODEL | Pass |
