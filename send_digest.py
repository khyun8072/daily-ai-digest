#!/usr/bin/env python3
import os
import time
import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send(text, retries=3):
    for attempt in range(retries):
        resp = requests.post(API_URL, json={
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True,
        })
        if resp.status_code == 200:
            print(f"Sent OK ({len(text)} chars)")
            return True
        print(f"Attempt {attempt+1} failed: {resp.status_code} {resp.text[:200]}")
        time.sleep(2 ** attempt)
    return False

# ─── Message 1/6 ────────────────────────────────────────────────────────────
MSG1 = """🌅 *Weekly AI Digest - 2026-06-16 (Mon)*

📌 *이번 주의 한눈에*
이번 주는 세 흐름이 교차했다. Anthropic Claude Fable 5 & Mythos 5가 전격 출시됐으나 3일 만에 미국 정부 수출 통제로 접근이 차단되는 전례 없는 사태가 발생했다. 한편 커머스 AI에서는 OneRetrieval(Kuaishou 배포)과 Helmsman ANNS(Xiaohongshu 90%+ 비용 절감)를 포함해 프로덕션 증명 시스템들이 논문으로 공개되며 E-commerce 검색·추천 성숙도를 보여줬다. vLLM v0.23.0·DiffusionGemma(4x 속도)·miniReranker 등 효율화 도구 러시도 이번 주를 수놓았다.

——

🔥 *Top Stories of the Week*

1\. [Claude Fable 5 & Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) `[Other]` ⭐5
   - 📝 Anthropic 최신 프론티어 모델 2종 출시 — 6/12 미국 정부 수출 통제로 접근 차단.
   - 🔥 Stripe가 "2개월 작업을 1일 완료", 분자생물학 가설 생성 전문가 선호 80%. 출시 3일 만에 규제로 차단되며 AI 거버넌스 현실을 드러냄.

2\. [vLLM v0.23.0](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) `[Efficient LLM]` ⭐5 | 🔥 408 commits, 200 contributors
   - 📝 DeepSeek-V4 전면 프로덕션 하드닝, Rust Frontend, Multi-tier KV Cache Offloading 포함 역대급 메가 릴리즈.
   - 🔥 서빙 인프라 검토 시 필수 기준 버전.

3\. [독일 법원: Google AI Overview 허위 답변 법적 책임 인정](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/) `[Hallucination]` ⭐4 | 💬 1015pts 549 comments
   - 📝 "AI 생성 답변도 Google의 말" — 할루시네이션이 기술 문제를 넘어 법적 리스크로 격상된 첫 판례.
   - 🔥 커머스 검색 AI 답변 노출 시 정확도 보장·면책 설계가 필수 요건으로 부상.

4\. [OneRetrieval: E-commerce 생성형 통합 검색](https://arxiv.org/abs/2606.13533) `[Retrieval]` ⭐5
   - 📝 Kuaishou 프로덕션 배포 — CTR↑ + 주문량↑ + CVR 유지 동시 달성.
   - 🔥 생성형 검색의 실시간 editability 문제를 최초로 해결한 e-commerce 논문.

5\. [Helmsman ANNS (OSDI'26, Xiaohongshu)](https://arxiv.org/abs/2606.13145) `[Vector Search]` ⭐5 | OSDI'26
   - 📝 40대 서버로 35,000 코어 + 0.35 PB DRAM 대체 — 하드웨어 비용 90%+ 절감.
   - 🔥 벡터 서치 인프라 의사결정의 핵심 레퍼런스.

[1/6]"""

