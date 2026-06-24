# Changelog - Fote CLI

## Version 1.1 - Ultra Minimal UI (Current)

**SIMPLIFIED - Like FreeBuff Style**

### Changes
- ✅ Removed all decorative ASCII boxes and borders
- ✅ Removed complex ANSI color schemes
- ✅ Simplified banner to just "Fote - Free AI in terminal"
- ✅ Clean `>` prompt (no fancy decorations)
- ✅ Minimal help output (no tables/boxes)
- ✅ Simple model list (no color coding per category)
- ✅ Plain text error messages
- ✅ Code reduced from ~700 lines to ~500 lines

### What It Looks Like Now

```
Fote - Free AI in terminal
Model: Llama 3.1 70B

> hello
Hello! How can I help you today?

> /help

Commands:
  /model <name>  - Change model
  /models        - List models
  /clear         - Clear chat
  /save [file]   - Save conversation
  /help          - Show help
  /exit          - Quit

>
```

### Command Line
```bash
# Quick chat
fote "your message"

# Interactive mode
fote -i

# Select model first
fote -s

# List all models
fote -l

# Use specific model
fote -m codestral "write python code"

# Help
fote -h
```

### Features Kept
- ✅ 27 free NVIDIA AI models
- ✅ Streaming responses
- ✅ Model switching
- ✅ Conversation saving
- ✅ Chat history
- ✅ Simple commands

### What Was Removed
- ❌ Complex bordered boxes (╔═══╗ style)
- ❌ Excessive colors and emojis
- ❌ Multi-line fancy prompts
- ❌ Decorative headers
- ❌ Over-engineered UI elements

---

## Version 1.0 - Initial Release

- Full-featured CLI with NVIDIA NIM API
- 27 free models
- Interactive mode
- Model selection
- Chat history
- Complex UI with boxes and colors
