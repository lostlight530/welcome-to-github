# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.12.0
> Date: 2026-06-13T03:46:41.752838

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.12.0


## New Model additions

### MiniMax-M3-VL

<img width="886" height="583" alt="image" src="https://github.com/user-attachments/assets/ae9dd96f-6877-4531-a06b-a756686f24e5" />

MiniMax-M3-VL is the vision-language member of the MiniMax-M3 family that pairs a CLIP-style vision tower with 3D rotary position embeddings with the MiniMax-M3 text backbone. It uses a mixed dense/sparse Mixture-of-Experts decoder with SwiGLU-OAI gated experts and a lightning indexer for block-sparse attention. The model processes images through a Conv3d patch embedding system and includes specialized components for efficient multimodal understanding and generation.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/minimax_m3_vl)
* Add minimax m3vl (#46600) by @ArthurZucker in [#46600](https://github.com/huggingface/transformers/pull/46600)


### PP-OCRv6: update documentation and slow tests (#46576)

<img width="3840" height="1494" alt="image" src="https://github.com/user-attachments/assets/e62284ec-78bf-49cb-8aa2-deccc665372f" />

The official weights for PP-OCRv6 are out: PP-OCRv6 is a lightweight OCR system that combines architectural innovation with data-centric optimization. It redesigns the backbone, detection neck, and recognition neck around a unified MetaFormer-style building block with structural reparameterization. Three model tiers (medium, small, tiny) share the same block primitives, covering deployment scenarios from server to edge.

* PP-OCRv6: update documentation and slow tests (#46576) by @ zhang-prog


### Add Parakeet-RNNT (#46331)

ParakeetForRNNT: a Fast Conformer Encoder + an RNN-T (RNN Transducer) decoder

- RNN-T Decoder: Standard neural transducer:
    - LSTM prediction network maintains language context across token predictions.
       - Joint network combines encoder and decoder outputs.
       - Greedy transducer decoding for inference: a blank emission advances the encoder frame by one, a non-blank emission stays on the same frame.

* Add Parakeet-RNNT (#46331) by @eustlb


## Bugfixes and improvements

* [CI] don't export OTELs within the tests (#46602) by @tarekziade in [#46602]
* [CI] capture checkers output in OTEL (#46601) by @tarekziade in [#46601]
* Lfm2: thread `seq_idx` through ShortConv for packed/varlen inputs (#46588) by @ChangyiYang in [#46588]
* put output_hidden_states into filter_output_hidden_states (#46422) by @molbap in [#46422]
* a11 for checkers (#46599) by @tarekziade in [#46599]
* Fix stop string matching for byte-fragment tokens (#46530) by @Incheonkirin in [#46530]
* [DiffusionGemma] better docs and links (#46569) by @gante in [#46569]
* Require `trust_remote_code` to run a local-directory `custom_generate` (#46483) by @LinZiyuu in [#46483]
* Fix torchaudio version not tied to torch version in docker file  (#46594) by @ydshieh in [#46594]
* [CI] Enable PR CI for all fork PRs via security gate (#46591) by @ydshieh in [#46591]
* [CB] [Minor] Add parameter to tune default compile level (#46533) by @remi-or in [#46533]
* Make DiffusionGemma trainable (#46568) by @kashif in [#46568]
* docs: 🌐 add Turkish translation for README file (#46312) by @onuralpszr in [#46312]
* fix-trainer-tests (#46541) by @SunMarc in [#46541]
* Remove unnecessary expand_as in get_placeholder_mask across VLMs (#44907) by @syncdoth in [#44907]
* [CI] Catch all shell/process execution issues in security gate via Bandit JSON report (#46560) by @ydshieh in [#46560]
* Honor a concrete dtype in AutoModel for composite checkpoints (#46514) by @qflen in [#46514]
* [CI] Implement real security check in PR CI security gate (#46557) by @ydshieh in [#46557]
* [CI] Add 60s delay in security gate for flow observation (#46555) by @ydshieh in [#46555]
* [TBC] [CI] Auto-approve PR CI for fork PRs via security gate (#46553) by @ydshieh in [#46553]
* [CI] fix and make less flaky (#46543) by @zucchini-nlp in [#46543]
* Fix hf_hub_download not placing file in current dir for url_to_local_path (#46545) by @ydshieh in [#46545]

## Significant community contributions

The following contributors have made significant changes to the library over the last release:

* @ArthurZucker
    * Add minimax m3vl (#46600)
* @eustlb
    * Add Parakeet-RNNT (#46331)

