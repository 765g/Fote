# 🎯 Fote Usage Examples

## 1. Quick Questions

### General Knowledge
```bash
fote "what is quantum entanglement?"
fote "explain the theory of relativity in simple terms"
fote "what are the 7 wonders of the world?"
```

### Programming Concepts
```bash
fote "explain async/await in javascript"
fote "what is the difference between heap and stack memory?"
fote "explain dependency injection"
```

---

## 2. Code Generation

### Python
```bash
fote -m codestral "write a python function to validate email addresses"
fote -m deepseek-coder "create a REST API using FastAPI with CRUD operations"
fote -m granite-code "write a python script to scrape website data"
```

### JavaScript
```bash
fote -m codestral "write a react component for a todo list"
fote -m codegemma "create an express.js server with authentication"
```

### Other Languages
```bash
fote -m codestral "write a rust program to parse JSON"
fote -m granite-code "create a Java Spring Boot application"
```

---

## 3. Debugging Help

```bash
fote -m deepseek-v4 "debug this code: for i in range(10) print(i)"
fote -m codestral "why am I getting a null pointer exception in this code: [paste code]"
fote -m llama-3.3-70b "fix this SQL query: SELECT * FROM users WHERE age > 18 AND"
```

---

## 4. Math & Logic Problems

```bash
fote -m deepseek-v4 "solve: if x^2 + 5x + 6 = 0, what is x?"
fote -m qwen-397b "calculate the area under the curve y=x^2 from x=0 to x=5"
fote -m nemotron-ultra "explain Bayes' theorem with an example"
```

---

## 5. Writing & Content

```bash
fote -m mistral-medium "write a professional email to decline a job offer"
fote -m llama-3.3-70b "create a README for a weather API project"
fote -m nemotron-super "write a technical blog post about microservices"
```

---

## 6. Data Analysis

```bash
fote -m deepseek-v4 "analyze this dataset: [paste data] and give insights"
fote -m qwen-397b "what statistical test should I use to compare two groups?"
fote -m nemotron-ultra "explain principal component analysis"
```

---

## 7. System Design

```bash
fote -m nemotron-ultra "design a scalable URL shortener system"
fote -m deepseek-v4 "how would you design a real-time chat application?"
fote -m mistral-large-3 "explain microservices vs monolithic architecture"
```

---

## 8. Interactive Mode Workflows

### Learning Session
```bash
fote -i

You: /model nemotron-super
Bot: ✓ Model changed to: Nemotron Super 49B

You: explain recursion
Bot: [Explains recursion]

You: give me an example in python
Bot: [Provides code example]

You: what are the performance implications?
Bot: [Explains performance]

You: /clear
Bot: ✓ Conversation cleared
```

### Coding Session
```bash
fote -i

You: /model codestral
Bot: ✓ Model changed to: Codestral 22B

You: I need to build a TODO API in Express.js
Bot: [Provides code structure]

You: add authentication with JWT
Bot: [Adds authentication code]

You: how do I test this?
Bot: [Provides test examples]

You: /exit
```

---

## 9. Model Comparison

### Try Different Models for Same Question
```bash
# Fast response
fote -m llama-4-maverick "explain docker containers"

# Detailed explanation
fote -m nemotron-ultra "explain docker containers"

# Code-focused
fote -m codestral "explain docker containers with examples"
```

---

## 10. Advanced System Prompts

```bash
fote -i

You: /system You are a senior software architect with 20 years of experience
Bot: ✓ System prompt updated

You: review my database schema
Bot: [Provides expert-level review]
```

---

## 11. Real-World Scenarios

### Interview Preparation
```bash
fote -m nemotron-ultra "explain how you would implement a cache system"
fote -m deepseek-v4 "solve: reverse a linked list"
fote -m llama-3.3-70b "behavioral question: tell me about a time you solved a complex problem"
```

### Code Review
```bash
fote -m codestral "review this code for security issues: [paste code]"
fote -m granite-code "suggest improvements for this function: [paste code]"
```

### Documentation
```bash
fote -m mistral-medium "write API documentation for these endpoints: [paste routes]"
fote -m llama-3.3-70b "create user documentation for this feature"
```

---

## 12. Quick Commands Cheatsheet

```bash
# Quick question
fote "your question here"

# Specific model
fote -m <model-name> "your question"

# Interactive mode
fote -i

# List models
fote -l

# Help
fote -h
```

---

## Pro Tips 💡

1. **Use the best model for hard questions**: `nemotron-ultra`, `mistral-large-3`
2. **Use fast models for simple tasks**: `llama-4-maverick`, `phi-4`
3. **Use code models for programming**: `codestral`, `granite-code`, `deepseek-coder`
4. **Use reasoning models for logic**: `deepseek-v4`, `qwen-397b`, `glm-5`
5. **Interactive mode is best for conversations**: `fote -i`
6. **Switch models in interactive mode**: `/model <name>`
7. **Clear history to start fresh**: `/clear`
8. **Set custom personality**: `/system <prompt>`

---

**Happy Coding! 🚀**
