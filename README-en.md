# Comfort Lang
A new imperative programming language centered on "ultra‑clean human‑computer interaction".
It pursues "no redundant syntax, intuitive operations, and Python‑ecosystem compatibility", making coding as natural as talking with a computer.

> Read this document in **[中文](./README.md)**

## ✨ Core Features
1. **Redundancy‑free syntax**: Focus on human‑friendly experience.
   - Batch variable declaration: `def a b c`
   - Batch assignment: `a=10,b=20`
   - Minimal arrow‑style function definition: `function add=(x,y)=>x+y`

2. **Intuitive REPL interaction**: Results are returned automatically, no `print` required.
   - Successful statement returns `[success]`
   - Expression / variable query returns `[value]`
   - Variable declared via `def` but unassigned: returns `[None]`
   - Undeclared, non‑existent variable: returns `[null]`

3. **Function environment snapshot**
> When defining a function, a deep‑copy snapshot of the global environment is created.
> Functions capture variable states at definition time. Later re‑assignments or modifications to mutable objects (list / dict) will not affect existing functions.
> ⚠️ Only top‑level function definitions are supported. Nested functions will be implemented in future versions.

4. **Python‑ecosystem compatible**: Directly call safe Python built‑ins such as `abs()` / `len()` / `max()` / `sum()`.
System‑related and dangerous built‑ins are blocked.

## 🚀 Quick Start
### Requirements
- Python 3.6+

### Run
1. Clone repository:
```bash
git clone [https://github.com/dxiangwiki/comfort-lang.git](https://github.com/dxiangwiki/comfort-lang.git)
cd comfort-lang
```

2. Launch REPL interpreter:
```bash
python comfort_lang.py
```
Type `exit` to quit the REPL terminal.

### Usage Examples
```bash
> def a b c
[success]
> function add=(x,y)=>x+y
[success]
> a=10,b=20
[success]
> a
[10]
> b
[20]
> a+b
[30]
> add(a,b)
[30]
> abs(-100)
[100]
> len("Hello Comfort Lang")
[17]

# Declared but unassigned variable returns [None]
> def m
[success]
> m
[None]

# Accessing non‑existent variable returns [null]
> n
[null]

# Function environment snapshot demo
> def arr
[success]
> arr=[1,2,3]
[success]
> function get_arr=()=>arr
[success]
> get_arr()
[[1, 2, 3]]
> arr.append(99)
[None]
> get_arr()
[[1, 2, 3]]

> exit
👋 Thank you for using Comfort Lang!
```

## ⚠️ Security Notice
✅ Safe for local usage: Download and run REPL on your local device. You may clone, Star, Fork and share this project publicly for further iteration.

❌ **Not recommended to deploy as public online backend service**:
The interpreter uses Python `eval` under the hood. Even with a blocklist for dangerous functions, it cannot fully resist escape attacks from untrusted external input.

This project is in the early progressive‑iteration stage. It is designed for local interactive development scenarios and should **not** be used directly as an online service component.

## 📌 Current Limitations
- `function` definitions are only allowed at top‑level. Nested function definitions inside expressions are unsupported; full lexical closure is not yet implemented.
- Only REPL interactive mode is available; loading `.cl` script files is not supported yet.
- No block syntax `{}`, no `if / while` statements. Only expression evaluation is supported currently.
- Future releases will add statement blocks, conditionals, loops, and script‑file loading capabilities.

## 📄 License
MIT License

## 💡 Design Philosophy
Comfort Lang is **not a simplified version of Python**. It re‑thinks the human‑computer interaction experience of programming. Python acts only as an extension ecosystem rather than the underlying core.
