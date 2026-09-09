# browser-use/browser-use · README.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [browser-use/browser-use](https://github.com/browser-use/browser-use) |
| 来源文件 | [README.md](https://github.com/browser-use/browser-use/blob/50f205533fe10ba35b553d2a3689c77b87bd5d0a/README.md) |
| 来源版本 | `50f205533fe10ba35b553d2a3689c77b87bd5d0a` |
| 来源目录 Tree | `5b421afc2d985329ebb09cd6177430113b14c302` |
| 来源内容 Blob | `2a3c0208abf29df21b5ceacfd9fdc4d88df6e40b` |
| 摄取时间 | `2026-09-09T23:51:26.684197+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_browser_use_browser_use_readme_md` |

## 本次变化

- 新增行数 `198`.
- 删除行数 `188`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- Navigate the web like a human does.
- Which Browser Use do I need?
- Quickstart
- Path 1: Fully Hosted Cloud
- Path 2: CLI
- Path 3: Python Library
- .env
- BROWSER_USE_API_KEY=your-key  # Optional: BU2 model or cloud browser
- Browser Use Benchmark v2
- Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)
- FAQ
- Related Repositories
- Citation

<details>
<summary>展开完整外部原文</summary>

<!-- mcp-name: com.browser-use/browser-use -->
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/2ccdb752-22fb-41c7-8948-857fc1ad7e24">
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/774a46d5-27a0-490c-b7d0-e65fcbbfa358">
  <img alt="Shows a black Browser Use Logo in light color mode and a white one in dark color mode." src="https://github.com/user-attachments/assets/2ccdb752-22fb-41c7-8948-857fc1ad7e24"  width="full">
</picture>

<div align="center">
    <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/9955dda9-ede3-4971-8ee0-91cbc3850125">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6797d09b-8ac3-4cb9-ba07-b289e080765a">
    <img alt="The AI browser agent." src="https://github.com/user-attachments/assets/9955dda9-ede3-4971-8ee0-91cbc3850125"  width="400">
    </picture>
</div>

<div align="center">
<a href="https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-downloads"><img src="https://media.browser-use.tools/badges/package" height="48" alt="Browser-Use Package Download Statistics"></a>
</div>

---

<div align="center">
<a href="#navigate-the-web-like-a-human-does"><img src="https://media.browser-use.tools/badges/demos" alt="Demos"></a>
<img width="16" height="1" alt="">
<a href="https://docs.browser-use.com"><img src="https://media.browser-use.tools/badges/docs" alt="Docs"></a>
<img width="16" height="1" alt="">
<a href="https://browser-use.com/posts"><img src="https://media.browser-use.tools/badges/blog" alt="Blog"></a>
<img width="16" height="1" alt="">
<a href="https://browsermerch.com"><img src="https://media.browser-use.tools/badges/merch" alt="Merch"></a>
<img width="100" height="1" alt="">
<a href="https://github.com/browser-use/browser-use"><img src="https://media.browser-use.tools/badges/github" alt="Github Stars"></a>
<img width="4" height="1" alt="">
<a href="https://x.com/intent/user?screen_name=browser_use"><img src="https://media.browser-use.tools/badges/twitter" alt="Twitter"></a>
<img width="4" height="1" alt="">
<a href="https://link.browser-use.com/discord"><img src="https://media.browser-use.tools/badges/discord" alt="Discord"></a>
<img width="4" height="1" alt="">
<a href="https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-cloud"><img src="https://media.browser-use.tools/badges/cloud" height="48" alt="Browser-Use Cloud"></a>
</div>

<br/>

<div align="center">
  <a href="https://browser-use.com">
    <img src="https://browser-use.com/lander/plates/browsers-8dd60aa0.jpg" alt="A person crossing an orange canyon on a giant key-shaped bridge, from the Browser Use website." width="720">
  </a>
</div>

<br/>

# Navigate the web like a human does.

Find an available slot, pick a date and time, handle the CAPTCHA, and book a driving test.

