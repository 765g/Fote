#!/usr/bin/env python3
"""
Test script to check NVIDIA API connectivity and list available models
"""

import requests
import json

NVIDIA_API_KEY = "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"
NVIDIA_API_BASE = "https://integrate.api.nvidia.com/v1"

def list_models():
    print("Fetching available models from NVIDIA API...")
    print(f"API URL: {NVIDIA_API_BASE}/models")
    print()
    
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}"
    }
    
    try:
        response = requests.get(f"{NVIDIA_API_BASE}/models", headers=headers, timeout=30)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            models = response.json()
            print("✓ Successfully retrieved models!")
            print()
            print(json.dumps(models, indent=2))
            
            if "data" in models:
                print(f"\n\nFound {len(models['data'])} models:")
                for model in models['data']:
                    print(f"  - {model['id']}")
        else:
            print("✗ API Error")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"✗ Error: {str(e)}")

def test_chat(model_id="meta/llama-3.1-8b-instruct"):
    print(f"\n\nTesting chat with model: {model_id}")
    print("=" * 60)
    
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model_id,
        "messages": [
            {"role": "user", "content": "Say hello in one word"}
        ],
        "temperature": 0.7,
        "max_tokens": 50,
        "stream": False
    }
    
    try:
        response = requests.post(f"{NVIDIA_API_BASE}/chat/completions", 
                                headers=headers, json=payload, timeout=30)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✓ Chat test successful!")
            print()
            print(json.dumps(result, indent=2))
        else:
            print("✗ Chat Error")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"✗ Error: {str(e)}")

if __name__ == "__main__":
    list_models()
    print("\n" + "=" * 60)
    test_chat()

