# Intent: chat-client

## Goal
A single-command terminal tool that takes one question as a quoted argument, sends it to a language model over the network, prints the answer, and exits. `python3 chat.py "why is the sky blue?"` prints a paragraph and returns you to your shell prompt.

## Who it is for
Me, as the developer, and anyone grading this lab. Today I reach a model either through a browser chat window or through Claude Code itself, which means I have never seen the actual request and response that carry a prompt. Writing the smallest possible client by hand makes that exchange visible: one HTTP request, one JSON body, one field pulled out of the reply.

## Constraints
- **Language:** Python 3 standard library only (`urllib.request`, `json`, `sys`, `os`). No third-party packages, `pip install`, or SDKs like `requests` or `anthropic`.
- **Configuration:** Base URL (`CHAT_BASE_URL`) and model name (`CHAT_MODEL`) must be read dynamically from environment variables rather than being hardcoded in the source file [Correction 1].
- **API Key:** Read from `OPENROUTER_API_KEY` environment variable and never committed to repository.
- **Scope ceiling:** One file (`chat.py`), clean and minimal.

## Not in scope
- Conversation memory. Every run is a blank slate.
- Interactive use, streaming, web interface, or retries.
- Tool use, images, attachments, or multi-provider switching in a single run.

## Success looks like
1. `python3 chat.py "name three primary colors"` prints the answer followed by a final line displaying model name and token usage (`input_tokens`, `output_tokens`) [Correction 2].
2. Missing `OPENROUTER_API_KEY` prints a clear readable error message without a raw Python traceback and exits non-zero.
3. Network or API errors print readable error messages cleanly.
4. `grep -ri "sk-or" .` finds nothing in the repository.

## Approved by
Approved by: Jeevan Gowda Kumaraswamy
Date: September 28, 2026