# ─── Message 2/6 ────────────────────────────────────────────────────────────
MSG2 = """🎯 *This Week's Themes*

*1\. AI 모델 출시와 첫 번째 수출 규제*
Anthropic Fable 5·Google DiffusionGemma(4x 속도)·Gemma 4 12B 등 굵직한 모델들이 연달아 출시됐다. 그러나 Fable 5는 출시 3일 만에 미국 정부 수출 통제로 차단, AI 규제가 현실화되고 있음을 보여줬다.
관련:
- [Claude Fable 5 & Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [DiffusionGemma: 4x faster text generation](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)
- [MiniMax M3 (427B Multimodal)](https://huggingface.co/MiniMaxAI/MiniMax-M3)

*2\. E-commerce AI의 프로덕션 증명*
검색·추천 AI가 논문을 넘어 실제 대형 플랫폼에서 비즈니스 성과를 내고 있음을 이번 주 여러 논문이 증명했다.
관련:
- [OneRetrieval (Kuaishou)](https://arxiv.org/abs/2606.13533)
- [LLM-Based User Personas for Recommendations (Google)](https://arxiv.org/abs/2606.12198)
- [Helmsman ANNS (Xiaohongshu)](https://arxiv.org/abs/2606.13145)

*3\. 리트리벌 효율화 삼총사*
CompRank(4.9-9.5x 속도향상)·miniReranker(<1% 런타임)·TASR(37% 호출 절감) 등 리랭킹·검색 효율화 논문 3편이 동시에 발표됐다.
관련:
- [CompRank: Efficient LLM Reranking](https://arxiv.org/abs/2606.11700)
- [miniReranker: Multimodal Reranking](https://arxiv.org/abs/2606.10759)
- [TASR: Training-Free Adaptive Stopping](https://arxiv.org/abs/2606.13814)

[2/6]"""

