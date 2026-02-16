# 🧬 NEXUS CORTEX: Autonomous Evolution Blueprint (自动进化蓝图)

> **Generated**: 2026-02-16
> **Scope**: Autonomous Agency, Feedback Loops, Dynamic Learning
> **Philosophy**: "Small and Stable" (Quiet, Pragmatic, Engineering Excellence)

---

## I. Executive Summary (执行摘要)
The current system operates on a static rule set (e.g., `Log10(Stars)*30` trust score). To achieve true autonomy, we must implement a **Metacognitive Feedback Loop**.
Current state: **Recorder** (Passive).
Target state: **Learner** (Active).
Mechanism: **Dual-Loop Learning** (Tactical Execution + Strategic Evolution).

## II. Feedback Capture Mechanism (反馈捕获机制)
### The "Curator" (策展人)
The Curator monitors user interactions with the system's outputs (PRs).

**Workflow**:
1.  **Trigger**: GitHub Action `on: pull_request_target`.
2.  **Event**:
    *   **Merged**: User accepted the intelligence. (Positive Signal +1)
    *   **Closed (Unmerged)**: User rejected the intelligence. (Negative Signal -1)
3.  **Action**:
    *   Extract the `candidates.jsonl` data associated with the PR.
    *   Log the feedback to `knowledge/feedback/history.jsonl`:
        ```json
        {
          "timestamp": "2026-02-16T12:00:00Z",
          "pr_id": 42,
          "action": "merged",
          "candidates": ["n8n-io-n8n"],
          "score_components": {"stars": 174692, "forks": 54878, "days": 0}
        }
        ```

## III. The Reflector Algorithm (反思者算法)
### From Binary Signal to Weight Adjustment (从二元信号到权重调整)
The Reflector runs weekly (e.g., Sunday 00:00 UTC) to analyze the feedback history and adjust the `harvester.py` weights.

**Core Logic**:
1.  **Baseline**: Start with the "Factory Default" weights:
    *   `W_Stars = 30`
    *   `W_Forks = 10`
    *   `W_Time = 0.3`

2.  **Analysis**:
    *   If **High Star** projects are frequently rejected (Zombie Fatigue):
        *   `Delta_Stars = -0.5` (Decrease Star weight)
    *   If **Fresh** projects are frequently accepted (New Star Hunter):
        *   `Delta_Time = +0.05` (Increase Time weight)

3.  **Adjustment Formula**:
    ```python
    New_Weight = Current_Weight + (Learning_Rate * Net_Feedback_Signal)
    # Clamp to safe ranges (e.g., Time Weight 0.1 - 1.0)
    ```

4.  **Decay**: Apply a slight decay towards the baseline to prevent extreme skewing over time.

## IV. Risk Mitigation Strategy (风险对冲方案)
### The "Factory Reset" Button (一键重置)
If the system "learns wrong" (e.g., over-optimizing for freshness and ignoring stability), we must have a fail-safe.

**Mechanism**:
1.  **Configuration File**: Move all hardcoded weights to `brain_config.json`.
2.  **Version Control**: Commit `brain_config.json` changes to git.
3.  **Reset Protocol**:
    *   A manual dispatch workflow `reset-brain.yml`.
    *   Action: Reverts `brain_config.json` to the "Golden Master" (2026-02-16 Snapshot).
    *   Effect: Instantly restores the proven `30/10/0.3` formula.

## V. Implementation Roadmap (实施路线图)

### Phase 1: The Sensor (Sensors)
- [ ] Create `knowledge/feedback/` directory.
- [ ] Implement `log_feedback.py` script.
- [ ] Add GitHub Action `feedback_loop.yml` to capture PR outcomes.

### Phase 2: The Brain (Reflector)
- [ ] Extract weights to `brain_config.json`.
- [ ] Implement `reflector.py` to analyze feedback logs.
- [ ] Implement the weight adjustment algorithm with safety clamps.

### Phase 3: The Auto-Pilot (Curator)
- [ ] Enable `evolution.py` to auto-commit high-confidence entities (>350 score) without PR.
- [ ] Enable "rejection learning" to filter future candidates.

---
**Status**: Blueprint Drafted. Awaiting Approval for Phase 1.
