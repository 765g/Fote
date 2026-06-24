#!/usr/bin/env python3
"""
Fote - Free AI Chat in Terminal
Uses NVIDIA NIM API with multiple models
Author: 765g
"""

import os
import sys
import json
import requests
from datetime import datetime
import platform

# Try to import prompt_toolkit for better input
try:
    from prompt_toolkit import prompt as pt_prompt
    from prompt_toolkit.styles import Style
    from prompt_toolkit.formatted_text import HTML
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False

# NVIDIA API Configuration
NVIDIA_API_KEY = "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"
NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

# Available FREE Models from NVIDIA API
# All models verified to work with the provided API key
MODELS = {
    # NVIDIA Best Models
    "nemotron-ultra": {
        "id": "nvidia/llama-3.1-nemotron-ultra-253b-v1",
        "name": "Nemotron Ultra 253B",
        "provider": "NVIDIA",
        "category": "Best"
    },
    "nemotron-super": {
        "id": "nvidia/llama-3.3-nemotron-super-49b-v1.5",
        "name": "Nemotron Super 49B",
        "provider": "NVIDIA",
        "category": "Best"
    },
    "nemotron-70b": {
        "id": "nvidia/llama-3.1-nemotron-70b-instruct",
        "name": "Nemotron 70B",
        "provider": "NVIDIA",
        "category": "Best"
    },
    
    # Reasoning/Logic Models
    "deepseek-v4-pro": {
        "id": "deepseek-ai/deepseek-v4-pro",
        "name": "DeepSeek V4 Pro",
        "provider": "DeepSeek",
        "category": "Reasoning"
    },
    "deepseek-v4-flash": {
        "id": "deepseek-ai/deepseek-v4-flash",
        "name": "DeepSeek V4 Flash",
        "provider": "DeepSeek",
        "category": "Reasoning"
    },
    "qwen-397b": {
        "id": "qwen/qwen3.5-397b-a17b",
        "name": "Qwen 3.5 397B",
        "provider": "Alibaba",
        "category": "Reasoning"
    },
    "qwen-122b": {
        "id": "qwen/qwen3.5-122b-a10b",
        "name": "Qwen 3.5 122B",
        "provider": "Alibaba",
        "category": "Reasoning"
    },
    "glm-5": {
        "id": "z-ai/glm-5.1",
        "name": "GLM 5.1",
        "provider": "Z.ai",
        "category": "Reasoning"
    },
    "minimax": {
        "id": "minimaxai/minimax-m3",
        "name": "MiniMax M3",
        "provider": "MiniMax",
        "category": "Reasoning"
    },
    
    # Code Specialized Models
    "codestral": {
        "id": "mistralai/codestral-22b-instruct-v0.1",
        "name": "Codestral 22B",
        "provider": "Mistral",
        "category": "Code"
    },
    "granite-code-34b": {
        "id": "ibm/granite-34b-code-instruct",
        "name": "Granite Code 34B",
        "provider": "IBM",
        "category": "Code"
    },
    "granite-code-8b": {
        "id": "ibm/granite-8b-code-instruct",
        "name": "Granite Code 8B",
        "provider": "IBM",
        "category": "Code"
    },
    "codegemma-7b": {
        "id": "google/codegemma-7b",
        "name": "CodeGemma 7B",
        "provider": "Google",
        "category": "Code"
    },
    "deepseek-coder": {
        "id": "deepseek-ai/deepseek-coder-6.7b-instruct",
        "name": "DeepSeek Coder 6.7B",
        "provider": "DeepSeek",
        "category": "Code"
    },
    "codellama": {
        "id": "meta/codellama-70b",
        "name": "CodeLlama 70B",
        "provider": "Meta",
        "category": "Code"
    },
    
    # General Purpose Models
    "llama-3.3-70b": {
        "id": "meta/llama-3.3-70b-instruct",
        "name": "Llama 3.3 70B",
        "provider": "Meta",
        "category": "General"
    },
    "llama-3.1-70b": {
        "id": "meta/llama-3.1-70b-instruct",
        "name": "Llama 3.1 70B",
        "provider": "Meta",
        "category": "General"
    },
    "llama-3.1-8b": {
        "id": "meta/llama-3.1-8b-instruct",
        "name": "Llama 3.1 8B",
        "provider": "Meta",
        "category": "General"
    },
    "llama-4-maverick": {
        "id": "meta/llama-4-maverick-17b-128e-instruct",
        "name": "Llama 4 Maverick 17B",
        "provider": "Meta",
        "category": "General"
    },
    "mistral-large-3": {
        "id": "mistralai/mistral-large-3-675b-instruct-2512",
        "name": "Mistral Large 3 675B",
        "provider": "Mistral",
        "category": "General"
    },
    "mistral-large-2": {
        "id": "mistralai/mistral-large-2-instruct",
        "name": "Mistral Large 2",
        "provider": "Mistral",
        "category": "General"
    },
    "mistral-medium": {
        "id": "mistralai/mistral-medium-3.5-128b",
        "name": "Mistral Medium 128B",
        "provider": "Mistral",
        "category": "General"
    },
    "gemma-4-31b": {
        "id": "google/gemma-4-31b-it",
        "name": "Gemma 4 31B",
        "provider": "Google",
        "category": "General"
    },
    "gemma-3-12b": {
        "id": "google/gemma-3-12b-it",
        "name": "Gemma 3 12B",
        "provider": "Google",
        "category": "General"
    },
    "phi-4": {
        "id": "microsoft/phi-4-mini-instruct",
        "name": "Phi-4 Mini",
        "provider": "Microsoft",
        "category": "General"
    },
    "yi-large": {
        "id": "01-ai/yi-large",
        "name": "Yi Large",
        "provider": "01.AI",
        "category": "General"
    }
}

