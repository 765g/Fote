# 🤖 Fote - Free AI Chat in Terminal

> A powerful CLI agent powered by NVIDIA NIM API - 100% Free!

**Author:** 765g  
**Version:** 1.0.0

---

## ✨ Features

- 🚀 **100% Free** - No credit card, no limits
- 🤖 **25+ AI Models** - Best models from NVIDIA, Meta, Mistral, DeepSeek, Google, and more
- 💬 **Interactive Chat** - Continuous conversation mode
- 🎨 **Beautiful Interface** - Professional terminal UI with colors and borders
- ⚡ **Streaming** - Real-time AI responses
- 📝 **Easy Commands** - Simple model switching and management
- 🔥 **Ultra Fast** - Direct API integration, no middleware

---

## 🎯 Quick Start

### Installation

1. **Run the installer:**
   ```cmd
   INSTALL.bat
   ```

2. **Restart your terminal**

3. **Start chatting:**
   ```bash
   fote "Hello, how are you?"
   ```

---

## 💡 Usage

### Quick Message
```bash
fote "explain quantum computing"
fote "write a python script to sort numbers"
fote "what is rust programming language"
```

### With Specific Model
```bash
fote -m llama-3.3-70b "explain async programming"
fote -m deepseek-v4 "debug this code: print('hello')"
fote -m codestral "write a REST API in fastapi"
```

### Interactive Mode (Best Experience)
```bash
fote -i
```

In interactive mode, you get:
- Continuous conversation with memory
- Easy model switching with `/model`
- Clear conversation with `/clear`
- Full command support

### List All Models
```bash
fote -l
```

### Help
```bash
fote -h
```

---

## 🤖 Available Models

### 🏆 Best Models (Largest & Most Capable)
| Command | Model | Size | Best For |
|---------|-------|------|----------|
| `nemotron-ultra` | NVIDIA Nemotron 3 Ultra | 550B | Complex reasoning, analysis |
| `nemotron-super` | NVIDIA Nemotron Super | 49B | General tasks, fast |
| `mistral-large-3` | Mistral Large 3 | 675B | Multilingual, long context |

### 🧠 Reasoning Models (Logic & Analysis)
| Command | Model | Provider | Best For |
|---------|-------|----------|----------|
| `deepseek-v4` | DeepSeek V4 Pro | DeepSeek | Math, logic problems |
| `deepseek-flash` | DeepSeek V4 Flash | DeepSeek | Fast reasoning |
| `qwen-397b` | Qwen 3.5 397B | Alibaba | Complex analysis |
| `glm-5` | GLM 5.1 | Z.ai | Reasoning tasks |
| `minimax` | MiniMax M3 | MiniMax | Problem solving |

### 💻 Code Models (Programming)
| Command | Model | Provider | Best For |
|---------|-------|----------|----------|
| `codestral` | Codestral 22B | Mistral | Code generation |
| `granite-code` | Granite Code 34B | IBM | Enterprise code |
| `codegemma` | CodeGemma 7B | Google | Quick coding |
| `deepseek-coder` | DeepSeek Coder 6.7B | DeepSeek | Fast code help |

### 🌐 General Models (Balanced)
| Command | Model | Provider | Best For |
|---------|-------|----------|----------|
| `llama-3.3-70b` | Llama 3.3 70B | Meta | Conversations |
| `llama-3.1-70b` | Llama 3.1 70B | Meta | General tasks |
| `llama-4-maverick` | Llama 4 Maverick 17B | Meta | Fast responses |
| `mistral-medium` | Mistral Medium 128B | Mistral | Balanced |
| `qwen-122b` | Qwen 3.5 122B | Alibaba | Multilingual |
| `gemma-4-31b` | Gemma 4 31B | Google | Efficient |
| `phi-4` | Phi-4 Mini | Microsoft | Quick tasks |
| `gpt-oss-120b` | GPT-OSS 120B | OpenAI | OpenAI style |
| `yi-large` | Yi Large | 01.AI | General use |

---

## 💬 Interactive Commands

When in interactive mode (`fote -i`):

| Command | Description | Example |
|---------|-------------|---------|
| `/model <name>` | Switch to different model | `/model deepseek-v4` |
| `/models` | List all available models | `/models` |
| `/clear` | Clear conversation history | `/clear` |
| `/system <prompt>` | Set custom system prompt | `/system You are a code expert` |
| `/help` | Show help | `/help` |
| `/exit` | Exit chat | `/exit` |

---

## 📸 Examples

