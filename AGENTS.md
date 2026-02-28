# OpenCode Agents and Skills

This project contains 109 specialized agents and 146 skills converted from the Claude Code workflows project (wshobson/agents).

## Available Agents

### Language Experts
- `python-pro` - Master Python 3.12+ with modern features
- `django-pro` - Django web development expert
- `fastapi-pro` - FastAPI REST API expert
- `javascript-pro` - Modern JavaScript development
- `typescript-pro` - TypeScript expert
- `golang-pro` - Go systems programming
- `rust-pro` - Rust systems programming
- `csharp-pro` - C# and .NET development
- `java-pro` - Java enterprise development
- `scala-pro` - Scala functional programming

### Architecture & Backend
- `backend-architect` - Backend architecture design
- `api-architect` - API design and GraphQL
- `database-architect` - Database schema design
- `cloud-architect` - Cloud infrastructure design
- `kubernetes-architect` - Kubernetes deployments

### Security
- `security-auditor` - Security vulnerability assessment
- `backend-security-coder` - Backend security implementation
- `frontend-security-coder` - Frontend security best practices

### Quality & Testing
- `code-reviewer` - Code quality review
- `test-automator` - Test automation
- `performance-engineer` - Performance optimization

### DevOps & Infrastructure
- `deployment-engineer` - Deployment automation
- `terraform-specialist` - Infrastructure as Code
- `devops-troubleshooter` - DevOps troubleshooting

### Specialization
- `ai-engineer` - AI/LLM application development
- `data-engineer` - Data engineering pipelines
- `ml-engineer` - Machine learning development

## Available Skills

### Python Skills
- `async-python-patterns` - Async/await patterns
- `python-testing-patterns` - pytest best practices
- `python-design-patterns` - Design patterns in Python

### JavaScript/TypeScript Skills
- `typescript-advanced-types` - Advanced TypeScript
- `nodejs-backend-patterns` - Node.js patterns

### Infrastructure Skills
- `k8s-manifest-generator` - Kubernetes manifests
- `helm-chart-scaffolding` - Helm charts
- `terraform-module-library` - Terraform modules

### AI/ML Skills
- `rag-implementation` - RAG systems
- `langchain-architecture` - LangChain patterns
- `prompt-engineering-patterns` - Prompt engineering

## Usage

### Invoking Agents
Use the `@` mention to invoke a subagent:
```
@python-pro help me with async patterns
```

### Loading Skills
Skills are automatically discovered. Use them with the skill tool:
```
skill({ name: "async-python-patterns" })
```

## Directory Structure

- `.opencode/agents/` - Agent definitions
- `.opencode/skills/` - Skill definitions
- `.claude/skills/` - Claude-compatible skill definitions

## Migration Notes

These agents and skills were converted from the Claude Code plugins system. The original project is available at: https://github.com/wshobson/agents
