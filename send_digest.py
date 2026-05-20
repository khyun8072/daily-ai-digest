#!/usr/bin/env python3
import os
import time
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send(text, retries=3):
    for attempt in range(retries):
        try:
            r = requests.post(API_URL, json={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": True
            }, timeout=30)
            if r.status_code == 200:
                print(f"  ✅ Sent ({len(text)} chars)")
                return True
            else:
                print(f"  ❌ HTTP {r.status_code}: {r.text[:300]}")
        except Exception as e:
            print(f"  ❌ Exception: {e}")
        if attempt < retries - 1:
            wait = 2 ** (attempt + 1)
            print(f"  Retrying in {wait}s...")
            time.sleep(wait)
    return False

MSG1 = """🌅 <b>Daily AI Digest — 2026-05-20</b>

📌 <b>오늘의 한눈에</b>
— 🔬 주목 논문: TIGER-FG — 텍스트로 이미지 검색 시각 집중, 커머스 Recall@1 +34.4pp
— 🚀 주목 릴리즈: vLLM v0.21.0 — KV Offload + Blackwell MLA, thinking budget 지원
— 🔑 키워드: [Lance 멀티모달 통합, OSCAR 2-bit KV, 커머스 시각 검색]
— 💡 즉시 활용: Ettin Reranker 17M — MiniLM 대비 품질↑ 속도↑, RAG 드롭인 교체 후보

━━━━━━━━━━━━━━━━━━━━
📚 <b>Papers</b>
━━━━━━━━━━━━━━━━━━━━

1. <a href="https://arxiv.org/abs/2605.18678">Lance: Unified Multimodal Modeling by Multi-Task Synergy</a> <code>[Multimodal]</code> ⭐5 | 👍 259 votes
   — 📝 이미지/비디오 이해·생성·편집을 단일 모델로 처리하는 통합 멀티모달 프레임워크.
   — 🔍 Dual-stream MoE + modality-aware RoPE로 이종 비주얼 토큰 간 간섭 억제, staged multi-task 학습으로 역할 충돌 없이 3가지 능력 동시 확보. 오픈소스 통합 모델 이미지·비디오 생성 SOTA.
   — 👉 상품 이미지 생성·편집·이해를 단일 백엔드로 처리하는 커머스 멀티모달 파이프라인 단순화에 실용적.

2. <a href="https://arxiv.org/abs/2605.18434">TIGER-FG: Text-Guided Implicit Fine-Grained Grounding for E-commerce Retrieval</a> <code>[Retrieval]</code> ⭐5
   — 📝 상품 텍스트를 암묵적 가이드로 활용해 부분 이미지 쿼리를 전체 상품 리스팅에 매칭하는 커머스 검색 프레임워크.
   — 🔍 별도 객체 탐지 없이 이중 증류로 쿼리-아이템 유사도 구조 보존. Recall@1 표준 +6.1pp, 복잡 레이아웃 +34.4pp. 쿼리 측 85.7M 파라미터. 새 벤치마크 ECom-RF-IMMR (1,000만 쌍) 공개.
   — 👉 크롭된 상품 사진으로 동일·유사 상품 검색하는 비주얼 탐색에 직접 적용 가능.

3. <a href="https://arxiv.org/abs/2605.18643">Post-Trained MoE Can Skip Half Experts via Self-Distillation</a> <code>[Efficient LLM]</code> ⭐4 | 👍 13 votes
   — 📝 이미 학습된 MoE 모델을 재훈련 없이 동적 Expert 스킵으로 변환하는 ZEDA 프레임워크.
   — 🔍 파라미터 없는 Zero-Expert 주입 후 원본 모델을 frozen teacher로 2단계 자기증류. Expert FLOP 50%+ 절감, 1.20× 추론 속도, Qwen3-30B-A3B 기준 동적 MoE 대비 +6.1점.
   — 👉 배포된 MoE 모델의 서빙 비용을 쉬운 토큰에서 즉시 절감하는 실용적 포스트프로세싱.

4. <a href="https://arxiv.org/abs/2605.17757">OSCAR: 2-bit KV Cache Quantization via Offline Spectral Covariance-Aware Rotation</a> <code>[Quantization]</code> ⭐4 | 👍 7 votes
   — 📝 어텐션 공분산 구조에 맞는 오프라인 회전으로 KV 캐시를 INT2 압축하는 양자화.
   — 🔍 Hadamard 대신 어텐션 소비 공분산 기반 회전+클리핑 오프라인 계산, 커스텀 INT2 커널. KV 메모리 8×↓, 처리량 최대 7×↑, 디코드 3×↑. 128K 컨텍스트에서도 BF16 대비 품질 손실 미미.
   — 👉 프로덕션 LLM 서빙에서 GPU 메모리를 8배 줄이고 처리량을 7배 올리는 게임체인저.

5. <a href="https://arxiv.org/abs/2605.17357">Dual-Diffusional Generative Fashion Recommendation</a> <code>[Recommendation]</code> ⭐4
   — 📝 이미지+텍스트 동시 생성 이중 디퓨전 트랜스포머 기반 패션 추천 시스템. (SIGIR'26)
   — 🔍 속성 캡션+코디 정보를 조건으로 이미지·텍스트 브랜치 공동 학습, 교차 모달 지식 공유. iFashion·Polyvore-U에서 기존 생성형 추천 모델 대비 성능·해석성·효율 우세.
   — 👉 "왜 어울리는가"를 이미지+텍스트로 동시에 설명하는 커머스 패션 추천 구현 방향.

[1/3]"""