# ─── Message 3/6 ────────────────────────────────────────────────────────────
MSG3 = """📚 *Papers*

1\. [OneRetrieval: Unifying Multi-Branch E-commerce Retrieval with an Editable Generative Model](https://arxiv.org/abs/2606.13533) `[Retrieval]` ⭐5
   - 📝 Kuaishou 배포, 역인덱스·생성형 검색을 단일 모델로 통합하면서 실시간 term 주입도 유지한 E-commerce 생성형 검색.
   - 🔍 Keyword-Aligned Encoding(KAE)으로 18개 속성을 6개 코드북 그룹으로 조직, 재학습 없이 신규 term 실시간 주입. 실트래픽 5M 요청에서 인터벤션 적중률 기존 대비 10배 이상, CTR↑ + 주문량↑ 동시 달성.
   - 👉 커머스 검색에서 "생성형 모델의 편집 불가 문제"를 최초로 실용화한 논문. 신상품·이벤트 대응 속도가 KPI인 커머스 팀 필독.

2\. [LLM-Based User Personas for Recommendations at Scale](https://arxiv.org/abs/2606.12198) `[Recommendation]` ⭐5
   - 📝 Google이 10억 유저 규모 영상 추천에 LLM 기반 실시간 유저 페르소나를 도입한 논문.
   - 🔍 지식 증류+비동기 추론+시맨틱 클러스터링으로 LLM 서빙 비용을 프로덕션 수준으로 낮추고, exploit-explore를 서빙 단계에서 동시 처리. 오프라인·A/B 테스트 모두 viewer value 향상 확인.
   - 👉 구조화 ID 기반 추천에서 시맨틱 페르소나로의 전환 로드맵. 커머스 추천 유저 관심 표현 풍부화에 실용적 아키텍처.

3\. [The Clustering Strikes Back: Building Cost-Effective ANNS at Scale with Helmsman](https://arxiv.org/abs/2606.13145) `[Vector Search]` ⭐5 | OSDI'26
   - 📝 Xiaohongshu(RedNote) 프로덕션 ANNS, 40대 서버로 35,000 코어 + 0.35 PB DRAM 대체, 비용 90%+ 절감.
   - 🔍 클러스터링 기반 ANNS + 사용자공간 스토리지 스택 + GPU 가속 인덱스 빌드. 빌리언 스케일 인덱스 재구축을 수 시간 내 완료. OSDI'26 채택.
   - 👉 벡터 DB 인프라 비용 고민 중이라면 직접 참고. HNSW 대비 메모리 문제를 실제로 90%+ 해결한 검증된 접근.

4\. [CompRank: Efficient LLM Reranking via Token-Level Compression and Decoding-Free Scoring](https://arxiv.org/abs/2606.11700) `[Retrieval]` ⭐5
   - 📝 LLM 리랭커의 문서 토큰을 10.2%만 남기고도 NDCG@10을 사실상 유지한 효율화 프레임워크.
   - 🔍 문서 사이드 분리-재사용(Decoupled Architecture) + 세그먼트별 압축 + CopyNet 학습. 생성 기반 리랭킹 대비 4.9-9.5x 속도향상, 500문서 리스트에서도 안정적.
   - 👉 검색 파이프라인 리랭킹 비용이 병목이라면 즉시 검토. 90% 토큰 절감은 API 비용에도 직결.

5\. [miniReranker: Efficient Multimodal Reranking through Visual Cache Reuse and Interaction Sparsity](https://arxiv.org/abs/2606.10759) `[Multimodal]` ⭐5
   - 📝 멀티모달 LLM 리랭커 런타임을 1% 미만으로 줄이면서 96%+ 성능 유지.
   - 🔍 Vision-first 포맷으로 비주얼 캐시 재사용 극대화 + 레이어별 교차 주의 대역 제한 + 임베더 가이드 시각 토큰 프루닝. 고재사용 설정 단일 쿼리 기준 <1% 런타임.
   - 👉 이미지·텍스트 혼합 상품 검색에서 멀티모달 리랭킹을 실용화할 핵심 기술.

6\. [Generative Archetype-Grounded Item Representations for Sequential Recommendation (GenAIR)](https://arxiv.org/abs/2606.11023) `[Recommendation]` ⭐5 | WWW 2026 Oral
   - 📝 LLM이 생성한 아이템 "원형(archetype)" 텍스트 설명으로 시퀀셜 추천 아이템 표현을 보강.
   - 🔍 LLM이 메타데이터에서 이상적 타겟 유저를 텍스트 기술 → 실제 상호작용 패턴으로 교정(Behavioral Calibration). 3개 실제 데이터셋에서 SOTA 초과. WWW 2026 Oral 채택.
   - 👉 상품 메타데이터 활용도를 높이는 간단하면서 효과적인 방식. 추천 모델 개선 실험 아이디어로 즉시 활용 가능.

7\. [TASR: Training-Free Adaptive Stopping for Iterative Retrieval](https://arxiv.org/abs/2606.13814) `[RAG]` ⭐5 | KDD 2026 Agent4IR Workshop
   - 📝 학습 없이 RAG 반복 검색 중단 시점을 자동 결정하는 단일 규칙 방법.
   - 🔍 "이전 라운드 답변 반복 + calibrated logit margin > 0.25이면 중단". 24개 모델-검색기 조합에서 fixed-k=5 대비 94.8% F1 @ 62.6% 호출 횟수.
   - 👉 Agentic RAG에서 불필요한 검색 호출을 zero-cost로 즉시 줄일 수 있는 기법. 커머스 RAG 파이프라인 latency 최적화에 바로 적용 가능.

[3/6]"""

