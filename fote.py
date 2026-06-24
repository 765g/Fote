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
                print("[No response received]")
            return full_response
        except Exception as e:
            print(f"[Stream error: {str(e)}]")
            return ""
    
    def clear_conversation(self):
        """Clear conversation history"""
        self.conversation = []
    
    def list_models(self):
        """List all available models - simple format"""
        print("\nAvailable models:\n")
        
        categories = {"Best": [], "Reasoning": [], "Code": [], "General": []}
        for key, info in MODELS.items():
            categories[info['category']].append((key, info))
        
        for category, models in categories.items():
            if not models:
                continue
            print(f"{category}:")
            for key, info in models:
                print(f"  {key:<25} {info['name']} ({info['provider']})")
            print()


def print_banner(model_name=None, username=None, show_instructions=False):
    """Print minimal CLI banner like FreeBuff"""
    import os
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Super simple banner - just the name and one line
    print("\033[32mFote\033[0m - Free AI in terminal")
    if model_name:
        print(f"Model: {model_name}")
    print()


def print_help():
    """Print simple help"""
    print("\nFote - Free AI in terminal\n")
    print("Usage:")
    print("  fote \"message\"          - Quick chat")
    print("  fote -i                 - Interactive mode")
    print("  fote -s                 - Select model")
    print("  fote -l                 - List models")
    print("  fote -m <model> \"msg\"   - Use specific model")
    print("\nCommands:")
    print("  /model <name>  - Change model")
    print("  /models        - List models")
    print("  /clear         - Clear chat")
    print("  /save [file]   - Save conversation")
    print("  /help          - Show help")
    print("  /exit          - Quit")
    print()


def interactive_mode(chat):
    """Run interactive chat mode - minimal like FreeBuff"""
    import os
    
    model_name = MODELS[chat.model]['name']
    
    # Print minimal banner
    print_banner(model_name)
    
    conversation_log = []
    
    while True:
        try:
            # Super simple prompt - just >
            user_input = input("> ").strip()
            
            if not user_input:
                continue
            
            conversation_log.append({"role": "user", "content": user_input, "timestamp": datetime.now().isoformat()})
            
            # Handle commands
            if user_input.startswith("/"):
                cmd_parts = user_input.split(maxsplit=1)
                cmd = cmd_parts[0].lower()
                
                if cmd in ["/exit", "/quit", "/q"]:
                    print("Bye!")
                    break
                
                elif cmd in ["/help", "/h", "/?"]:
                    print("\nCommands:")
                    print("  /model <name>  - Change model")
                    print("  /models        - List models")
                    print("  /clear         - Clear chat")
                    print("  /save [file]   - Save conversation")
                    print("  /exit          - Quit\n")
                    continue
                
                elif cmd in ["/models", "/list", "/ls"]:
                    print("\nModels:")
                    for key, info in MODELS.items():
                        print(f"  {key:<20} {info['name']}")
                    print()
                    continue
                
                elif cmd in ["/clear", "/cls", "/reset"]:
                    chat.clear_conversation()
                    conversation_log = []
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_banner(MODELS[chat.model]['name'])
                    continue
                
                elif cmd in ["/model", "/m", "/use"]:
                    if len(cmd_parts) < 2:
                        print("Usage: /model <name>\n")
                        continue
                    model_key = cmd_parts[1]
                    if chat.set_model(model_key):
                        print(f"Model: {MODELS[model_key]['name']}\n")
                    else:
                        print(f"Model '{model_key}' not found\n")
                    continue
                
                elif cmd in ["/save", "/export"]:
                    filename = cmd_parts[1] if len(cmd_parts) > 1 else f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    try:
                        with open(filename, 'w', encoding='utf-8') as f:
                            for msg in conversation_log:
                                role = "You" if msg['role'] == 'user' else "AI"
                                f.write(f"{role}: {msg['content']}\n\n")
                        print(f"Saved: {filename}\n")
                    except Exception as e:
                        print(f"Error: {str(e)}\n")
                    continue
                
                else:
                    print(f"Unknown command: {cmd}")
                    print("Type /help for commands\n")
                    continue
            
            # Send message and stream response
            response = chat.chat(user_input, stream=True)
            print()
            
            if response:
                conversation_log.append({"role": "assistant", "content": response, "timestamp": datetime.now().isoformat()})
            
        except KeyboardInterrupt:
            print("\n\nBye!")
            break
        except EOFError:
            print("\nBye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


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
        print("\nSelect model:\n")
        
        # Group models by category
        categories = {"Best": [], "Reasoning": [], "Code": [], "General": []}
        for key, info in MODELS.items():
            categories[info['category']].append((key, info))
        
        model_list = []
        idx = 1
        
        for category, models in categories.items():
            if not models:
                continue
            print(f"{category}:")
            for key, info in models:
                model_list.append(key)
                print(f"  [{idx}] {key:<20} {info['name']} ({info['provider']})")
                idx += 1
            print()
        
        try:
            choice = input("Select number (or Enter for default): ").strip()
            
            if choice == "":
                print(f"Using: {MODELS[chat.model]['name']}\n")
            elif choice.isdigit() and 1 <= int(choice) <= len(model_list):
                selected_key = model_list[int(choice) - 1]
                chat.set_model(selected_key)
                print(f"Model: {MODELS[selected_key]['name']}\n")
            else:
                print("Invalid selection. Using default.\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")
        
        # Continue to interactive mode
        interactive_mode(chat)
        return
    
    if sys.argv[1] == "-i" or sys.argv[1] == "--interactive":
        interactive_mode(chat)
        return
    
    # Handle model selection
    if sys.argv[1] == "-m" or sys.argv[1] == "--model":
        if len(sys.argv) < 4:
            print("\nError: Usage: fote -m <model> \"message\"\n")
            return
        model_key = sys.argv[2]
        if not chat.set_model(model_key):
            print(f"\nError: Model '{model_key}' not found")
            print("Use 'fote -l' to see available models\n")
            return
        message = sys.argv[3]
    else:
        # Single message mode
        message = sys.argv[1]
    
    # Quick single message - minimal output
    import os
    model_name = MODELS[chat.model]['name']
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print banner
    print_banner(model_name)
    
    # Show user message
    print(f"> {message}\n")
    
    # Show AI response
    response = chat.chat(message, stream=True)
    print()


if __name__ == "__main__":
    main()