MSG2 = """🚀 <b>Releases &amp; Tools</b>
━━━━━━━━━━━━━━━━━━━━

1. <a href="https://github.com/vllm-project/vllm/releases/tag/v0.21.0">vLLM v0.21.0</a> <code>[Efficient LLM]</code> ⭐5
   — 📝 KV Offload + Hybrid Memory Allocator 통합, Blackwell TOKENSPEED_MLA 백엔드, Speculative Decoding이 reasoning budget 지원.
   — 🔍 DeepSeek-R1/Kimi 추론 모델 서빙 최적화. AMD ROCm Dynamic Batch Optimization + CPU FP8 추가. 367커밋, 202기여자.
   — 👉 Reasoning 모델 서빙 인프라 검토 필수 버전. Transformers v5 마이그레이션도 이 버전부터.

2. <a href="https://github.com/unslothai/unsloth/releases/tag/v0.1.405-beta">Unsloth v0.1.405-beta</a> <code>[Fine-tuning]</code> ⭐4
   — 📝 MTP 자동 활성화로 GGUF 추론 ~2× 속도 향상, OpenAI·Anthropic API 연동 + 자동 프롬프트 캐싱.
   — 🔍 MLX 추론 실험적 지원, 멀티 언어 개선, 보안 강화. 파인튜닝 모델을 로컬 배포하면서 외부 API 폴백 연동 가능.
   — 👉 파인튜닝 후 로컬 GGUF 서빙 시 무료 2× 속도. 로컬 vs API 비용 비교 실험에 유용.

3. <a href="https://github.com/ollama/ollama/releases/tag/v0.30.0">Ollama v0.30.0</a> <code>[Efficient LLM]</code> ⭐4
   — 📝 llama.cpp 직접 지원 아키텍처 전환, Apple Silicon MLX 가속 추가. (Pre-release)
   — 🔍 GGML 대신 llama.cpp 직접 연결로 GGUF 포맷 호환성 강화, Mac 로컬 추론 대폭 개선.

4. <a href="https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.3.0">LangChain v1.3.0</a> <code>[Other]</code> ⭐3
   — 📝 에이전트 stream_events/astream_events에서 v3 프로토콜 지원 추가.
   — 🔍 v3 이벤트 스트리밍으로 에이전트 단계별 상태 추적 개선.

5. <a href="https://github.com/huggingface/transformers/releases/tag/v5.8.1">Transformers v5.8.1</a> <code>[Efficient LLM]</code> ⭐3
   — 📝 DeepSeek V4 WeightConverter regex 오류 수정 패치. shared_experts 오매칭 &amp; fatal_error 처리 버그 수정.

━━━━━━━━━━━━━━━━━━━━
📝 <b>Research Blogs</b>
━━━━━━━━━━━━━━━━━━━━

1. <a href="https://huggingface.co/blog/ettin-reranker">Introducing the Ettin Reranker Family</a> <code>[Retrieval]</code> ⭐5
   — 📝 17M~1B 파라미터 6종 CrossEncoder 리랭커 패밀리, MTEB NDCG@10 기준 동급 최강.
   — 🔍 ModernBERT 기반 + MSE 증류 (teacher: mxbai-rerank-large-v2), 1.43억 쌍 학습. FA2 + 시퀀스 언패딩으로 17M이 MiniLM보다 품질↑ 속도↑ (7,517 pairs/s). 모델·데이터·코드 전부 Apache 2.0.
   — 👉 커머스 RAG 파이프라인 Reranker 교체 최우선 후보. ettin-17m은 MiniLM 대비 품질+레이턴시 동시 개선.

2. <a href="https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2">Granite Embedding Multilingual R2</a> <code>[Retrieval]</code> ⭐4
   — 📝 97M·311M 다국어 임베딩 모델, 32K 컨텍스트, 200개 언어, Apache 2.0.
   — 🔍 97M 모델이 300M급 (multilingual-e5-base) 대비 MTEB 우세. Matryoshka 지원 (311M, 768→256 dim, 0.5점 손실).
   — 👉 글로벌 커머스 한국어+다국어 상품 검색에 경량 임베딩 모델 실험 시 우선 고려.

3. <a href="https://huggingface.co/blog/continuous_async">Unlocking Asynchronicity in Continuous Batching</a> <code>[Efficient LLM]</code> ⭐4
   — 📝 CUDA 스트림으로 CPU-GPU를 겹쳐 실행해 LLM 추론 처리량 22% 향상.
   — 🔍 H2D·compute·D2H 스트림 분리 + 이중 슬롯 메모리로 GPU 유휴 24%→0.6%. 새 커널 없이 Transformers 라이브러리 내 순수 하드웨어 조율.
   — 👉 기존 Transformers 서빙 파이프라인에서 코드 변경 최소화로 ~22% 비용 절감.

[2/3]"""

