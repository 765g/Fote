# 🤖 Fote - Free AI in Your Terminal

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Chat with 27+ state-of-the-art AI models completely FREE from your terminal**

[🚀 Quick Install](#-quick-install) • [📖 Usage](#-usage) • [🤖 Models](#-available-models) • [💡 Examples](#-examples) • [🆘 Help](#-troubleshooting)

![Fote Demo](https://raw.githubusercontent.com/765g/Fote/master/demo.gif)

</div>

---

## ✨ Features

- 🆓 **100% Free** - No API key needed, no credit card, no signup
- 🤖 **27+ AI Models** - From 8B to 675B parameters (DeepSeek, Llama, Mistral, Codestral, etc.)
- ⚡ **Blazing Fast** - Real-time streaming responses
- 🎨 **Beautiful UI** - Professional terminal interface with colors and borders
- 💬 **Interactive Mode** - Full conversation with memory
- 🔄 **Model Switching** - Change models mid-conversation
- 💾 **Save Conversations** - Export your chats to files
- 📝 **Smart Commands** - 11+ CLI commands for full control
- 🚀 **One-Line Install** - Get started in seconds
- 🔒 **Privacy First** - No data collection, runs locally

---

## 🚀 Quick Install

### One-Line Installation

**Windows (PowerShell):**
```powershell
curl -o "$env:USERPROFILE\fote.py" https://raw.githubusercontent.com/765g/Fote/master/fote.py; pip install requests prompt-toolkit; if (!(Test-Path $PROFILE)) { New-Item -Path $PROFILE -ItemType File -Force }; Add-Content -Path $PROFILE -Value "`nfunction fote { python $env:USERPROFILE\fote.py @args }"; . $PROFILE; fote -s
```

**Linux / macOS:**
```bash
curl -o ~/fote.py https://raw.githubusercontent.com/765g/Fote/master/fote.py && pip3 install requests prompt-toolkit && echo "alias fote='python3 ~/fote.py'" >> ~/.bashrc && source ~/.bashrc && fote -s
```

**macOS (Zsh):**
```bash
curl -o ~/fote.py https://raw.githubusercontent.com/765g/Fote/master/fote.py && pip3 install requests prompt-toolkit && echo "alias fote='python3 ~/fote.py'" >> ~/.zshrc && source ~/.zshrc && fote -s
```

After installation, just type `fote` and you're ready! 🎉

---

## 📖 Usage

### Basic Commands

```bash
fote              # Show help
fote -s           # Select model interactively (recommended for first time)
fote -i           # Interactive chat mode
fote "question"   # Quick single question
fote -m MODEL     # Use specific model
fote -l           # List all available models
fote -h           # Show detailed help
```

### Interactive Mode Commands

Once inside Fote (using `fote -i` or `fote -s`):

| Command | Description | Example |
|---------|-------------|---------|
| `/model MODEL` | Switch to different model | `/model codestral` |
| `/models` | List all available models | `/models` |
| `/clear` | Clear conversation history | `/clear` |
| `/history` | Show message history | `/history` |
| `/save [file]` | Save conversation to file | `/save chat.txt` |
| `/status` | Show current model & stats | `/status` |
| `/system PROMPT` | Set custom system prompt | `/system You are a code expert` |
| `/version` | Show version info | `/version` |
| `/reload` | Refresh screen | `/reload` |
| `/help` | Show all commands | `/help` |
| `/exit` | Exit Fote | `/exit` |

---

## 🤖 Available Models

### 🏆 Best Models (Most Powerful)

| Model | Command | Parameters | Best For |
|-------|---------|------------|----------|
| Nemotron Ultra | `nemotron-ultra` | 253B | Complex reasoning & analysis |
| Nemotron Super | `nemotron-super` | 49B | Fast & balanced |
| Nemotron 70B | `nemotron-70b` | 70B | General tasks |

### 🧠 Reasoning Models (Logic & Math)

| Model | Command | Parameters | Best For |
|-------|---------|------------|----------|
| DeepSeek V4 Pro | `deepseek-v4-pro` | - | Complex problem solving |
| DeepSeek V4 Flash | `deepseek-v4-flash` | - | Fast reasoning |
| Qwen 3.5 397B | `qwen-397b` | 397B | Large-scale analysis |
| Qwen 3.5 122B | `qwen-122b` | 122B | Balanced reasoning |
| GLM 5.1 | `glm-5` | - | Logic problems |
| MiniMax M3 | `minimax` | - | Mathematical reasoning |

### 💻 Code Models (Programming)

| Model | Command | Parameters | Best For |
|-------|---------|------------|----------|
| Codestral | `codestral` | 22B | Code generation & debugging |
| Granite Code 34B | `granite-code-34b` | 34B | Enterprise code |
| Granite Code 8B | `granite-code-8b` | 8B | Quick code tasks |
| CodeGemma | `codegemma-7b` | 7B | Google's code model |
| DeepSeek Coder | `deepseek-coder` | 6.7B | Fast coding help |
| CodeLlama | `codellama` | 70B | Meta's code specialist |

### 🌐 General Models (Conversations)

| Model | Command | Parameters | Best For |
|-------|---------|------------|----------|
| Llama 3.3 70B | `llama-3.3-70b` | 70B | General chat |
| Llama 3.1 70B | `llama-3.1-70b` | 70B | Balanced tasks |
| Llama 3.1 8B | `llama-3.1-8b` | 8B | Fast responses |
| Llama 4 Maverick | `llama-4-maverick` | 17B | Latest from Meta |
| Mistral Large 3 | `mistral-large-3` | 675B | Huge multilingual model |
| Mistral Large 2 | `mistral-large-2` | - | Balanced performance |
| Mistral Medium | `mistral-medium` | 128B | General purpose |
| Gemma 4 31B | `gemma-4-31b` | 31B | Google's latest |
| Gemma 3 12B | `gemma-3-12b` | 12B | Efficient |
| Phi-4 Mini | `phi-4` | - | Microsoft's compact model |
| Yi Large | `yi-large` | - | Multilingual |

**Total: 27 models available!**

---

## 💡 Examples

### Example 1: Quick Question
```bash
fote "what is machine learning?"
```

### Example 2: Code Generation
```bash
fote -m codestral "write a python function to calculate fibonacci"
```

### Example 3: Interactive Session
```bash
$ fote -s

# Select model from menu
Select model number: 1

# Start chatting
You: explain quantum computing
AI: Quantum computing is a revolutionary approach...

You: give me a code example
AI: Here's a simple quantum circuit using Qiskit...

You: /model codestral
✓ Model changed to: Codestral 22B

You: optimize this code
AI: Here are 3 optimizations...

You: /save quantum_chat.txt
✓ Conversation saved to: quantum_chat.txt

You: /exit
✓ Session ended successfully
```

### Example 4: Debugging Help
```bash
fote -m deepseek-v4-pro "why am I getting 'NoneType' error in Python?"
```

### Example 5: Learning
```bash
$ fote -i

You: /system You are a patient teacher explaining concepts simply
✓ System prompt updated

You: explain async/await in JavaScript
AI: [Clear explanation with examples]

You: now explain promises
AI: [Builds on previous explanation]

You: /history
📜 Conversation History:
1. You: explain async/await in JavaScript
2. AI: [Async/await is...]
3. You: now explain promises
4. AI: [Promises are...]
```

---

## 🎨 Screenshots

### Model Selection
```
═══════════════════════════════════════════════════════════════════
                    SELECT YOUR DEFAULT MODEL
═══════════════════════════════════════════════════════════════════

▸ Best
  [1]  nemotron-ultra        Nemotron Ultra 253B (NVIDIA)
  [2]  nemotron-super        Nemotron Super 49B (NVIDIA)
  [3]  nemotron-70b          Nemotron 70B (NVIDIA)

▸ Reasoning
  [4]  deepseek-v4-pro       DeepSeek V4 Pro (DeepSeek)
  [5]  deepseek-v4-flash     DeepSeek V4 Flash (DeepSeek)
  ...

Select model number: _
```

### Chat Interface
```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ███████╗ ██████╗ ████████╗███████╗                              ║
║   ██╔════╝██╔═══██╗╚══██╔══╝██╔════╝                              ║
║   █████╗  ██║   ██║   ██║   █████╗                                ║
║   ██╔══╝  ██║   ██║   ██║   ██╔══╝                                ║
║   ██║     ╚██████╔╝   ██║   ███████╗                              ║
║   ╚═╝      ╚═════╝    ╚═╝   ╚══════╝                              ║
║                                                                   ║
║   Free AI Agent in Your Terminal                                ║
║   Powered by NVIDIA NIM API                                     ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

┌─ Session Info ─────────────────────────────────────────────────┐
│  User: YourName                                                 │
│  Model: Codestral 22B                                           │
│  Status: ● Online                                               │
└─────────────────────────────────────────────────────────────────┘

┌─[/home/user/projects]
└─> You: write a hello world in rust

┌─[Codestral 22B · Mistral]
└─> fn main() {
        println!("Hello, World!");
    }
```

---

## 🛠️ Installation Details

### Requirements
- **Python 3.8+** (Python 3.7 or higher)
- **pip** (comes with Python)
- **Internet connection** (for API calls)

### Manual Installation

If the one-liner doesn't work, install manually:

1. **Download Fote:**
```bash
curl -o fote.py https://raw.githubusercontent.com/765g/Fote/master/fote.py
```

2. **Install dependencies:**
```bash
pip install requests
```

3. **Run Fote:**
```bash
python fote.py -s
```

4. **(Optional) Create alias:**

**Windows PowerShell:**
```powershell
echo "function fote { python $HOME\fote.py @args }" >> $PROFILE
```

**Linux/macOS:**
```bash
echo "alias fote='python3 ~/fote.py'" >> ~/.bashrc
source ~/.bashrc
```

---

## 🆘 Troubleshooting

### "python command not found"
**Solution:** Install Python from [python.org](https://www.python.org/downloads/)

Or use `python3`:
```bash
python3 fote.py -s
```

### "requests module not found"
**Solution:**
```bash
pip install requests
# or
pip3 install requests
```

### "fote command not found"
**Solution:** Restart your terminal after installation, or use full path:
```bash
python ~/fote.py -s  # Linux/macOS
python %USERPROFILE%\fote.py -s  # Windows
```

### No response from AI
**Solution:** 
- Check your internet connection
- Try a different model with `/model llama-3.1-8b`
- Some models may be temporarily unavailable

### Slow responses
**Solution:** Use faster models:
- `llama-3.1-8b` (fastest)
- `llama-4-maverick` (fast)
- `deepseek-v4-flash` (fast reasoning)

---

## 🔧 Advanced Usage

### Custom System Prompts
```bash
fote -i
You: /system You are a senior software architect with 20 years of experience
You: review my database schema
```

### Saving Conversations
```bash
You: /save my_chat_$(date +%Y%m%d).txt
```

### Chaining Commands
```bash
# Quick question with specific model
fote -m deepseek-v4-pro "calculate the derivative of x^3 + 2x"

# Multiple quick questions
fote "what is rust?" && fote "what is golang?"
```

### Using in Scripts
```bash
#!/bin/bash
# Ask AI for code review
RESPONSE=$(echo "review this code: $(cat myfile.py)" | python fote.py -m codestral)
echo "$RESPONSE" > review.txt
```

---

## 🎯 Use Cases

### For Developers
```bash
fote -m codestral "refactor this function for better performance"
fote -m granite-code-34b "write unit tests for this class"
fote -m deepseek-coder "explain this regex pattern"
```

### For Students
```bash
fote -m deepseek-v4-pro "explain Bayes theorem with example"
fote -m llama-3.3-70b "summarize this article"
fote "help me understand quantum mechanics"
```

### For Writers
```bash
fote -m mistral-large-2 "write a professional email declining a job offer"
fote "brainstorm blog post ideas about AI"
```

### For Data Scientists
```bash
fote -m qwen-397b "explain principal component analysis"
fote -m deepseek-v4-pro "which statistical test should I use?"
```

---

## 📊 Model Comparison

| Characteristic | Best For | Recommended Models |
|----------------|----------|-------------------|
| 🚀 Speed | Quick answers | `llama-3.1-8b`, `llama-4-maverick`, `deepseek-v4-flash` |
| 🧠 Intelligence | Complex tasks | `nemotron-ultra`, `qwen-397b`, `mistral-large-3` |
| 💻 Coding | Programming | `codestral`, `granite-code-34b`, `deepseek-coder` |
| 🔬 Reasoning | Math & Logic | `deepseek-v4-pro`, `qwen-397b`, `glm-5` |
| 💬 Chat | Conversations | `llama-3.3-70b`, `mistral-large-2`, `gemma-4-31b` |
| 🌍 Multilingual | Non-English | `mistral-large-3`, `qwen-397b`, `yi-large` |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Add more models
- Improve UI/UX
- Add conversation history search
- Create plugins system
- Add voice input/output
- Multi-language support

---

## 📝 Changelog

### v1.0.0 (2024-06-23)
- 🎉 Initial release
- ✨ 27+ AI models
- 💬 Interactive chat mode
- 🎨 Beautiful CLI interface
- 💾 Save conversations
- 🔄 Model switching
- 📊 Full command system

---

## 📜 License

This project is licensed under the MIT License - see below:

```
MIT License

Copyright (c) 2024 765g

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **NVIDIA** - For providing free access to NIM API
- **Model Providers** - Meta, Mistral, DeepSeek, Alibaba, Google, Microsoft, and more
- **Community** - For feedback and contributions

---

## 📞 Contact & Support

- **GitHub Issues:** [Report bugs or request features](https://github.com/765g/Fote/issues)
- **Author:** 765g
- **Repository:** [github.com/765g/Fote](https://github.com/765g/Fote)

---

## ⭐ Show Your Support

If you find Fote useful, please consider:
- ⭐ Starring the repository
- 🐦 Sharing on social media
- 🤝 Contributing to the project
- 💬 Spreading the word

---

<div align="center">

**Made with ❤️ by [765g](https://github.com/765g)**

**Powered by NVIDIA NIM API**

[⬆ Back to Top](#-fote---free-ai-in-your-terminal)

</div>
