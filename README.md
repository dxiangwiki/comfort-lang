# Comfort Lang
一款以「极致清爽的人机交互」为核心设计的新型命令式编程语言，主打“无冗余语法、直觉式操作、兼容Python生态”，让写代码像和计算机对话一样简单～

## ✨ 核心特色
1. **无冗余语法**：砍掉所有为机器解析服务的冗余符号，聚焦“人用着舒服”
   - 批量声明变量：`def a b c`
   - 批量赋值：`a=10,b=20`
   - 极简函数定义：`function add=(x,y)=>x+y`
2. **直觉式交互**：每一步操作自动反馈结果，无需手动`print`
   - 成功操作返回 `[success]`
   - 查询/计算返回 `[结果值]`
   - 未定义变量返回 `[null]`
3. **兼容Python生态**：可直接调用Python安全内置函数（如`abs()`/`len()`/`max()`），扩展能力拉满

## 🚀 快速开始
### 环境要求
- Python 3.6+

### 运行方式
1. 克隆本仓库：
   ```bash
   git clone https://github.com/dxiangwiki/comfort-lang.git
   cd comfort-lang
   ```
2. 启动交互式解释器：
   ```bash
   python comfort_lang.py
   ```

### 使用示例
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
> abs(-100)  # 兼容Python内置函数
[100]
> len("Hello Comfort Lang")
[17]
> exit
👋 感谢使用 Comfort Lang！
```

## 📄 许可证
MIT License

## 💡 设计理念
Comfort Lang 不是Python的“简化版”，而是重构了“人写代码”的交互逻辑——核心是“体验优先”，Python只是我们的扩展生态，而非底层依赖。
