#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

TODAY = "2026-06-16"
CUTOFF = (datetime.strptime(TODAY, "%Y-%m-%d") - timedelta(days=30)).strftime("%Y-%m-%d")

new_entries = [
    # Papers
    {"id": "2606.13533", "type": "paper", "date": TODAY},
    {"id": "2606.12198", "type": "paper", "date": TODAY},
    {"id": "2606.13145", "type": "paper", "date": TODAY},
    {"id": "2606.11700", "type": "paper", "date": TODAY},
    {"id": "2606.10759", "type": "paper", "date": TODAY},
    {"id": "2606.11023", "type": "paper", "date": TODAY},
    {"id": "2606.13814", "type": "paper", "date": TODAY},
    # Releases
    {"id": "https://github.com/vllm-project/vllm/releases/tag/v0.23.0", "type": "release", "date": TODAY},
    {"id": "https://www.anthropic.com/news/claude-fable-5-mythos-5", "type": "release", "date": TODAY},
    {"id": "https://huggingface.co/google/diffusiongemma-26B-A4B-it", "type": "release", "date": TODAY},
    {"id": "https://github.com/unslothai/unsloth/releases/tag/v0.1.464-beta", "type": "release", "date": TODAY},
    {"id": "https://github.com/ollama/ollama/releases/tag/v0.30.8", "type": "release", "date": TODAY},
    {"id": "https://github.com/anthropics/claude-code/releases/tag/v2.1.178", "type": "release", "date": TODAY},
    {"id": "https://huggingface.co/MiniMaxAI/MiniMax-M3", "type": "release", "date": TODAY},
    # Blogs
    {"id": "https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/", "type": "blog", "date": TODAY},
    {"id": "https://deepmind.google/discover/blog/investing-in-multi-agent-ai-safety-research/", "type": "blog", "date": TODAY},
    {"id": "https://huggingface.co/blog/torch-mlp-fusion", "type": "blog", "date": TODAY},
    {"id": "https://huggingface.co/blog/allenai/olmo-eval", "type": "blog", "date": TODAY},
    # Community
    {"id": "https://news.ycombinator.com/item?id=48542100", "type": "community", "date": TODAY},
    {"id": "https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/", "type": "community", "date": TODAY},
    {"id": "https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/", "type": "community", "date": TODAY},
    {"id": "https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/", "type": "community", "date": TODAY},
    {"id": "https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models", "type": "community", "date": TODAY},
    {"id": "https://news.hada.io/topic?id=30488", "type": "community", "date": TODAY},
    {"id": "https://news.ycombinator.com/item?id=48528029", "type": "community", "date": TODAY},
]

with open("sent_ids.json", "r") as f:
    existing = json.load(f)

# 30일 초과 항목 제거
existing = [e for e in existing if e.get("date", "0000-00-00") >= CUTOFF]

# 중복 제거 후 신규 추가
existing_ids = {e["id"] for e in existing}
for entry in new_entries:
    if entry["id"] not in existing_ids:
        existing.append(entry)
        existing_ids.add(entry["id"])

with open("sent_ids.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

print(f"Updated sent_ids.json: {len(existing)} total entries ({len(new_entries)} new)")
