# Contributing to AgentScope Sovereign Swarm

We welcome contributions to the world's first Sovereign AI Intelligence Organization!

## How to Contribute
1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Branch**: Work on features in a new branch (e.g., `feature/new-agent-role`).
3. **Write Tests**: Ensure your new agent or tool passes in the `TesterAgent` logic.
4. **Submit a Pull Request**: Describe your changes and which version (v31+) you are targeting.

## Agent Standards
- All new agents must be registered in `agents/registry.py`.
- Tools must return `ServiceResponse` objects.
- System prompts must be optimized for token efficiency.

## Security
If you find a security vulnerability, please do NOT open a public issue. Email the architect directly.
