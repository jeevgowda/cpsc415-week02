# Week 2 - Chat Client

## Overview
A command-line chat client using Python standard library (urllib.request, json, sys, os).

## How to Run
export OPENROUTER_API_KEY="sk-or-v1-..."
export CHAT_BASE_URL="https://openrouter.ai/api/v1"
export CHAT_MODEL="nvidia/nemotron-3-ultra-550b-a55b:free"

python3 chat.py "In one sentence, what is a context window?"

## Intent Corrections
1. Configured dynamically from environment variables (CHAT_BASE_URL, CHAT_MODEL, OPENROUTER_API_KEY) without hardcoded defaults.
2. Required output to print the model response followed by a usage line containing model name and token counts.

## Code Explanation
In chat.py, line 28 constructs the HTTP POST request using urllib.request.Request(url, data=payload, headers=headers) to send the JSON-encoded prompt to OpenRouter without relying on third-party libraries.

## Two-Model Comparison & Costs
- Model 1 (nvidia/nemotron-3-ultra-550b-a55b:free):
  - Input Tokens: 26 | Output Tokens: 49
  - Cost: $0.0000 (Free Tier)
- Model 2 (anthropic/claude-3.5-haiku):
  - Input Tokens: 26 | Output Tokens: 42
  - Cost: ~$0.0002 (Billed per OpenRouter token pricing)
- Observation: Both models correctly answered the prompt in one sentence. Nemotron provided a slightly longer explanation while running on the free tier.