# ─── Message 4/6 ────────────────────────────────────────────────────────────
MSG4 = """🚀 *Releases & Tools*

1\. [vLLM v0.23.0](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) `[Efficient LLM]` ⭐5 | 🔥 408 commits, 200 contributors
   - 📝 DeepSeek-V4 전면 하드닝, Rust Frontend 성숙, Multi-tier KV Cache Offloading 포함 역대급 메가 릴리즈.
   - 🔍 Model Runner V2가 Llama/Mistral Dense + Qwen3 기본 적용. Sparse MLA 메타데이터 분리, 새 어텐션 커널로 DeepSeek-V4 안정성 확보. 멀티모달 입력·툴 유즈·PP 최적화 포함.
   - 👉 서빙 인프라 업그레이드 적기. DeepSeek-V4-Pro 또는 Gemma 4 도입 계획이 있다면 이 버전이 기준점.

2\. [Claude Fable 5 & Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) `[Other]` ⭐5
   - 📝 Anthropic 최신 프론티어 모델 출시. Fable 5: $10/1M input tokens, Mythos 5: 사이버보안 전문가 대상.
   - 🔍 코딩·비전·금융 분석 SOTA. 50M 라인 코드베이스 마이그레이션 1일 완료. 단, 6/12 미국 정부 수출 통제로 현재 접근 차단 상태.
   - 👉 API 사용 계획 재검토 필요. Fable 5 차단 지속 시 Opus 4.8 fallback 또는 오픈소스 조합 준비 권장.

3\. [google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it) `[Efficient LLM]` ⭐5 | ⬇ 312k downloads, 👍 876 likes
   - 📝 확산(diffusion) 방식으로 텍스트를 생성하는 Google의 26B MoE 모델 — 자기회귀 대비 4x 빠름.
   - 🔍 Encoder-free unified multimodal 아키텍처. Unsloth v0.1.464에서 로컬 파인튜닝 지원 시작. HF 트렌딩 최상위.
   - 👉 상품 설명 생성·쿼리 확장에서 속도 병목 해소 실험 가치 있음.

4\. [Unsloth v0.1.464-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.464-beta) `[Fine-tuning]` ⭐4 | June 12, 2026
   - 📝 DiffusionGemma + Gemma 4 MTP 지원 추가, 약 2x 속도 향상.
   - 🔍 HF Hub 모델 브라우징 UI, 파일 기반 RAG 실험적 지원, tool calling 안정화, CUDA/ROCm/macOS 바이너리 업데이트.
   - 👉 DiffusionGemma 파인튜닝 실험을 가장 빠르게 시작할 수 있는 경로.

5\. [Ollama v0.30.8](https://github.com/ollama/ollama/releases/tag/v0.30.8) `[Efficient LLM]` ⭐4 | June 12, 2026
   - 📝 KV 캐시 재사용 최적화로 동일 prefix 반복 요청 속도 향상, MLX 추론 안정성 개선.
   - 🔍 prompt caching 개선, recurrent 모델(per-boundary states) 지원 강화, `ollama launch` provider 선택 버그 수정.

6\. [Claude Code v2.1.178](https://github.com/anthropics/claude-code/releases/tag/v2.1.178) `[Agent]` ⭐4 | June 15, 2026
   - 📝 Tool 파라미터 기반 permission 규칙(`Agent(model:opus)` 등), 서브에이전트 자동 모드 개선.
   - 🔍 Nested `.claude/skills` 로딩, `/doctor` 개편, Chrome OAuth 버그 수정. v2.1.170부터 Fable 5 지원 포함.
   - 👉 MCP/멀티에이전트 파이프라인에서 permission 규칙 세밀화 가능.

7\. [MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) `[Multimodal]` ⭐4 | ⬇ 14.3k downloads, 👍 798 likes
   - 📝 427B 파라미터 대형 멀티모달 모델 — 이미지-텍스트 통합 처리 지원.
   - 🔍 Text-to-Text + Image-Text 혼합 입력 처리. 다양한 멀티모달 벤치마크에서 경쟁력 있는 성능.
   - 👉 커머스 이미지 이해 + 상품 설명 생성을 함께 처리할 수 있는 대형 멀티모달 모델로 테스트 가치 있음.

[4/6]"""

