# ℹ️ Intel: ModelEngine-Group/nexent v1.8.1
> Source: GitHub Releases
> Date: 2026-03-14T22:25:27.270843
> **Analysis**: 🔗 Agent-Protocol

## 📝 Summary
v1.8.1

## 🔍 Changelog (Extract)
# 🚀 Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

我们很高兴地宣布 **Nexent v1.8.1 LTS（长期支持版）** 正式发布！🎉

🌟 本次 **LTS 版本** 聚焦 **企业级稳定性、工具优化、新模型支持** 及 **多项 Bug 修复**，将作为长期维护版本提供安全性和功能更新支持，推荐企业和生产环境使用。

We are excited to announce that **Nexent v1.8.1 LTS (Long-Term Support)** is released! 🎉

🌟 This **LTS release** focuses on **enterprise-level stability, tool enhancements, new model support**, and **multiple bug fixes**, and will be maintained with security and functionality updates for the long term. It is recommended for enterprise and production environments.

---

## 🔔 核心功能更新 / Key Enhancements

### 1️⃣ 模型提供商支持 / Provider Model Support

新增对 **Dashscope** 与 **Tokenpony** 模型的支持，可在智能体中直接调用，丰富了可用的 LLM 选择。

Support for **Dashscope** and **Tokenpony** models has been added, allowing agents to directly use these LLMs and expanding available model options.

### 2️⃣ 工具优化 / Tool & Search Improvements

* 新增 **idata search** 工具，提升信息检索能力。

* 文件预览功能后台服务上线，可在智能体中快速预览文件内容。

* 修复智能体中重复工具实例和工具选择逻辑问题，提高工具管理稳定性。

* Added **idata search** tool for better information retrieval.

* Backend service for file preview added, enabling quick file previews in agents.

* Fixed duplicate tool instances and tool selection issues in agents, improving tool management stability.

### 3️⃣ 调试体验增强 / Debugging Experience Enhancement

* 缓存调试错误信息，提高 TaskWindow 调试体验。

* SSE 流式消息优化，仅渲染当前助手消息，降低界面卡顿。

* Cached debug errors for improved TaskWindow debugging experience.

* SSE streaming optimized to render only the currently active assistant message, reducing UI lag.

### 4️⃣ Bug 修复与稳定性提升 / Bug Fixes & Stability Improvements

本次更新修复了包括 **MCP 容器启动错误提示、cookie 发送问题、租户账户管理、模型列表显示** 等多项问题，全面提升平台稳定性和可靠性。

This update fixes multiple issues, including **MCP container start errors, cookie sending problems, tenant account management, model list display**, and more, significantly improving platform stability and reliability.

---

## 🧭 特性预览 / Feature Preview

### 1️⃣ Skill 功能 / Skill Feature

Nexent 2.0 将推出 **Skill 功能体系**，支持将能力封装为可复用的 Skill 模块，并允许接入 **第三方 Skill**。用户可以快速集成外部能力或自定义技能，构建更加灵活和可扩展的智能体能力体系。

Nexent 2.0 will introduce a **Skill framework**, enabling capabilities to be packaged as reusable Skill modules while supporting integration of **third-party Skills**. Users can easily integrate external capabilities or custom skills to build a more flexible and extensible agent ecosystem.

---

### 2️⃣ RESTful 接口一键转 MCP / RESTful-to-MCP Integration

即将支持通过 **RESTful 接口一键转 MCP 接入**，可将现有 REST API 快速转换为 MCP 工具并接入 Nexent 智能体生态，大幅降低工具接入成本。

Support for **one-click RESTful-to-MCP integration** is coming soon, enabling existing REST APIs to be quickly converted into MCP tools and integrated into the Nexent agent ecosystem, significantly reducing tool integration effort.

---

### 3️⃣ 支持 K8s 集群部署 / Kubernetes Cluster Deployment

Nexent 2.0 将原生支持 **Kubernetes 集群部署**，支持企业级弹性扩展、高可用部署及统一运维管理，满足生产环境的大规模部署需求。

Nexent 2.0 will natively s
