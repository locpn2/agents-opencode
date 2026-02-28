# OpenCode Agents & Skills

> 109 specialized agents and 146 skills for OpenCode - converted from Claude Code workflows

A comprehensive collection of AI agents and skills optimized for [OpenCode](https://opencode.ai), containing specialized experts across software development, infrastructure, security, AI/ML, and more.

## Overview

This repository provides ready-to-use agents and skills for OpenCode:

- **109 Specialized Agents** - Domain experts for Python, JavaScript, Go, Rust, security, DevOps, AI/ML, and more
- **146 Skills** - Modular knowledge packages with progressive disclosure for specialized expertise
- **OpenCode Native** - Optimized for OpenCode's agent and skill system

## Quick Start

### Option 1: Clone and Use

```bash
git clone https://github.com/locpn2/agents-opencode.git
cd agents-opencode
opencode
```

OpenCode will automatically discover agents in `.opencode/agents/` and skills in `.opencode/skills/`.

### Option 2: Copy to Your Project

Copy agents and skills to your project's `.opencode/` directory:

```bash
# Copy agents
cp -r agents-opencode/.opencode/agents/ your-project/.opencode/

# Copy skills
cp -r agents-opencode/.opencode/skills/ your-project/.opencode/
```

### Option 3: Global Installation

Copy to your global OpenCode config:

```bash
# Agents
cp -r .opencode/agents/* ~/.config/opencode/agents/

# Skills
cp -r .opencode/skills/* ~/.config/opencode/skills/
```

## Usage

### Invoking Agents

Use the `@` mention to invoke a subagent:

```
@python-pro help me create a FastAPI application
@security-auditor review this code for vulnerabilities
@data-engineer design an ETL pipeline
```

### Loading Skills

Skills are automatically discovered and available via the skill tool:

```
skill({ name: "async-python-patterns" })
skill({ name: "rag-implementation" })
skill({ name: "k8s-manifest-generator" })
```

## Available Agents

### Language Experts
| Agent | Description |
|-------|-------------|
| `python-pro` | Master Python 3.12+ with async, FastAPI, Django |
| `javascript-pro` | Modern JavaScript and ES6+ development |
| `typescript-pro` | TypeScript with advanced types |
| `golang-pro` | Go systems programming |
| `rust-pro` | Rust for systems programming |
| `java-pro` | Java enterprise development |
| `csharp-pro` | C# and .NET development |

### Architecture & Backend
| Agent | Description |
|-------|-------------|
| `backend-architect` | Backend architecture design |
| `api-architect` | REST API and GraphQL design |
| `database-architect` | Database schema and SQL optimization |
| `cloud-architect` | Cloud infrastructure (AWS/Azure/GCP) |
| `kubernetes-architect` | Kubernetes deployments |

### Security
| Agent | Description |
|-------|-------------|
| `security-auditor` | Security vulnerability assessment |
| `backend-security-coder` | Backend security implementation |
| `frontend-security-coder` | Frontend security best practices |

### Quality & Testing
| Agent | Description |
|-------|-------------|
| `code-reviewer` | Code quality review |
| `test-automator` | Test automation with pytest |
| `performance-engineer` | Performance optimization |

### DevOps & Infrastructure
| Agent | Description |
|-------|-------------|
| `deployment-engineer` | Deployment automation |
| `terraform-specialist` | Infrastructure as Code |
| `devops-troubleshooter` | DevOps troubleshooting |

### AI/ML
| Agent | Description |
|-------|-------------|
| `ai-engineer` | LLM application development |
| `data-engineer` | Data engineering pipelines |
| `ml-engineer` | Machine learning development |
| `prompt-engineer` | Prompt engineering |

## Available Skills

### Python Skills
- `async-python-patterns` - Async/await patterns
- `python-testing-patterns` - pytest best practices
- `python-design-patterns` - Design patterns in Python
- `python-packaging` - Python packaging with uv

### JavaScript/TypeScript Skills
- `typescript-advanced-types` - Advanced TypeScript
- `nodejs-backend-patterns` - Node.js patterns
- `javascript-testing-patterns` - JS testing

### Infrastructure Skills
- `k8s-manifest-generator` - Kubernetes manifests
- `helm-chart-scaffolding` - Helm charts
- `terraform-module-library` - Terraform modules
- `gitops-workflow` - GitOps workflows

### AI/ML Skills
- `rag-implementation` - RAG systems
- `langchain-architecture` - LangChain patterns
- `prompt-engineering-patterns` - Prompt engineering
- `embedding-strategies` - Embedding strategies
- `vector-index-tuning` - Vector database tuning

### Security Skills
- `sast-configuration` - SAST scanning
- `stride-analysis-patterns` - STRIDE threat modeling
- `security-requirement-extraction` - Security requirements

[→ View all 146 skills](docs/agent-skills.md)

## Directory Structure

```
agents-opencode/
├── .opencode/
│   ├── agents/           # 109 agents for OpenCode
│   │   ├── python-pro.md
│   │   ├── javascript-pro.md
│   │   └── ...
│   └── skills/          # 146 skills
│       ├── async-python-patterns/
│       │   └── SKILL.md
│       ├── rag-implementation/
│       │   └── SKILL.md
│       └── ...
├── .claude/
│   └── skills/          # Claude-compatible skills
├── AGENTS.md            # OpenCode project descriptor
├── README.md            # This file
└── docs/                # Documentation
```

## Configuration

### Global Agents

Place agent files in `~/.config/opencode/agents/`:

```bash
mkdir -p ~/.config/opencode/agents
cp agents-opencode/.opencode/agents/* ~/.config/opencode/agents/
```

### Global Skills

Place skill folders in `~/.config/opencode/skills/`:

```bash
mkdir -p ~/.config/opencode/skills
cp -r agents-opencode/.opencode/skills/* ~/.config/opencode/skills/
```

### Project-Specific

Copy to your project's `.opencode/` directory:

```bash
cp -r agents-opencode/.opencode/ your-project/
```

## Migration Notes

This project was converted from [wshobson/agents](https://github.com/wshobson/agents) - a Claude Code plugins system. The original project contains 72 plugins with 112 agents and 146 skills.

## Documentation

- [Agent Reference](docs/agents.md) - All 109 agents
- [Skills Reference](docs/agent-skills.md) - All 146 skills
- [OpenCode Docs](https://opencode.ai/docs) - OpenCode documentation

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=locpn2/agents-opencode&type=Date&legend=top-left)](https://www.star-history.com/#locpn2/agents-opencode&type=Date&legend=top-left)