class NvidiaChat:
    def __init__(self):
        self.api_key = NVIDIA_API_KEY
        self.api_url = NVIDIA_API_URL
        self.model = "llama-3.1-70b"  # Default to working model
        self.conversation = []
        self.system_prompt = "You are a helpful AI assistant."
        
    def set_model(self, model_key):
        """Change the current model"""
        if model_key in MODELS:
            self.model = model_key
            return True
        return False
    
    def set_system_prompt(self, prompt):
        """Set custom system prompt"""
        self.system_prompt = prompt
        
    def chat(self, user_message, stream=False):
        """Send a message and get response"""
        # Add user message to conversation
        self.conversation.append({"role": "user", "content": user_message})
        
        # Prepare messages with system prompt
        messages = [{"role": "system", "content": self.system_prompt}] + self.conversation
        
        # Get model ID
        model_id = MODELS[self.model]["id"]
        
        # Prepare request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model_id,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4096,
            "stream": stream
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=payload, stream=stream)
            response.raise_for_status()
            
            if stream:
                return self._handle_stream(response)
            else:
                result = response.json()
                assistant_message = result["choices"][0]["message"]["content"]
                self.conversation.append({"role": "assistant", "content": assistant_message})
                return assistant_message
                
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
    
    def _handle_stream(self, response):
        """Handle streaming response"""
        full_response = ""
        try:
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith("data: "):
                        data = line[6:]
                        if data == "[DONE]":
                            break
                        try:
                            chunk = json.loads(data)
                            if "choices" in chunk and len(chunk["choices"]) > 0:
                                delta = chunk["choices"][0].get("delta", {})
                                content = delta.get("content", "")
                                if content:
                                    print(content, end="", flush=True)
                                    full_response += content
                        except json.JSONDecodeError:
                            pass
            
            if full_response:
                print()  # New line after stream
                self.conversation.append({"role": "assistant", "content": full_response})
            else:
                print("\033[31m[No response received]\033[0m")
            return full_response
        except Exception as e:
            print(f"\033[31m[Stream error: {str(e)}]\033[0m")
            return ""
    
    def clear_conversation(self):
        """Clear conversation history"""
        self.conversation = []
    
    def list_models(self):
        """List all available models"""
        print("\n\033[90m╔═══════════════════════════════════════════════════════════════════════╗\033[0m")
        print("\033[90m║\033[0m  \033[36m🤖 Available Models\033[0m" + " " * 46 + "\033[90m║\033[0m")
        print("\033[90m╠═══════════════════════════════════════════════════════════════════════╣\033[0m")
        
        categories = {"Best": [], "Reasoning": [], "Code": [], "General": []}
        for key, info in MODELS.items():
            categories[info['category']].append((key, info))
        
        for category, models in categories.items():
            if not models:
                continue
                
            category_color = {
                "Best": "\033[35m",
                "Reasoning": "\033[33m",
                "Code": "\033[32m",
                "General": "\033[36m"
            }.get(category, "\033[37m")
            
            print(f"\033[90m║\033[0m  {category_color}▸ {category}\033[0m" + " " * (63 - len(category)) + "\033[90m║\033[0m")
            
            for key, info in models:
                name_display = f"{key}"
                full_name = f"{info['name']} ({info['provider']})"
                spacing = 65 - len(name_display) - len(full_name)
                print(f"\033[90m║\033[0m    \033[36m{name_display}\033[0m{' ' * spacing}{full_name} \033[90m║\033[0m")
            
            print("\033[90m║\033[0m" + " " * 71 + "\033[90m║\033[0m")
        
        print("\033[90m╚═══════════════════════════════════════════════════════════════════════╝\033[0m")
        print()


