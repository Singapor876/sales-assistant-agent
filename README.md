# 多智能体导购助手

这是一个用于学习和验证多智能体协作流程的导购助手项目。系统将用户输入处理、意图识别、普通聊天、商品导购、售后处理、历史记录和人工服务等职责拆分到不同智能体中，再通过工作流进行路由与组合。

## 当前状态

项目仍处于开发阶段，主要用于架构实验和功能验证，并非可直接用于生产环境的完整商城客服系统。

## 主要模块

- `agents/main_router_agent`：入口路由、状态管理和工作流编排
- `agents/chat_agent`：普通聊天场景
- `agents/shopping_agent`：商品导购相关处理
- `agents/after_sales_agent`：售后场景处理
- `agents/output_agent`：统一输出处理
- `agents/to_human_agent`：转人工服务流程
- `agents/main_router_agent/agents/history_agent`：Redis 与 PostgreSQL 历史记录
- `retriever`：商品或知识检索能力的扩展位置
- `web`：调试和接口入口

## 技术组成

- Python
- LangGraph / LangChain 风格工作流
- 通义千问兼容接口
- Redis
- PostgreSQL
- aiohttp

## 配置方法

复制环境变量模板：

```bash
cp .env.example .env
```

然后在本地 `.env` 中填写大模型、Redis 和 PostgreSQL 配置。请勿提交真实 API Key、密码或 Token。

## 安装依赖

```bash
python -m venv .venv
```

Windows：

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux 或 macOS：

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## 运行方式

调试工作流：

```bash
python web/debugger.py
```

启动 Web 接口：

```bash
python web/main.py
```

部分子智能体还提供独立接口，具体入口请查看相应目录中的 Python 文件。

## 安全说明

- 公开版本仅提供 `.env.example`，不包含真实环境变量。
- 部署前应为数据库和缓存设置独立账号及强密码。
- 大模型输出需要在业务侧增加权限、内容安全和人工复核机制。

## 文档来源说明

本说明根据当前仓库的代码结构重新整理。旧版说明曾参考其他项目文档，但原始参考链接尚未确认；确认后应在此处补充准确来源、作者和许可证信息。