### Example 1: Quick Question
```bash
C:\> fote "what is the fastest sorting algorithm?"

╔═══════════════════════════════════════════════════════╗
║   ███████╗ ██████╗ ████████╗███████╗                  ║
║   ██╔════╝██╔═══██╗╚══██╔══╝██╔════╝                  ║
║   █████╗  ██║   ██║   ██║   █████╗                    ║
║   ██╔══╝  ██║   ██║   ██║   ██╔══╝                    ║
║   ██║     ╚██████╔╝   ██║   ███████╗                  ║
║   ╚═╝      ╚═════╝    ╚═╝   ╚══════╝                  ║
╚═══════════════════════════════════════════════════════╝

┌─ Session Info ────────────────────────────────────┐
│  User: Administrator                              │
│  Model: Nemotron 3 Ultra 550B                     │
│  Status: ● Online                                 │
└───────────────────────────────────────────────────┘

┌─[C:\Users\Admin]
└─> Administrator: what is the fastest sorting algorithm?

┌─[Nemotron 3 Ultra 550B · NVIDIA]
└─> The fastest sorting algorithm depends on the context...
    [AI provides detailed explanation]
```

### Example 2: Code Generation
```bash
C:\> fote -m codestral "write a python function to calculate fibonacci"

┌─[Codestral 22B · Mistral]
└─> Here's an efficient Fibonacci implementation:
    
    def fibonacci(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

### Example 3: Interactive Session
```bash
C:\> fote -i

[Banner appears]

Administrator: /model llama-3.3-70b
┌─[✓]
└─> Model changed to: Llama 3.3 70B

Administrator: explain async/await in javascript

┌─[Llama 3.3 70B · Meta]
└─> Async/await is syntactic sugar for working with Promises...
    [Detailed explanation follows]

Administrator: /clear
┌─[✓]
└─> Conversation cleared

Administrator: /exit
╔═══════════════════════════════════════╗
║  ✓ Session ended successfully      ║
║  Thank you for using Fote!       ║
╚═══════════════════════════════════════╝
```

---

## 🔧 Technical Details

**Requirements:**
- Python 3.8+
- `requests` library (auto-installed)
- Windows, Linux, or macOS

**API:**
- NVIDIA NIM API (`integrate.api.nvidia.com`)
- 100% Free (no credit card required)
- Multiple model endpoints
- Streaming support

**Files:**
- `fote.py` - Main Python script
- `fote.ps1` - PowerShell wrapper
- `INSTALL.bat` - Auto installer
- `test_api.py` - API connectivity test

---

## 🎨 Interface

**Colors:**
- **Cyan** - User input, commands
- **Green** - AI responses, success messages
- **Yellow** - Warnings, highlights
- **Gray** - Metadata, borders
- **Red** - Errors
- **Purple** - Best models

**Layout:**
- Professional ASCII banner
- Bordered session info
- Clean prompt structure
- Status indicators

---

## ⚡ Pro Tips

1. **Use Best Models for Hard Tasks**
   ```bash
   fote -m nemotron-ultra "complex math problem"
   ```

2. **Use Fast Models for Quick Questions**
   ```bash
   fote -m llama-4-maverick "quick question"
   ```

3. **Use Code Models for Programming**
   ```bash
   fote -m codestral "write a REST API"
   ```

4. **Interactive Mode for Long Conversations**
   ```bash
   fote -i
   # Then chat normally with memory
   ```

5. **Switch Models Mid-Conversation**
   ```
   /model deepseek-v4    # For reasoning
   /model codestral      # For coding
   ```

---

## 🆘 Troubleshooting

### "Python not found"
Install Python 3.8+ from [python.org](https://python.org)

### "Module 'requests' not found"
```bash
pip install requests
```

### "Command not recognized"
Restart your terminal after running `INSTALL.bat`

### "API errors"
- Check internet connection
- API key is embedded, should work automatically
- Try a different model with `-m`

### "No response"
- Some models may be slow to respond
- Try a smaller model like `llama-4-maverick`
- Check if the model is available with `fote -l`

---

## 📝 License

Free to use for personal, educational, and commercial purposes.

---

## 🤝 Credits

**Author:** 765g  
**Powered by:** NVIDIA NIM API  
**Models from:** NVIDIA, Meta, Mistral, DeepSeek, Alibaba, Google, Microsoft, OpenAI, and more

---

## 🌟 Why Fote?

✅ **100% Free** - No signup, no credit card, no limits  
✅ **25+ Models** - From 6.7B to 675B parameters  
✅ **Professional** - Clean interface, fast responses  
✅ **Powerful** - Access to state-of-the-art AI  
✅ **Easy** - Install and start in 30 seconds  

**Enjoy chatting with Fote! 🚀**

---

**Need help? Found a bug?**  
Contact: 765g on GitHub

**Star the repo if you like it!** ⭐