def print_banner(model_name=None, username=None, show_instructions=True):
    """Print CLI banner"""
    import getpass
    if username is None:
        username = getpass.getuser()
    
    banner = f"""
\033[35m╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   \033[31m███████╗ ██████╗ ████████╗███████╗\033[35m                                  ║
║   \033[31m██╔════╝██╔═══██╗╚══██╔══╝██╔════╝\033[35m                                  ║
║   \033[31m█████╗  ██║   ██║   ██║   █████╗\033[35m                                    ║
║   \033[31m██╔══╝  ██║   ██║   ██║   ██╔══╝\033[35m                                    ║
║   \033[31m██║     ╚██████╔╝   ██║   ███████╗\033[35m                                  ║
║   \033[31m╚═╝      ╚═════╝    ╚═╝   ╚══════╝\033[35m                                  ║
║                                                                       ║
║   \033[90mFree AI Agent in Your Terminal\033[35m                                    ║
║   \033[90mPowered by NVIDIA NIM API\033[35m                                         ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝\033[0m
"""
    
    print(banner)
    
    if model_name and username:
        print(f"\033[90m┌─ Session Info ─────────────────────────────────────────────────────┐\033[0m")
        print(f"\033[90m│\033[0m  \033[36mUser:\033[0m {username:<40} \033[90m│\033[0m")
        print(f"\033[90m│\033[0m  \033[32mModel:\033[0m {model_name:<39} \033[90m│\033[0m")
        print(f"\033[90m│\033[0m  \033[33mStatus:\033[0m \033[32m●\033[0m Online{' ' * 39} \033[90m│\033[0m")
        print(f"\033[90m└────────────────────────────────────────────────────────────────────┘\033[0m")
        print()
    
    if show_instructions:
        print("\033[90m  Commands: /help /models /model /clear /history /save /status\033[0m")
        print("\033[90m            /system /version /reload /exit\033[0m")
        print()