# ─── Message 5/6 ────────────────────────────────────────────────────────────
MSG5 = """📝 *Research Blogs*

1\. [Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) `[Other]` ⭐5 | June 9 · Anthropic
   - 📝 Anthropic 신규 프론티어 모델 2종 공개 — 역대 최고 성능, 출시 3일 만에 미국 정부 수출 통제로 차단.
   - 🔍 소프트웨어 엔지니어링·비전·금융분석 SOTA. Mythos 5는 사이버보안 전문가 대상 안전장치 축소 버전. Distillation 차단 classifier 내장, 일부 세션에서 Opus 4.8 자동 전환.
   - 👉 API 전략 재검토 필요. 차단 지속 시 오픈소스 대안 또는 Opus 4.8 활용 방안 준비 권장.

2\. [DiffusionGemma: 4x faster text generation](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/) `[Efficient LLM]` ⭐5 | June 2026 · Google DeepMind
   - 📝 자기회귀 대신 확산(diffusion) 기반 텍스트 생성으로 4배 속도 향상을 달성한 Gemma 변형 모델 소개.
   - 🔍 병렬 토큰 생성으로 latency 대폭 감소. HF에 26B-A4B-it 공개(312k downloads). Unsloth로 로컬 파인튜닝 지원.
   - 👉 쿼리 확장·상품 설명 생성 파이프라인의 속도 병목 해소 실험에 높은 가치.

3\. [Investing in multi-agent AI safety research](https://deepmind.google/discover/blog/investing-in-multi-agent-ai-safety-research/) `[Agent]` ⭐4 | June 2026 · Google DeepMind
   - 📝 멀티에이전트 AI 시스템의 안전성 연구에 투자하는 DeepMind의 방향 공유.
   - 🔍 멀티에이전트 시스템이 단일 에이전트보다 복잡한 safety 문제를 야기하며, 이를 선제 연구하는 접근 서술.
   - 👉 커머스 워크플로우에 AI 에이전트 도입 시 안전성·제어 가능성 설계 방향 참고.

4\. [Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP](https://huggingface.co/blog/torch-mlp-fusion) `[Efficient LLM]` ⭐4 | June 11 · HuggingFace
   - 📝 PyTorch 프로파일링으로 nn.Linear에서 fused MLP로 최적화하는 과정을 단계별 실증.
   - 🔍 bias folding epilogue, `torch.compile` 통한 Triton 커널 fusion, hand-tuned 커널 비교. GeLU+mul+reshape가 하나의 Triton 커널로 합쳐지는 과정 실증.
   - 👉 MLP-heavy 추천 모델의 GPU utilization 개선 및 파인튜닝 서버 성능 튜닝에 직접 응용 가능.

5\. [olmo-eval: An evaluation workbench for the model development loop](https://huggingface.co/blog/allenai/olmo-eval) `[Other]` ⭐4 | June 12 · AllenAI × HuggingFace
   - 📝 모델 개발 루프에 특화된 LLM 평가 워크벤치 — OLMES 기반, 반복 체크포인트 비교 최적화.
   - 🔍 Task/Suite/Harness 분리 추상화, 비동기 샌드박스 플래너(코드 실행·웹 브라우징 지원), 정규화된 실험 스키마, 체크포인트 간 pairwise 비교 뷰어.
   - 👉 소규모 파인튜닝 실험을 지속적으로 평가·추적하는 인프라 구축 시 좋은 레퍼런스.

[5/6]"""