![Browser Use V4 booking a driving test](https://github.com/user-attachments/assets/135885e8-1141-4e10-b719-bf690ae7d260)

[Explore more demos and prompts ↗](https://browser-use.com/showcase)

<br/>

# Which Browser Use do I need?

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="static/readme/which-product-dark.svg">
  <img alt="Three ways to use Browser Use: fully hosted cloud; your existing agent with Browser Use CLI; or the open source Browser Use agent, available as a Python library. The CLI and library each connect to a local or cloud browser." src="static/readme/which-product-light.svg" width="100%">
</picture>

- **[Path 1: Fully Hosted Cloud](#path-1-fully-hosted-cloud):** Scale up with a fully hosted agent and browser.
- **[Path 2: CLI](#path-2-cli):** Automate your own browser tasks.
- **[Path 3: Python Library](#path-3-python-library):** Run the open source Browser Use agent locally from your own code.

# Quickstart

## Path 1: Fully Hosted Cloud

Scale browser automation with our hosted agent, stealth browsers, and infrastructure for profiles, recordings, and data policies.

[Get started with the API ↗](https://docs.browser-use.com/cloud/agent/quickstart)

New Google, GitHub, or Microsoft signups get **$15 cloud credit**.

<br/>

## Path 2: CLI

Paste this prompt into Claude Code, Codex, Hermes, OpenClaw, or your favorite agent.

```text
Install or upgrade browser-use to the latest stable version with uv using Python 3.12, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, follow https://github.com/browser-use/browser-harness/blob/main/install.md.
```

<br/>

## Path 3: Python Library

Run the Browser Use agent locally from Python, with your choice of model and a local or cloud browser:

**1. Install Browser Use (Python >= 3.11):**

With [uv](https://docs.astral.sh/uv/getting-started/installation/) installed, run `uv init --python 3.12` first if you're starting a new project.

```bash
uv add browser-use
```

**2. Add your [OpenAI API key](https://platform.openai.com/api-keys) to `.env`:**

```bash
# .env
OPENAI_API_KEY=your-key
# BROWSER_USE_API_KEY=your-key  # Optional: BU2 model or cloud browser
```

For either optional Browser Use service, get a [Browser Use API key](https://cloud.browser-use.com/new-api-key).

**3. Save this as `agent.py`:**

```python
import asyncio

from browser_use import Agent, Browser, ChatBrowserUse, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

async def main():
    llm = ChatOpenAI(model='gpt-5.6-luna', reasoning_effort='xhigh')
    # llm = ChatBrowserUse(model='bu-2-0')  # Use BU2 instead; requires BROWSER_USE_API_KEY
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=llm,
        # browser=Browser(use_cloud=True),  # Use a cloud browser; requires BROWSER_USE_API_KEY
    )
    history = await agent.run()
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())
```

To use BU2, replace the `ChatOpenAI` line with the commented `ChatBrowserUse` line. The cloud-browser option works with either model.

**4. Run it:**

```bash
uv run agent.py
```

The agent opens a browser, looks up the repository, and prints its answer.

[Python library docs ↗](https://docs.browser-use.com/open-source/introduction)

<br/>

# Browser Use Benchmark v2

<img alt="Browser Use Benchmark v2 - Mean rubric score by model and cost per task" src="static/hard_benchmark_v2.jpg" width="100%">

This [very hard benchmark](https://github.com/browser-use/benchmark) targets the hardest browser tasks. On easier tasks, even smaller models can achieve very high success rates. Results shown are from a 60-task subset of BU Bench V2.

## Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)

<br/>

# FAQ

<details>
<summary><b>Should I use the fully hosted cloud, CLI, or Python library?</b></summary>

- **[Fully Hosted Cloud](#path-1-fully-hosted-cloud):** Send tasks through the API and let Browser Use run the agent, browser, and infrastructure.
- **[CLI](#path-2-cli):** Give an existing agent (Claude Code, Codex, Hermes, OpenClaw, Pi, Cursor, etc.) browser access. You can use it interactively or in scripts.
- **[Python Library](#path-3-python-library):** Run the open source agent in your own application, with custom tools, structured output, and your choice of model.

The CLI and Python library can each connect to a local or cloud browser. A cloud browser hosts the browser; the fully hosted API runs the agent as well.
</details>

<details>
<summary><b>What's the best model to use?</b></summary>

We recommend **BU2**, our model optimized for browser automation: `ChatBrowserUse(model='bu-2-0')`. It uses `BROWSER_USE_API_KEY`; `ChatBrowserUse()` currently selects the same model.

The best choice depends on your tasks, latency, and budget. See the [BU2 model card](https://docs.browser-use.com/open-source/bu-2-0-model-card), [benchmark](https://github.com/browser-use/benchmark), and [supported models and pricing](https://docs.browser-use.com/open-source/supported-models) to compare options.
</details>

<details>
<summary><b>Can I use Claude / GPT / Gemini through ChatBrowserUse?</b></summary>

Yes. `ChatBrowserUse` accepts provider-prefixed model IDs through the Browser Use gateway, using `BROWSER_USE_API_KEY`:

```python
from browser_use import Agent, ChatBrowserUse

llm = ChatBrowserUse(model='anthropic/claude-sonnet-4-6')  # or 'google/gemini-3-pro'
agent = Agent(task='...', llm=llm)
```

You can also use providers directly through wrappers such as `ChatOpenAI`, `ChatAnthropic`, and `ChatGoogle`, with each provider's own API key. See [supported models](https://docs.browser-use.com/open-source/supported-models).
</details>

<details>
<summary><b>Do I need to provide a system prompt?</b></summary>

No. `Agent(...)` supplies the Browser Use system prompt automatically, including when you change models. Put your task in `task=`. Use `extend_system_message` to add instructions or `override_system_message` to replace the default prompt when you need custom behavior.

See the [custom system prompt example](https://github.com/browser-use/browser-use/blob/main/examples/features/custom_system_prompt.py).
</details>

<details>
<summary><b>Can I use custom tools with the agent?</b></summary>

Yes. Register a function with `Tools` and pass it to the agent. This example adds a tool for the current UTC time and uses `BROWSER_USE_API_KEY` from `.env`:

```python
import asyncio
from datetime import datetime, timezone

from browser_use import ActionResult, Agent, ChatBrowserUse, Tools
from dotenv import load_dotenv

load_dotenv()
tools = Tools()

@tools.action(description='Get the current date and time in UTC.')
def get_current_time() -> ActionResult:
    return ActionResult(extracted_content=datetime.now(timezone.utc).isoformat())

async def main():
    agent = Agent(
        task="What is the current UTC time?",
        llm=ChatBrowserUse(model='bu-2-0'),
        tools=tools,
    )
    history = await agent.run()
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())
```

</details>

<details>
<summary><b>Can I use this for free?</b></summary>

The Python library is free and [MIT-licensed](LICENSE). Model inference and hosted browsers are separate: API providers, including `ChatBrowserUse`, and Browser Use Cloud charge for usage. You can also use a local browser and a local model through [Ollama](https://docs.browser-use.com/open-source/supported-models#ollama), subject to your hardware and model requirements.
</details>

<details>
<summary><b>Terms of Service</b></summary>

This open-source library is licensed under the MIT License. For Browser Use services & data policy, see our [Terms of Service](https://browser-use.com/legal/terms-of-service) and [Privacy Policy](https://browser-use.com/privacy/).
</details>

<details>
<summary><b>How do I handle authentication?</b></summary>

- **Local browser:** Use `Browser.from_system_chrome()` to reuse a Chrome profile. See the [real-browser guide](https://docs.browser-use.com/open-source/customize/browser/real-browser) and [example](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py).
- **Cloud browser:** Follow the [profile sync guide](https://github.com/browser-use/browser-harness/blob/main/interaction-skills/profile-sync.md), then use `Browser(use_cloud=True, cloud_profile_id='your-profile-id')`.

Profile sync transfers cookies, not local storage, IndexedDB, or extensions. Some sites may require you to sign in again.
</details>

<details>
<summary><b>How do I solve CAPTCHAs?</b></summary>

[Browser Use Cloud](https://docs.browser-use.com/cloud/browser/quickstart) provides stealth browsers and proxies designed to reduce bot detection and CAPTCHA challenges. With the Python library, enable a cloud browser with `Browser(use_cloud=True)` and set `BROWSER_USE_API_KEY`.

Results depend on the site and challenge; no browser configuration guarantees that every CAPTCHA can be avoided or solved.
</details>

<details>
<summary><b>How do I go into production?</b></summary>

Choose how much you want to manage:

- **Keep your agent code:** Connect the CLI or Python library to [cloud browsers](https://docs.browser-use.com/cloud/browser/quickstart) for managed browser infrastructure, stealth, profiles, and recordings.
- **Have us run the agent too:** Use the [fully hosted Cloud API](https://docs.browser-use.com/cloud/agent/quickstart) to submit tasks and retrieve results.

You can also host the Python library and browsers on your own infrastructure.
</details>

<br/>

## Related Repositories

| Repository | What it's for |
| --- | --- |
| [Browser Harness](https://github.com/browser-use/browser-harness) | Our CLI for giving AI agents control of your browser. |
| [Browser Harness JS](https://github.com/browser-use/browser-harness-js) | Give your JavaScript agent control of a real browser. |
| [Browser Use Pi](https://github.com/browser-use/browser-use-pi) | Run a TypeScript browser agent built on Pi. |
| [Cloud SDK](https://github.com/browser-use/sdk) | Integrate Browser Use Cloud into your application. |
| [Video Use](https://github.com/browser-use/video-use) | Edit videos with your coding agent. |
| [macOS Harness](https://github.com/browser-use/macos-harness) | Give your agent control of Mac apps, browsers, and files. |
| [Benchmark](https://github.com/browser-use/benchmark) | Explore browser tasks and compare agent performance. |

<br/>

## Citation

If you use Browser Use in your research or project, please cite:

```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```

<br/>

<div align="center">

**Tell your computer what to do, and it gets it done.**

<img src="https://github.com/user-attachments/assets/06fa3078-8461-4560-b434-445510c1766f" width="400"/>

[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/intent/user?screen_name=mamagnus00)
&emsp;&emsp;&emsp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/intent/user?screen_name=gregpr07)

</div>

<div align="center"> Made with ❤️ in Zurich and San Francisco </div>

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 2a3c0208abf29df21b5ceacfd9fdc4d88df6e40b

@@ -20,7 +20,7 @@

 ---
 
 <div align="center">
-<a href="#what-can-browser-use-do"><img src="https://media.browser-use.tools/badges/demos" alt="Demos"></a>
+<a href="#navigate-the-web-like-a-human-does"><img src="https://media.browser-use.tools/badges/demos" alt="Demos"></a>
 <img width="16" height="1" alt="">
 <a href="https://docs.browser-use.com"><img src="https://media.browser-use.tools/badges/docs" alt="Docs"></a>
 <img width="16" height="1" alt="">
@@ -37,213 +37,211 @@

 <a href="https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-cloud"><img src="https://media.browser-use.tools/badges/cloud" height="48" alt="Browser-Use Cloud"></a>
 </div>
 
-</br>
-
-# What can Browser Use do?
-
-Browser Use lets an AI agent use a web browser the same way humans do — it opens pages, clicks buttons, types, and fills in forms. You describe the task, and it completes it. For example, you can have it:
-
-
-### 📋 Fill Forms
-#### Task: "Fill in this job application with my resume and information."
-
-![Job Application Demo](https://github.com/user-attachments/assets/57611d8e-0474-4de6-84b7-37a0c0cd27e7)
-
-[Example code ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/apply_to_job.py)
-
-
-### 🍎 Extract data
-#### Task: "Extract structured data about my followers and export it as a CSV."
-
-https://github.com/user-attachments/assets/485fd3ec-61b9-4afc-9e86-ee9b85acb592
-
-[Browser Use Cloud Docs ↗](https://docs.browser-use.com/cloud/quickstart)
-
-
-<br/>
-
-# Start with Browser Use Cloud
-
-Eligible new Google, GitHub or Microsoft signups get a one-time **$15 Cloud credit**. No card required; email/password signups do not qualify. [Pricing and eligibility](https://browser-use.com/pricing.md).
-
-- **Hosted agent:** [V4 quickstart](https://docs.browser-use.com/cloud/agent/quickstart), using `browser-use-sdk`.
-- **Your own agent:** [Managed browser quickstart](https://docs.browser-use.com/cloud/browser/quickstart).
-- **Local framework:** the `browser-use` Python library below.
+<br/>
+
+<div align="center">
+  <a href="https://browser-use.com">
+    <img src="https://browser-use.com/lander/plates/browsers-8dd60aa0.jpg" alt="A person crossing an orange canyon on a giant key-shaped bridge, from the Browser Use website." width="720">
+  </a>
+</div>
+
+<br/>
+
+# Navigate the web like a human does.
+
+Find an available slot, pick a date and time, handle the CAPTCHA, and book a driving test.
+
+![Browser Use V4 booking a driving test](https://github.com/user-attachments/assets/135885e8-1141-4e10-b719-bf690ae7d260)
+
+[Explore more demos and prompts ↗](https://browser-use.com/showcase)
+
+<br/>
+
+# Which Browser Use do I need?
+
+<picture>
+  <source media="(prefers-color-scheme: dark)" srcset="static/readme/which-product-dark.svg">
+  <img alt="Three ways to use Browser Use: fully hosted cloud; your existing agent with Browser Use CLI; or the open source Browser Use agent, available as a Python library. The CLI and library each connect to a local or cloud browser." src="static/readme/which-product-light.svg" width="100%">
+</picture>
+
+- **[Path 1: Fully Hosted Cloud](#path-1-fully-hosted-cloud):** Scale up with a fully hosted agent and browser.
+- **[Path 2: CLI](#path-2-cli):** Automate your own browser tasks.
+- **[Path 3: Python Library](#path-3-python-library):** Run the open source Browser Use agent locally from your own code.
 
 # Quickstart
 
-If you want to use Browser Use in your agent (Claude Code, Codex, Cursor, Hermes, OpenClaw, etc.), paste this prompt, and it sets everything up itself:
+## Path 1: Fully Hosted Cloud
+
+Scale browser automation with our hosted agent, stealth browsers, and infrastructure for profiles, recordings, and data policies.
+
+[Get started with the API ↗](https://docs.browser-use.com/cloud/agent/quickstart)
+
+New Google, GitHub, or Microsoft signups get **$15 cloud credit**.
+
+<br/>
+
+## Path 2: CLI
+
+Paste this prompt into Claude Code, Codex, Hermes, OpenClaw, or your favorite agent.
 
 ```text
 Install or upgrade browser-use to the latest stable version with uv using Python 3.12, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, follow https://github.com/browser-use/browser-harness/blob/main/install.md.
 ```
 
-Then tell your agent what you want done.
-
-<br/>
-
-# Python library: the easiest way to automate the web
-
-Want to automate the web at scale, from your own code, and with any LLM? Use the Python library:
+<br/>
+
+## Path 3: Python Library
+
+Run the Browser Use agent locally from Python, with your choice of model and a local or cloud browser:
 
 **1. Install Browser Use (Python >= 3.11):**
+
+With [uv](https://docs.astral.sh/uv/getting-started/installation/) installed, run `uv init --python 3.12` first if you're starting a new project.
 
 ```bash
 uv add browser-use
-# or: pip install browser-use
-```
-
-**2. Add your LLM API key to `.env`**. Get one from [Browser Use Cloud](https://cloud.browser-use.com/new-api-key?utm_source=github&utm_medium=readme-quickstart-api-key), or bring your own provider key:
+```
+
+**2. Add your [OpenAI API key](https://platform.openai.com/api-keys) to `.env`:**
 
 ```bash
 # .env
-BROWSER_USE_API_KEY=your-key
-# GOOGLE_API_KEY=your-key
-# ANTHROPIC_API_KEY=your-key
-```
-
-**3. Run your first agent:**
+OPENAI_API_KEY=your-key
+# BROWSER_USE_API_KEY=your-key  # Optional: BU2 model or cloud browser
+```
+
+For either optional Browser Use service, get a [Browser Use API key](https://cloud.browser-use.com/new-api-key).
+
+**3. Save this as `agent.py`:**
 
 ```python
 import asyncio
 
+from browser_use import Agent, Browser, ChatBrowserUse, ChatOpenAI
+from dotenv import load_dotenv
+
+load_dotenv()
+
+async def main():
+    llm = ChatOpenAI(model='gpt-5.6-luna', reasoning_effort='xhigh')
+    # llm = ChatBrowserUse(model='bu-2-0')  # Use BU2 instead; requires BROWSER_USE_API_KEY
+    agent = Agent(
+        task="Find the number of stars of the browser-use repo",
+        llm=llm,
+        # browser=Browser(use_cloud=True),  # Use a cloud browser; requires BROWSER_USE_API_KEY
+    )
+    history = await agent.run()
+    print(history.final_result())
+
+if __name__ == "__main__":
+    asyncio.run(main())
+```
+
+To use BU2, replace the `ChatOpenAI` line with the commented `ChatBrowserUse` line. The cloud-browser option works with either model.
+
+**4. Run it:**
+
+```bash
+uv run agent.py
+```
+
+The agent opens a browser, looks up the repository, and prints its answer.
+
+[Python library docs ↗](https://docs.browser-use.com/open-source/introduction)
+
+<br/>
+
+# Browser Use Benchmark v2
+
+<img alt="Browser Use Benchmark v2 - Mean rubric score by model and cost per task" src="static/hard_benchmark_v2.jpg" width="100%">
+
+This [very hard benchmark](https://github.com/browser-use/benchmark) targets the hardest browser tasks. On easier tasks, even smaller models can achieve very high success rates. Results shown are from a 60-task subset of BU Bench V2.
+
+## Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)
+
+<br/>
+
+# FAQ
+
+<details>
+<summary><b>Should I use the fully hosted cloud, CLI, or Python library?</b></summary>
+
+- **[Fully Hosted Cloud](#path-1-fully-hosted-cloud):** Send tasks through the API and let Browser Use run the agent, browser, and infrastructure.
+- **[CLI](#path-2-cli):** Give an existing agent (Claude Code, Codex, Hermes, OpenClaw, Pi, Cursor, etc.) browser access. You can use it interactively or in scripts.
+- **[Python Library](#path-3-python-library):** Run the open source agent in your own application, with custom tools, structured output, and your choice of model.
+
+The CLI and Python library can each connect to a local or cloud browser. A cloud browser hosts the browser; the fully hosted API runs the agent as well.
+</details>
+
+<details>
+<summary><b>What's the best model to use?</b></summary>
+
+We recommend **BU2**, our model optimized for browser automation: `ChatBrowserUse(model='bu-2-0')`. It uses `BROWSER_USE_API_KEY`; `ChatBrowserUse()` currently selects the same model.
+
+The best choice depends on your tasks, latency, and budget. See the [BU2 model card](https://docs.browser-use.com/open-source/bu-2-0-model-card), [benchmark](https://github.com/browser-use/benchmark), and [supported models and pricing](https://docs.browser-use.com/open-source/supported-models) to compare options.
+</details>
+
+<details>
+<summary><b>Can I use Claude / GPT / Gemini through ChatBrowserUse?</b></summary>
+
+Yes. `ChatBrowserUse` accepts provider-prefixed model IDs through the Browser Use gateway, using `BROWSER_USE_API_KEY`:
+
+```python
 from browser_use import Agent, ChatBrowserUse
+
+llm = ChatBrowserUse(model='anthropic/claude-sonnet-4-6')  # or 'google/gemini-3-pro'
+agent = Agent(task='...', llm=llm)
+```
+
+You can also use providers directly through wrappers such as `ChatOpenAI`, `ChatAnthropic`, and `ChatGoogle`, with each provider's own API key. See [supported models](https://docs.browser-use.com/open-source/supported-models).
+</details>
+
+<details>
+<summary><b>Do I need to provide a system prompt?</b></summary>
+
+No. `Agent(...)` supplies the Browser Use system prompt automatically, including when you change models. Put your task in `task=`. Use `extend_system_message` to add instructions or `override_system_message` to replace the default prompt when you need custom behavior.
+
+See the [custom system prompt example](https://github.com/browser-use/browser-use/blob/main/examples/features/custom_system_prompt.py).
+</details>
+
+<details>
+<summary><b>Can I use custom tools with the agent?</b></summary>
+
+Yes. Register a function with `Tools` and pass it to the agent. This example adds a tool for the current UTC time and uses `BROWSER_USE_API_KEY` from `.env`:
+
+```python
+import asyncio
+from datetime import datetime, timezone
+
+from browser_use import ActionResult, Agent, ChatBrowserUse, Tools
+from dotenv import load_dotenv
+
+load_dotenv()
+tools = Tools()
+
+@tools.action(description='Get the current date and time in UTC.')
+def get_current_time() -> ActionResult:
+    return ActionResult(extracted_content=datetime.now(timezone.utc).isoformat())
 
 async def main():
     agent = Agent(
-        task="Find the number of stars of the browser-use repo",
-        llm=ChatBrowserUse(model='openai/gpt-5.5'),
-        # llm=ChatBrowserUse(model='bu-2-0-mini-preview'),  # Browser Use's optimized model
-        # llm=ChatOpenAI(model='gpt-5.5'),
-        # llm=ChatAnthropic(model='claude-opus-4-8'),  # Sonnet also works well
+        task="What is the current UTC time?",
+        llm=ChatBrowserUse(model='bu-2-0'),
+        tools=tools,
     )
     history = await agent.run()
+    print(history.final_result())
 
 if __name__ == "__main__":
     asyncio.run(main())
 ```
 
-Check out the [library docs](https://docs.browser-use.com/open-source/introduction) and the [cloud docs](https://docs.cloud.browser-use.com?utm_source=github&utm_medium=readme-cloud-docs) for more!
-
-<br/>
-
-# Open Source vs Cloud
-
-<picture>
-  <source media="(prefers-color-scheme: light)" srcset="static/accuracy_by_model_light.png">
-  <source media="(prefers-color-scheme: dark)" srcset="static/accuracy_by_model_dark.png">
-  <img alt="BU Bench V1 - LLM Success Rates" src="static/accuracy_by_model_light.png" width="100%">
-</picture>
-
-We benchmark Browser Use across 100 real-world browser tasks. Full benchmark is open source: **[browser-use/benchmark](https://github.com/browser-use/benchmark)**.
-
-Browser Use is also **#1 on the [Odysseys leaderboard](https://odysseysbench.com/leaderboard)** with an 87.4% average, ahead of computer-use agents from OpenAI, Anthropic, Google, and Microsoft. Odysseys measures the agent's performance on 200 long-horizon web tasks.
-
-**Use the Open-Source Agent**
-- Free, and runs on your own machine
-- Deep code-level integration and control: pick your LLM, customize the agent's behavior
-- We recommend pairing it with our [cloud browsers](https://docs.browser-use.com/open-source/customize/browser/remote) for leading stealth, proxy rotation, and scaling
-
-**Use the [Fully-Hosted Cloud Agent](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-hosted-agent) (recommended)**
-- Much more powerful agent for complex tasks (see plot above)
-- Easiest way to start and scale
-- Best stealth with proxy rotation and captcha solving
-- 1000+ integrations (Gmail, Slack, Notion, and more)
-- Persistent filesystem and memory
-- Rerunnable scripts fetch live data, even when sites change ([guide](https://docs.browser-use.com/cloud/agent/scripts))
-
-```sh
-curl -X POST https://api.browser-use.com/api/v4/runs \
-  -H "X-Browser-Use-API-Key: $BROWSER_USE_API_KEY" \
-  -H "Content-Type: application/json" \
-  -d '{"task": "Your task"}'
-```
-
-<br/>
-
-## Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)
-
-<br/>
-
-# FAQ
-
-<details>
-<summary><b>Should I use the CLI vs. the Python library?</b></summary>
-
-**Use the CLI** if you already have an agent (Claude Code, Codex, Cursor, Hermes, OpenClaw, etc.) that you want to complete browser tasks for you. The agent installs the skill once (see [Quickstart](#quickstart)) and can then control the browser. Examples:
-- "Upload this video to YouTube"
-- "Compare these three laptops and give me a table with prices"
-- "Fill in this job application with my resume"
-
-**Use the Python library** when you are building software that automates the web. Examples:
-- Run many tasks on a schedule or in parallel (scraping, monitoring, QA)
-- Embed a browser agent into your own product
-- Custom tools, custom system prompts, structured output, fine-grained browser control
-
-Rule of thumb: one-off tasks through an agent → CLI. Repeatable automation in code → Python library.
-</details>
-
-<details>
-<summary><b>What's the best model to use?</b></summary>
-
-We optimized **ChatBrowserUse()** specifically for browser automation tasks. On avg it completes tasks 3-5x faster than other models with SOTA accuracy.
-
-For pricing and other LLM providers, see our [supported models documentation](https://docs.browser-use.com/supported-models).
-</details>
-
-<details>
-<summary><b>Can I use Claude / GPT / Gemini through ChatBrowserUse?</b></summary>
-
-Yes. `ChatBrowserUse` accepts provider-prefixed model ids, so a single `BROWSER_USE_API_KEY` reaches all of them — no separate OpenAI/Anthropic/Google keys required:
-
-```python
-from browser_use import Agent, ChatBrowserUse
-
-llm = ChatBrowserUse(model='anthropic/claude-sonnet-4-6')  # or 'openai/gpt-5.5', 'google/gemini-3-pro'
-agent = Agent(task='...', llm=llm)
-```
-
-For the best speed and cost we still recommend the default `bu-*` models.
-</details>
-
-<details>
-<summary><b>Should I use the Browser Use system prompt with the open-source preview model?</b></summary>
-
-Yes. If you use `ChatBrowserUse(model='browser-use/bu-30b-a3b-preview')` with a normal `Agent(...)`, Browser Use still sends its default agent system prompt for you.
-
-You do **not** need to add a separate custom "Browser Use system message" just because you switched to the open-source preview model. Only use `extend_system_message` or `override_system_message` when you intentionally want to customize the default behavior for your task.
-
-If you want the best default speed/accuracy, we still recommend the newer hosted `bu-*` models. If you want the open-source preview model, the setup stays the same apart from the `model=` value.
-</details>
-
-<details>
-<summary><b>Can I use custom tools with the agent?</b></summary>
-
-Yes! You can add custom tools to extend the agent's capabilities:
-
-```python
-from browser_use import Tools
-
-tools = Tools()
-
-@tools.action(description='Description of what this tool does.')
-def custom_tool(param: str) -> str:
-    return f"Result: {param}"
-
-agent = Agent(
-    task="Your task",
-    llm=llm,
-    browser=browser,
-    tools=tools,
-)
-```
-
 </details>
 
 <details>
 <summary><b>Can I use this for free?</b></summary>
 
-Yes! Browser-Use is open source and free to use. You only need to choose an LLM provider (like OpenAI, Google, ChatBrowserUse, or run local models with Ollama).
+The Python library is free and [MIT-licensed](LICENSE). Model inference and hosted browsers are separate: API providers, including `ChatBrowserUse`, and Browser Use Cloud charge for usage. You can also use a local browser and a local model through [Ollama](https://docs.browser-use.com/open-source/supported-models#ollama), subject to your hardware and model requirements.
 </details>
 
 <details>
@@ -255,32 +253,44 @@

 <details>
 <summary><b>How do I handle authentication?</b></summary>
 
-Check out our authentication examples:
-- [Using real browser profiles](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py) - Reuse your existing Chrome profile with saved logins
-- If you want to use temporary accounts with inbox, choose AgentMail
-- To sync your auth profile with a remote browser, install `profile-use` for your platform from the [official releases](https://github.com/browser-use/profile-use-releases/releases/latest), then follow the [profile sync guide](https://github.com/browser-use/browser-harness/blob/main/interaction-skills/profile-sync.md).
-
-These examples show how to maintain sessions and handle authentication seamlessly.
+- **Local browser:** Use `Browser.from_system_chrome()` to reuse a Chrome profile. See the [real-browser guide](https://docs.browser-use.com/open-source/customize/browser/real-browser) and [example](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py).
+- **Cloud browser:** Follow the [profile sync guide](https://github.com/browser-use/browser-harness/blob/main/interaction-skills/profile-sync.md), then use `Browser(use_cloud=True, cloud_profile_id='your-profile-id')`.
+
+Profile sync transfers cookies, not local storage, IndexedDB, or extensions. Some sites may require you to sign in again.
 </details>
 
 <details>
 <summary><b>How do I solve CAPTCHAs?</b></summary>
 
-For CAPTCHA handling, you need better browser fingerprinting and proxies. Use [Browser Use Cloud](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-faq-captcha) which provides stealth browsers designed to avoid detection and CAPTCHA challenges.
+[Browser Use Cloud](https://docs.browser-use.com/cloud/browser/quickstart) provides stealth browsers and proxies designed to reduce bot detection and CAPTCHA challenges. With the Python library, enable a cloud browser with `Browser(use_cloud=True)` and set `BROWSER_USE_API_KEY`.
+
+Results depend on the site and challenge; no browser configuration guarantees that every CAPTCHA can be avoided or solved.
 </details>
 
 <details>
 <summary><b>How do I go into production?</b></summary>
 
-Chrome can consume a lot of memory, and running many agents in parallel can be tricky to manage.
-
-For production use cases, use our [Browser Use Cloud API](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-faq-production) which handles:
-- Scalable browser infrastructure
-- Memory management
-- Proxy rotation
-- Stealth browser fingerprinting
-- High-performance parallel execution
-</details>
+Choose how much you want to manage:
+
+- **Keep your agent code:** Connect the CLI or Python library to [cloud browsers](https://docs.browser-use.com/cloud/browser/quickstart) for managed browser infrastructure, stealth, profiles, and recordings.
+- **Have us run the agent too:** Use the [fully hosted Cloud API](https://docs.browser-use.com/cloud/agent/quickstart) to submit tasks and retrieve results.
+
+You can also host the Python library and browsers on your own infrastructure.
+</details>
+
+<br/>
+
+## Related Repositories
+
+| Repository | What it's for |
+| --- | --- |
+| [Browser Harness](https://github.com/browser-use/browser-harness) | Our CLI for giving AI agents control of your browser. |
+| [Browser Harness JS](https://github.com/browser-use/browser-harness-js) | Give your JavaScript agent control of a real browser. |
+| [Browser Use Pi](https://github.com/browser-use/browser-use-pi) | Run a TypeScript browser agent built on Pi. |
+| [Cloud SDK](https://github.com/browser-use/sdk) | Integrate Browser Use Cloud into your application. |
+| [Video Use](https://github.com/browser-use/video-use) | Edit videos with your coding agent. |
+| [macOS Harness](https://github.com/browser-use/macos-harness) | Give your agent control of Mac apps, browsers, and files. |
+| [Benchmark](https://github.com/browser-use/benchmark) | Explore browser tasks and compare agent performance. |
 
 <br/>
```

</details>