def print_help():
    """Print help message"""
    print("\n\033[90m╔═══════════════════════════════════════════════════════════════════════╗\033[0m")
    print("\033[90m║\033[0m  \033[36m📖 Fote Help & Commands\033[0m" + " " * 43 + "\033[90m║\033[0m")
    print("\033[90m╠═══════════════════════════════════════════════════════════════════════╣\033[0m")
    print("\033[90m║\033[0m  \033[33m▸ CLI Usage\033[0m" + " " * 57 + "\033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36mfote \"your message\"\033[0m              Quick single message         \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36mfote -m model \"message\"\033[0m          Use specific model           \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36mfote -i\033[0m                          Interactive mode             \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36mfote -s\033[0m                          Select model & chat          \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36mfote -l\033[0m                          List all models              \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36mfote -h\033[0m                          Show this help               \033[90m║\033[0m")
    print("\033[90m║\033[0m" + " " * 71 + "\033[90m║\033[0m")
    print("\033[90m║\033[0m  \033[33m▸ Interactive Commands\033[0m" + " " * 46 + "\033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/model, /m, /use <name>\033[0m          Change model                 \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/models, /list, /ls\033[0m              List all models              \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/clear, /cls, /reset\033[0m             Clear conversation           \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/system, /sys <prompt>\033[0m           Set system prompt            \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/history, /hist\033[0m                  Show message history         \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/save, /export [file]\033[0m            Save conversation            \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/status, /stat\033[0m                   Show current status          \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/version, /v, /info\033[0m              Show version info            \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/reload, /refresh\033[0m                Refresh screen               \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/help, /h, /?\033[0m                    Show help                    \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[36m/exit, /quit, /q\033[0m                 Exit chat                    \033[90m║\033[0m")
    print("\033[90m║\033[0m" + " " * 71 + "\033[90m║\033[0m")
    print("\033[90m║\033[0m  \033[33m▸ Examples\033[0m" + " " * 58 + "\033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[90mfote \"explain quantum computing\"\033[0m                            \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[90mfote -m codestral \"write python code\"\033[0m                      \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[90mfote -s\033[0m                       \033[90m(select model interactively)\033[0m \033[90m║\033[0m")
    print("\033[90m║\033[0m    \033[90mfote -i\033[0m" + " " * 63 + "\033[90m║\033[0m")
    print("\033[90m╚═══════════════════════════════════════════════════════════════════════╝\033[0m")
    print()


def get_user_input(username, cwd):
    """Get user input with optional prompt_toolkit"""
    if PROMPT_TOOLKIT_AVAILABLE:
        # Simple clean input bar
        style = Style.from_dict({
            'prompt': '#00ff00',  # Green
        })
        
        try:
            return pt_prompt(
                HTML(f'<prompt>{username}:</prompt> '),
                style=style,
                multiline=False
            ).strip()
        except (EOFError, KeyboardInterrupt):
            return None
    else:
        # Fallback to regular input
        return input(f"\033[32m{username}:\033[0m ").strip()


