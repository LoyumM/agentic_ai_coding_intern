# Agentic AI coding intern


## Core structure
```text
Multi_agent_code_generation/
├── agents/
│   ├── graph.py          # LangGraph orchestration and flow logic
│   ├── nodes.py          # Python functions for Coder, Tester, and Debugger
│   ├── state.py          # TypedDict defining the 'AgentState'
│   └── prompts.py        # System instructions for Qwen and Phi
├── sandbox/
│   └── temp_script.py    # The file where code is written and executed
├── scripts/
│   └── run_agent.py      # Terminal entry point (CLI tool)
├── tests/
│   └── sample_tasks.py   # A few boilerplates to test the agent
├── config.py             # Model names and Ollama configurations
└── requirements.txt
```