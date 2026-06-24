# ⚡ Fote Quick Start Guide

**Get started in 30 seconds!**

---

## 🚀 Installation

### Step 1: Install
```cmd
cd C:\Users\Administrator\Desktop\RIVALS\Fote
INSTALL.bat
```

### Step 2: Restart Terminal
Close and reopen your terminal (Command Prompt or PowerShell)

### Step 3: Test
```bash
fote "hello"
```

**That's it!** 🎉

---

## 💡 Basic Usage

### Ask a Question
```bash
fote "what is artificial intelligence?"
```

### Get Code Help
```bash
fote -m codestral "write a python function to sort a list"
```

### Start Interactive Chat
```bash
fote -i
```

### List All Models
```bash
fote -l
```

---

## 🎯 Best Practices

### For Quick Questions
Use the default model (fastest for general queries):
```bash
fote "your question here"
```

### For Complex Problems
Use the best reasoning models:
```bash
fote -m deepseek-v4 "solve this math problem: ..."
fote -m qwen-397b "explain quantum mechanics"
fote -m nemotron-ultra "analyze this data: ..."
```

### For Programming
Use specialized code models:
```bash
fote -m codestral "write a REST API"
fote -m granite-code "refactor this code"
fote -m deepseek-coder "debug this error"
```

### For Long Conversations
Use interactive mode:
```bash
fote -i
# Then chat normally, it remembers context!
```

---

## 🤖 Top 5 Models to Try

1. **nemotron-ultra** - Best overall, 550B parameters
   ```bash
   fote -m nemotron-ultra "your question"
   ```

2. **deepseek-v4** - Best for reasoning and logic
   ```bash
   fote -m deepseek-v4 "complex problem"
   ```

3. **codestral** - Best for code generation
   ```bash
   fote -m codestral "write code"
   ```

4. **llama-3.3-70b** - Fast and balanced
   ```bash
   fote -m llama-3.3-70b "general question"
   ```

5. **mistral-large-3** - Huge 675B model
   ```bash
   fote -m mistral-large-3 "difficult task"
   ```

---

## 💬 Interactive Mode Commands

When you run `fote -i`, you can use these commands:

| Command | What it does | Example |
|---------|--------------|---------|
| `/model` | Change AI model | `/model codestral` |
| `/models` | Show all models | `/models` |
| `/clear` | Clear chat history | `/clear` |
| `/system` | Change AI personality | `/system You are a coding expert` |
| `/help` | Show help | `/help` |
| `/exit` | Quit | `/exit` |

---

## 📚 Common Tasks

### Learn Something New
```bash
fote "explain machine learning in simple terms"
fote "what is blockchain technology?"
fote "teach me about design patterns"
```

### Write Code
```bash
fote -m codestral "create a TODO app in React"
fote -m granite-code "write a Python web scraper"
fote -m deepseek-coder "make a Discord bot"
```

### Debug Code
```bash
fote -m deepseek-v4 "why is my code giving this error: [paste error]"
fote -m codestral "optimize this function: [paste code]"
```

### Get Creative
```bash
fote "write a short story about AI"
fote "create a professional email template"
fote "help me brainstorm app ideas"
```

---

## ⚡ Pro Tips

1. **Try different models** for the same question to compare answers
2. **Use interactive mode** for coding projects (keeps context)
3. **Save good responses** by copying them to a file
4. **Switch models mid-conversation** with `/model`
5. **Use specific models** for their strengths:
   - Questions → `nemotron-ultra`
   - Math/Logic → `deepseek-v4`
   - Code → `codestral`
   - Fast → `llama-4-maverick`

---

## 🆘 Need Help?

### Show Help
```bash
fote -h
```

### List Models
```bash
fote -l
```

### Test API Connection
```bash
python test_api.py
```

### Read Full Documentation
Open `README.md` in this folder

### Check Examples
Open `EXAMPLES.md` for tons of usage examples

---

## 🎯 Example Session

```bash
# Start
C:\> fote -i

# Change to code model
You: /model codestral
Bot: ✓ Model changed to: Codestral 22B

# Ask for code
You: create a python web server
Bot: [Provides code]

# Ask follow-up
You: add authentication
Bot: [Adds auth code]

# Switch to reasoning model
You: /model deepseek-v4
Bot: ✓ Model changed to: DeepSeek V4 Pro

# Ask logic question
You: how do I optimize this algorithm?
Bot: [Explains optimization]

# Clear and start fresh
You: /clear
Bot: ✓ Conversation cleared

# Exit
You: /exit
Bot: ✓ Session ended successfully
```

---

## 🌟 Why Fote is Awesome

✅ **100% Free** - No signup, no credit card  
✅ **25+ AI Models** - From 7B to 675B parameters  
✅ **Zero Config** - Works out of the box  
✅ **Professional UI** - Clean and beautiful  
✅ **Fast** - Streaming responses  
✅ **Easy** - Simple commands  

---

**Ready to start? Just type:**
```bash
fote -i
```

**Happy chatting! 🚀**

---

**Questions?** Check `README.md` or `EXAMPLES.md`  
**Author:** 765g | **Version:** 1.0.0