def interactive_mode(chat):
    """Run interactive chat mode"""
    import getpass
    import os
    
    username = getpass.getuser()
    model_name = MODELS[chat.model]['name']
    
    # Clear screen (Windows/Linux compatible)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print banner
    print_banner(model_name, username, show_instructions=True)
    
    # Show prompt_toolkit status
    if not PROMPT_TOOLKIT_AVAILABLE:
        print("\033[33m💡 Tip: Install 'prompt-toolkit' for a better input experience:\033[0m")
        print("\033[33m   pip install prompt-toolkit\033[0m\n")
    
    # Conversation history (for save/export)
    conversation_log = []
    
    while True:
        try:
            # Get current directory for prompt
            cwd = os.getcwd()
            
            # Get user input
            user_input = get_user_input(username, cwd)
            
            # Handle Ctrl+C or Ctrl+D
            if user_input is None:
                print("\n\n\033[90m╔═══════════════════════════════════════╗\033[0m")
                print("\033[90m║\033[0m  \033[33m⚠\033[0m  Interrupted by user          \033[90m║\033[0m")
                print("\033[90m║\033[0m  \033[90mSession terminated\033[0m               \033[90m║\033[0m")
                print("\033[90m╚═══════════════════════════════════════╝\033[0m\n")
                break
            
            if not user_input:
                continue
            
            # Log user input
            conversation_log.append({"role": "user", "content": user_input, "timestamp": datetime.now().isoformat()})
            
            # Handle commands
            if user_input.startswith("/"):
                cmd_parts = user_input.split(maxsplit=1)
                cmd = cmd_parts[0].lower()
                
                # EXIT/QUIT
                if cmd == "/exit" or cmd == "/quit" or cmd == "/q":
                    print("\n\033[90m╔═══════════════════════════════════════╗\033[0m")
                    print("\033[90m║\033[0m  \033[32m✓\033[0m Session ended successfully      \033[90m║\033[0m")
                    print("\033[90m║\033[0m  \033[90mThank you for using Fote!\033[0m       \033[90m║\033[0m")
                    print("\033[90m╚═══════════════════════════════════════╝\033[0m\n")
                    break
                
                # HELP
                elif cmd == "/help" or cmd == "/h" or cmd == "/?":
                    print_help()
                    continue
                
                # LIST MODELS
                elif cmd == "/models" or cmd == "/list" or cmd == "/ls":
                    chat.list_models()
                    continue
                
                # CLEAR CONVERSATION
                elif cmd == "/clear" or cmd == "/cls" or cmd == "/reset":
                    chat.clear_conversation()
                    conversation_log = []
                    # Clear screen
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_banner(MODELS[chat.model]['name'], username, show_instructions=True)
                    print("\n\033[90m┌─[\033[32m✓\033[90m]\033[0m")
                    print("\033[90m└─>\033[0m \033[90mConversation cleared\033[0m")
                    continue
                
                # CHANGE MODEL
                elif cmd == "/model" or cmd == "/m" or cmd == "/use":
                    if len(cmd_parts) < 2:
                        print("\n\033[90m┌─[\033[31m✗\033[90m]\033[0m")
                        print("\033[90m└─>\033[0m \033[31mUsage: /model <model_name>\033[0m")
                        print("\033[90m    Try: /models to see available options\033[0m")
                        continue
                    model_key = cmd_parts[1]
                    if chat.set_model(model_key):
                        new_model_name = MODELS[model_key]['name']
                        print(f"\n\033[90m┌─[\033[32m✓\033[90m]\033[0m")
                        print(f"\033[90m└─>\033[0m Model changed to: \033[32m{new_model_name}\033[0m")
                    else:
                        print(f"\n\033[90m┌─[\033[31m✗\033[90m]\033[0m")
                        print(f"\033[90m└─>\033[0m \033[31mModel '{model_key}' not found\033[0m")
                        print(f"\033[90m    Use /models to see available options\033[0m")
                    continue
                
                # CHANGE SYSTEM PROMPT
                elif cmd == "/system" or cmd == "/sys":
                    if len(cmd_parts) < 2:
                        print("\n\033[90m┌─[\033[31m✗\033[90m]\033[0m")
                        print("\033[90m└─>\033[0m \033[31mUsage: /system <prompt>\033[0m")
                        print("\033[90m    Example: /system You are a coding expert\033[0m")
                        continue
                    chat.set_system_prompt(cmd_parts[1])
                    print("\n\033[90m┌─[\033[32m✓\033[90m]\033[0m")
                    print("\033[90m└─>\033[0m \033[90mSystem prompt updated\033[0m")
                    continue
                
                # SHOW HISTORY
                elif cmd == "/history" or cmd == "/hist":
                    print("\n\033[90m╔═══════════════════════════════════════════════════════════════════════╗\033[0m")
                    print("\033[90m║\033[0m  \033[36m📜 Conversation History\033[0m" + " " * 41 + "\033[90m║\033[0m")
                    print("\033[90m╠═══════════════════════════════════════════════════════════════════════╣\033[0m")
                    if not conversation_log:
                        print("\033[90m║\033[0m  \033[90mNo messages yet\033[0m" + " " * 54 + "\033[90m║\033[0m")
                    else:
                        for i, msg in enumerate(conversation_log, 1):
                            role_color = "\033[36m" if msg['role'] == 'user' else "\033[32m"
                            role_text = "You" if msg['role'] == 'user' else "AI"
                            content_preview = msg['content'][:50] + "..." if len(msg['content']) > 50 else msg['content']
                            print(f"\033[90m║\033[0m  {role_color}{i}. {role_text}:\033[0m {content_preview}" + " " * max(0, 60 - len(content_preview)) + "\033[90m║\033[0m")
                    print("\033[90m╚═══════════════════════════════════════════════════════════════════════╝\033[0m")
                    continue
                
                # SAVE CONVERSATION
                elif cmd == "/save" or cmd == "/export":
                    filename = cmd_parts[1] if len(cmd_parts) > 1 else f"fote_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    try:
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write("=" * 70 + "\n")
                            f.write(f"FOTE CONVERSATION EXPORT\n")
                            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                            f.write(f"Model: {MODELS[chat.model]['name']}\n")
                            f.write("=" * 70 + "\n\n")
                            for msg in conversation_log:
                                role = "YOU" if msg['role'] == 'user' else "AI"
                                f.write(f"[{role}]: {msg['content']}\n\n")
                        print(f"\n\033[90m┌─[\033[32m✓\033[90m]\033[0m")
                        print(f"\033[90m└─>\033[0m \033[32mConversation saved to: {filename}\033[0m")
                    except Exception as e:
                        print(f"\n\033[90m┌─[\033[31m✗\033[90m]\033[0m")
                        print(f"\033[90m└─>\033[0m \033[31mError saving: {str(e)}\033[0m")
                    continue
                
                # VERSION INFO
                elif cmd == "/version" or cmd == "/v" or cmd == "/info":
                    print("\n\033[90m╔═══════════════════════════════════════╗\033[0m")
                    print("\033[90m║\033[0m  \033[36mFote Version 1.0.0\033[0m            \033[90m║\033[0m")
                    print("\033[90m║\033[0m  \033[90mBy: 765g\033[0m                       \033[90m║\033[0m")
                    print("\033[90m║\033[0m  \033[90mPython: " + f"{sys.version.split()[0]}\033[0m" + " " * (21 - len(sys.version.split()[0])) + "\033[90m║\033[0m")
                    print("\033[90m║\033[0m  \033[90mPlatform: " + f"{platform.system()}\033[0m" + " " * (19 - len(platform.system())) + "\033[90m║\033[0m")
                    print("\033[90m╚═══════════════════════════════════════╝\033[0m")
                    continue
                
                # STATUS INFO
                elif cmd == "/status" or cmd == "/stat":
                    print(f"\n\033[90m╔═══════════════════════════════════════╗\033[0m")
                    print(f"\033[90m║\033[0m  \033[36mCurrent Status\033[0m                \033[90m║\033[0m")
                    print(f"\033[90m╠═══════════════════════════════════════╣\033[0m")
                    print(f"\033[90m║\033[0m  \033[90mModel:\033[0m {MODELS[chat.model]['name'][:25]:<25}\033[90m║\033[0m")
                    print(f"\033[90m║\033[0m  \033[90mProvider:\033[0m {MODELS[chat.model]['provider']:<23}\033[90m║\033[0m")
                    print(f"\033[90m║\033[0m  \033[90mCategory:\033[0m {MODELS[chat.model]['category']:<23}\033[90m║\033[0m")
                    print(f"\033[90m║\033[0m  \033[90mMessages:\033[0m {len(conversation_log):<23}\033[90m║\033[0m")
                    print(f"\033[90m╚═══════════════════════════════════════╝\033[0m")
                    continue
                
                # RELOAD/REFRESH
                elif cmd == "/reload" or cmd == "/refresh":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_banner(MODELS[chat.model]['name'], username, show_instructions=True)
                    print("\n\033[90m┌─[\033[32m✓\033[90m]\033[0m")
                    print("\033[90m└─>\033[0m \033[90mScreen refreshed\033[0m")
                    continue
                
                # UNKNOWN COMMAND
                else:
                    print(f"\n\033[90m┌─[\033[31m✗\033[90m]\033[0m")
                    print(f"\033[90m└─>\033[0m \033[31mUnknown command: {cmd}\033[0m")
                    print(f"\033[90m    Type /help for available commands\033[0m")
                    continue
            
            # Send message and get response
            model_name = MODELS[chat.model]['name']
            provider = MODELS[chat.model]['provider']
            
            print(f"\n\033[90m┌─[\033[32m{model_name}\033[90m · {provider}]\033[0m")
            print(f"\033[90m└─>\033[0m ", end="")
            response = chat.chat(user_input, stream=True)
            
            # Log AI response
            if response:
                conversation_log.append({"role": "assistant", "content": response, "timestamp": datetime.now().isoformat()})
            
        except KeyboardInterrupt:
            print("\n\n\033[90m╔═══════════════════════════════════════╗\033[0m")
            print("\033[90m║\033[0m  \033[33m⚠\033[0m  Interrupted by user          \033[90m║\033[0m")
            print("\033[90m║\033[0m  \033[90mSession terminated\033[0m               \033[90m║\033[0m")
            print("\033[90m╚═══════════════════════════════════════╝\033[0m\n")
            break
        except Exception as e:
            print(f"\n\033[90m┌─[\033[31m✗ Error\033[90m]\033[0m")
            print(f"\033[90m└─>\033[0m \033[31m{str(e)}\033[0m")