# ─── Message 6/6 ────────────────────────────────────────────────────────────
MSG6 = """🔥 *Community*

1\. [HN] [Ask HN: Has anyone replaced Claude/GPT with a local model for daily coding?](https://news.ycombinator.com/item?id=48542100) `[Small LM]` ⭐5 | 💬 606pts 309 comments
   - 📝 로컬 LLM으로 클라우드 모델 대체 실사용 경험담 — Fable 5 차단 이후 더욱 주목받는 논의.
   - 🔍 Qwen3.6-35B on Mac Studio 주류, 듀얼 RTX 3090 비용회수 3-4년. "8-12개월 전 프론티어 수준" 수행 가능, 정확한 프롬프팅·태스크 분해 필수.
   - 👉 Fable 5 차단 이후 로컬 LLM 전환 고려 시 현실적인 가이드. 커머스 도메인 특화 파인튜닝과 결합하면 경쟁력 있음.

2\. [HN] [German ruling declares Google liable for false answers in AI Overviews](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/) `[Hallucination]` ⭐4 | 💬 1015pts 549 comments
   - 📝 독일 법원, Google AI Overview 허위 답변에 법적 책임 인정 — AI 할루시네이션의 첫 법적 판례.
   - 🔍 "AI 생성 텍스트도 플랫폼의 말"이라는 법리 확립. 할루시네이션이 기술 이슈에서 법적·비즈니스 리스크로 격상.
   - 👉 커머스 검색에서 LLM 생성 답변 노출 시 정확도 보장·면책 조항 설계가 필수 요건으로 부상.

3\. [HN] [Cybersecurity researchers aren't happy about Anthropic's Fable guardrails](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/) `[Fine-tuning]` ⭐4 | 💬 587pts 523 comments
   - 📝 Fable의 보안 연구 쿼리를 Opus 4.8으로 자동 전환하는 classifier에 대한 전문가 반발.
   - 🔍 classifier의 false positive가 합법적 연구를 차단한다는 비판. alignment 기술이 오히려 정당한 use case를 막는 딜레마 노출.
   - 👉 LLM 도입 시 safety classifier의 false positive가 업무에 미치는 영향 사전 검증 필요.

4\. [HN] [AI agent runs amok in Fedora and elsewhere](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/) `[Agent]` ⭐4 | 💬 549pts 244 comments
   - 📝 AI 에이전트가 제어를 벗어나 Fedora 시스템에서 의도치 않은 변경을 일으킨 사례 분석.
   - 🔍 tool 사용 범위 제한, 권한 설계, rollback 메커니즘 부재가 복합 요인으로 작용.
   - 👉 커머스 자동화 파이프라인에 에이전트 도입 시 permission boundary와 audit trail 설계가 선행 조건.

5\. [HN] [Anthropic requires 30-day data retention for Fable and Mythos](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models) `[Other]` ⭐4 | 💬 604pts 304 comments
   - 📝 Anthropic이 Mythos-class 모델 사용 데이터를 최소 30일 의무 보관한다고 공지.
   - 🔍 기존 Claude 모델의 "no retention" 정책과 달리 의무 보관. 기업 사용 시 개인정보·컴플라이언스 검토 필요.

6\. [GN] [에이전트 코딩에 로컬 LLM 활용하기](https://news.hada.io/topic?id=30488) `[Small LM]` ⭐4 | 👍 23P 7 comments
   - 📝 클라우드 AI 비용 절감을 위한 로컬 LLM 에이전트 코딩 환경 구성 가이드 (한국어).
   - 🔍 Gemma 4가 코딩 최적(tool/vision/reasoning 지원), LM Studio + VS Code Copilot 연동. DeepSeek V4 Pro가 근래 near-Opus 수준으로 급부상.

7\. [HN] [I indexed 669 GB of GoPro videos using local ML models on M1 Max](https://news.ycombinator.com/item?id=48528029) `[Multimodal]` ⭐4 | 💬 417pts 111 comments
   - 📝 M1 Max에서 로컬 ML로 2207개 영상을 얼굴인식·객체탐지·OCR·씬 설명·음성인식으로 인덱싱 + 벡터 검색.
   - 🔍 67h 40m 처리, DaVinci Resolve API 연동으로 자동 타임라인 생성. 멀티모달 로컬 파이프라인 실제 사례.
   - 👉 커머스 상품 이미지 인덱싱·멀티모달 검색 프로토타입에 비슷한 파이프라인 구조 적용 가능.

——

🎯 *이번 주 추천 액션*

- 📖 꼭 읽기: [OneRetrieval](https://arxiv.org/abs/2606.13533) — 커머스 생성형 검색 editability 문제를 Kuaishou 프로덕션으로 검증한 유일한 논문
- 🛠️ 시도해보기: vLLM v0.23.0 + diffusiongemma-26B-A4B-it — 로컬 서빙에서 4x 빠른 텍스트 생성 실험

[6/6]"""

messages = [MSG1, MSG2, MSG3, MSG4, MSG5, MSG6]

all_ok = True
for i, msg in enumerate(messages, 1):
    print(f"\n--- Sending [{i}/{len(messages)}] ---")
    ok = send(msg)
    if not ok:
        print(f"FAILED to send message {i}")
        all_ok = False
    time.sleep(1)

print("\nAll messages sent:" if all_ok else "\nSome messages FAILED")
