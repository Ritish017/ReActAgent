# ðŸ¤– ReAct Agent with LangChain

A powerful **ReAct (Reasoning + Acting) Agent** implementation using LangChain and Groq's Mixtral model. This agent demonstrates how AI can reason through problems step-by-step and use tools to solve tasks.

## ðŸŒŸ Features

- **ðŸ§  Reasoning**: Step-by-step thinking process
- **ðŸ› ï¸ Tool Usage**: Executes custom Python functions
- **ðŸ”„ Iterative Problem Solving**: Can chain multiple actions
- **ðŸ“Š Transparent Process**: Shows complete reasoning trace
- **âš¡ Fast Inference**: Powered by Groq's Mixtral-8x7B model

## ðŸš€ What is ReAct?

ReAct is a paradigm that combines **Reasoning** and **Acting** in language models:

1. **ðŸ’­ Thought**: Agent reasons about the problem
2. **ðŸŽ¯ Action**: Agent selects and executes a tool
3. **ðŸ‘ï¸ Observation**: Agent observes the results
4. **ðŸ”„ Repeat**: Process continues until solution is found

## ðŸ“ Project Structure

```
ReActAgent/
â”œâ”€â”€ main.py              # Main ReAct agent implementation
â”œâ”€â”€ callbacks.py         # LangChain callback handlers  
â”œâ”€â”€ .env.example         # Environment variables template
â”œâ”€â”€ .gitignore          # Git ignore rules
â”œâ”€â”€ pyproject.toml      # UV project configuration
â”œâ”€â”€ README.md           # This file
â””â”€â”€ .venv/              # Virtual environment (UV managed)
```

## ðŸ› ï¸ Installation

### Prerequisites
- Python 3.13+
- [UV](https://docs.astral.sh/uv/) (ultra-fast Python package manager)
- Groq API Key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ReActAgent.git
   cd ReActAgent
   ```

2. **Install dependencies with UV**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your Groq API key
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the agent**
   ```bash
   uv run python main.py
   ```

## ðŸŽ¯ Usage

The agent currently includes one tool:
- **`get_text_length`**: Counts characters in text

### Example Interaction

```
Question: What is the text length of 'DOG' in characters?

Thought: I need to use the get_text_length tool to count the characters.
Action: get_text_length
Action Input: DOG
Observation: 3
Thought: I now know the final answer
Final Answer: The text length of 'DOG' is 3 characters.
```

## ðŸ”§ Code Structure

### Tool Definition
```python
@tool
def get_text_length(text: str) -> int:
    """Returns the Length of given text."""
    text = text.strip("'\n").strip('"')
    return len(text)
```

### ReAct Agent Pipeline
```python
agent = {
    "input": lambda x: x["input"], 
    "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"])
} | prompt | llm | ReActSingleInputOutputParser()
```

## ðŸ§ª Key Components Explained

### 1. **LangChain Tools**
- Convert Python functions to LLM-callable tools
- Automatic schema generation from type hints
- Input validation and error handling

### 2. **ReAct Prompt Template**
- Structured format for reasoning and acting
- Guides LLM through step-by-step process
- Prevents hallucination of tool outputs

### 3. **Groq Integration**
- Ultra-fast inference with Mixtral model
- Temperature=0 for consistent responses
- Stop tokens to control generation

### 4. **Agent Execution Loop**
- Handles `AgentAction` vs `AgentFinish` states
- Maintains conversation history in `intermediate_steps`
- Dynamic tool selection and execution

## ðŸ”„ Adding New Tools

```python
@tool
def your_new_tool(param: str) -> str:
    """Description of what your tool does."""
    # Your tool logic here
    return result

# Add to tools list
tools = [get_text_length, your_new_tool]
```

## ðŸŒ Environment Variables

Create a `.env` file with:
```
GROQ_API_KEY=your_groq_api_key_here
```

## ðŸ§ª Testing

Run the agent with different questions:
- Text length calculations
- Multi-step reasoning tasks
- Tool chaining scenarios

## ðŸ›¡ï¸ Error Handling

The agent includes:
- Tool name validation
- Input sanitization
- Graceful failure modes
- Detailed error messages

## ðŸ”® Future Enhancements

- [ ] Multiple tool types (web search, calculator, etc.)
- [ ] Memory and context persistence
- [ ] Multi-agent collaboration
- [ ] Custom callback handlers
- [ ] Performance metrics
- [ ] Web interface

## ðŸ“š Learn More

- [LangChain Documentation](https://docs.langchain.com/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Groq API](https://console.groq.com/)
- [UV Package Manager](https://docs.astral.sh/uv/)

## ðŸ¤ Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## ðŸ“„ License

This project is licensed under the MIT License.

## ðŸ”— Links

- **Repository**: [GitHub](https://github.com/yourusername/ReActAgent)
- **Issues**: [Bug Reports](https://github.com/yourusername/ReActAgent/issues)
- **Discussions**: [Ideas & Questions](https://github.com/yourusername/ReActAgent/discussions)

---

**Built with â¤ï¸ using LangChain, Groq, and UV**