def main():
    chat = NvidiaChat()
    
    # Parse arguments
    if len(sys.argv) == 1:
        print_help()
        return
    
    # Check for flags
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_help()
        return
    
    if sys.argv[1] == "-l" or sys.argv[1] == "--list":
        chat.list_models()
        return
    
    # SELECT MODEL INTERACTIVELY
    if sys.argv[1] == "-s" or sys.argv[1] == "--select":
        print("\n\033[36m═══════════════════════════════════════════════════════════════════════\033[0m")
        print("\033[36m                    SELECT YOUR DEFAULT MODEL\033[0m")
        print("\033[36m═══════════════════════════════════════════════════════════════════════\033[0m\n")
        
        # Group models by category
        categories = {"Best": [], "Reasoning": [], "Code": [], "General": []}
        for key, info in MODELS.items():
            categories[info['category']].append((key, info))
        
        model_list = []
        idx = 1
        
        for category, models in categories.items():
            if not models:
                continue
            
            category_color = {
                "Best": "\033[35m",
                "Reasoning": "\033[33m",
                "Code": "\033[32m",
                "General": "\033[36m"
            }.get(category, "\033[37m")
            
            print(f"{category_color}▸ {category}\033[0m")
            for key, info in models:
                model_list.append(key)
                print(f"  \033[90m[{idx}]\033[0m \033[36m{key:<20}\033[0m {info['name']} \033[90m({info['provider']})\033[0m")
                idx += 1
            print()
        
        print("\033[90m═══════════════════════════════════════════════════════════════════════\033[0m")
        
        try:
            choice = input("\n\033[36mSelect model number (or press Enter for default):\033[0m ").strip()
            
            if choice == "":
                print("\033[32m✓\033[0m Using default model: \033[33m" + MODELS[chat.model]['name'] + "\033[0m")
            elif choice.isdigit() and 1 <= int(choice) <= len(model_list):
                selected_key = model_list[int(choice) - 1]
                chat.set_model(selected_key)
                print("\033[32m✓\033[0m Model set to: \033[33m" + MODELS[selected_key]['name'] + "\033[0m")
            else:
                print("\033[31m✗\033[0m Invalid selection. Using default model.")
        except Exception as e:
            print(f"\033[31m✗\033[0m Error: {str(e)}")
        
        # Continue to interactive mode
        print()
        interactive_mode(chat)
        return
    
    if sys.argv[1] == "-i" or sys.argv[1] == "--interactive":
        interactive_mode(chat)
        return
    
    # Handle model selection
    if sys.argv[1] == "-m" or sys.argv[1] == "--model":
        if len(sys.argv) < 4:
            print("\n\033[90m┌─[\033[31m✗ Error\033[90m]\033[0m")
            print("\033[90m└─>\033[0m \033[31mUsage: fote -m <model> \"message\"\033[0m\n")
            return
        model_key = sys.argv[2]
        if not chat.set_model(model_key):
            print(f"\n\033[90m┌─[\033[31m✗ Error\033[90m]\033[0m")
            print(f"\033[90m└─>\033[0m \033[31mModel '{model_key}' not found\033[0m")
            print(f"\033[90m    Use 'fote -l' to see available models\033[0m\n")
            return
        message = sys.argv[3]
    else:
        # Single message mode
        message = sys.argv[1]
    
    # Quick single message
    import getpass
    import os
    username = getpass.getuser()
    model_name = MODELS[chat.model]['name']
    provider = MODELS[chat.model]['provider']
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print banner
    print_banner(model_name, username, show_instructions=False)
    
    # Show user message
    cwd = os.getcwd()
    print(f"\033[90m┌─[\033[36m{cwd}\033[90m]\033[0m")
    print(f"\033[90m└─>\033[0m \033[36m{username}\033[90m:\033[0m {message}")
    
    # Show AI response
    print(f"\n\033[90m┌─[\033[32m{model_name}\033[90m · {provider}]\033[0m")
    print(f"\033[90m└─>\033[0m ", end="")
    
    response = chat.chat(message, stream=True)
    print()


if __name__ == "__main__":
    main()