MSG3 = """🔥 <b>Community</b>
━━━━━━━━━━━━━━━━━━━━

1. [HN] <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3.5 Flash — Google</a> <code>[Other]</code> ⭐4 | 💬 492pts 382 comments
   — 📝 Google의 최신 경량 고성능 멀티모달 모델 공개.
   — 🔍 HN에서 가격·속도·멀티모달 처리 능력으로 뜨거운 토론. OpenAI/Anthropic 대비 가성비 논쟁이 핵심.

2. [HN] <a href="https://deepmind.google/models/gemini-omni/">Gemini Omni — DeepMind</a> <code>[Multimodal]</code> ⭐4 | 💬 236pts 102 comments
   — 📝 자연어로 비디오를 생성·편집하는 Google DeepMind의 멀티모달 비디오 모델.
   — 🔍 다중 입력 (이미지·텍스트·비디오·오디오) 처리, 물리 이해 기반 생성, 멀티턴 일관성 유지. SynthID 워터마크 내장.
   — 👉 커머스 상품 영상 생성·편집 자동화 방향을 가늠할 수 있는 레퍼런스.

3. [HN] <a href="https://github.com/antoinezambelli/forge">Forge — 8B 모델 guardrails로 agentic 86.5% 달성</a> <code>[Agent]</code> ⭐4 | 💬 206pts 73 comments
   — 📝 rescue parsing·retry nudge·step enforcement로 로컬 8B LLM 도구 호출 신뢰성 대폭 향상.
   — 🔍 Ministral-3 8B Q8이 26시나리오 eval 86.5% 달성. OpenAI 호환 프록시 모드로 기존 스택에 미들웨어 삽입 가능.
   — 👉 소형 LLM 기반 커머스 에이전트 (주문·CS) 프로덕션화 시 즉시 참고.

4. [GN] <a href="https://eugeneyan.com/writing/working-with-ai/">AI와 함께 일하며 복리처럼 성장하는 법 — Eugene Yan</a> <code>[Other]</code> ⭐3 | 💬 75pts
   — 📝 Anthropic 추천 시스템 개발자 Eugene Yan의 AI 협업 원칙.
   — 🔍 컨텍스트 제공→취향 설정→검증 자동화→위임 확대→피드백 루프의 5단계가 작업물을 다음 세션의 복리 자산으로 축적.

5. [HN] <a href="https://openai.com/index/advancing-content-provenance/">OpenAI Adopts Google's SynthID Watermark for AI Images</a> <code>[Other]</code> ⭐3 | 💬 156pts 71 comments
   — 📝 OpenAI가 AI 이미지 생성에 Google SynthID 워터마크 표준 채택.
   — 🔍 크로스 플랫폼 콘텐츠 출처 검증 도구 제공. 생성형 AI 콘텐츠 신뢰성·저작권 업계 표준화 신호.

[3/3]"""

messages = [MSG1, MSG2, MSG3]

print(f"총 {len(messages)}개 메시지 전송 시작")
all_ok = True
for i, msg in enumerate(messages, 1):
    print(f"\n메시지 [{i}/{len(messages)}] 전송 중... ({len(msg)} chars)")
    ok = send(msg)
    if not ok:
        all_ok = False
        print(f"  ❌ 메시지 {i} 최종 실패")
    time.sleep(1)

if all_ok:
    print("\n✅ 모든 메시지 전송 완료")
else:
    print("\n⚠️ 일부 메시지 전송 실패")
