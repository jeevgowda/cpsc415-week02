#!/usr/bin/env python3
"""Send one question to a language model and print the answer.

Usage: python3 chat.py "why is the sky blue?"

Configuration comes from the environment:
    OPENROUTER_API_KEY  required, the bearer token
    CHAT_BASE_URL       required, e.g. https://openrouter.ai/api/v1
    CHAT_MODEL          required, the model name to ask for
"""

import json
import os
import sys
import urllib.error
import urllib.request


def fail(message):
    """Print a readable error and exit non-zero."""
    print(message, file=sys.stderr)
    sys.exit(1)


def require_env(name):
    value = os.environ.get(name)
    if not value:
        fail("Error: %s is not set. Export it and try again." % name)
    return value


def ask(question, base_url, model, api_key):
    """Send one chat completion request and return the decoded response."""
    url = base_url.rstrip("/") + "/chat/completions"
    body = json.dumps(
        {
            "model": model,
            "messages": [{"role": "user", "content": question}],
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace").strip()
        try:
            detail = json.loads(detail)["error"]["message"]
        except (ValueError, KeyError, TypeError):
            pass
        fail("Error: the API returned %s %s. %s" % (error.code, error.reason, detail))
    except urllib.error.URLError as error:
        fail("Error: could not reach %s. %s" % (url, error.reason))

    try:
        return json.loads(raw)
    except ValueError:
        fail("Error: the API returned a response that was not valid JSON.")


def main():
    if len(sys.argv) != 2:
        fail('Usage: python3 chat.py "your question here"')

    question = sys.argv[1]
    api_key = require_env("OPENROUTER_API_KEY")
    base_url = require_env("CHAT_BASE_URL")
    model = require_env("CHAT_MODEL")

    payload = ask(question, base_url, model, api_key)

    try:
        answer = payload["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        fail("Error: the API response did not contain an answer.")

    usage = payload.get("usage") or {}
    print(answer)
    print(
        "\n[model: %s | input_tokens: %s | output_tokens: %s]"
        % (
            payload.get("model", model),
            usage.get("prompt_tokens", "unknown"),
            usage.get("completion_tokens", "unknown"),
        )
    )


if __name__ == "__main__":
    main()
