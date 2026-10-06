# Comfort Lang
一款以「极致清爽的人机交互」为核心设计的新型命令式编程语言，主打“无冗余语法、直觉式操作、兼容Python生态”，让写代码像和计算机对话一样简单～

> Read this document in **[English](./c)**

## ✨ 核心特色
1. **无冗余语法**：砍掉所有为机器解析服务的冗余符号，聚焦“人用着舒服”
   - 批量声明变量：`def a b c`
   - 批量赋值：`a=10,b=20`
   - 极简箭头函数定义：`function add=(x,y)=>x+y`

2. **直觉式交互 REPL**：每一步操作自动反馈结果，**不需要 print**
   - 语句执行成功返回 `[success]`
   - 表达式 / 变量查询返回 `[结果值]`
   - 变量经过 `def` 声明但未赋值：返回 `[None]`
   - 完全未声明、不存在的变量：返回 `[null]`

3. **函数环境快照**
> 定义函数时会对当前全局环境做完整深度快照；
> 函数捕获定义时刻的变量状态，后续全局重新赋值、修改可变对象（list/dict）不会影响已创建函数。
> ⚠️ 当前版本仅支持顶层定义函数，嵌套函数能力后续迭代补齐。

4. **兼容Python生态**：可直接调用Python安全内置函数（`abs()` / `len()` / `max()` / `sum()` 等），扩展能力拉满；
   屏蔽文件、系统、危险执行相关内置。

## 🚀 快速开始
### 环境要求
- Python 3.6+

### 运行方式
1. 克隆本仓库：
```bash
git clone [https://github.com/dxiangwiki/comfort-lang.git](https://github.com/dxiangwiki/comfort-lang.git)
cd comfort-lang
```

2. 启动交互式解释器：
```bash
python comfort_lang.py
```
输入 `exit` 退出 REPL 终端。

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
> abs(-100)
[100]
> len("Hello Comfort Lang")
[17]

# 变量声明但未赋值返回 [None]
> def m
[success]
> m
[None]

# 访问完全不存在变量返回 [null]
> n
[null]

# 函数环境快照演示
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
👋 感谢使用 Comfort Lang！
```

## ⚠️ 安全提示
✅ 本地使用完全安全：下载至个人设备运行交互式 REPL，可正常 clone、Star、Fork，支持 GitHub 公开分享与二次迭代。

❌ **不建议直接部署为公网在线后端服务**：
解释器内部使用 Python `eval` 执行表达式，即便内置危险函数黑名单，仍然无法完全抵御外部不可信输入的各类逃逸风险。
本项目尚处于早期渐进式迭代阶段，优先面向本地交互开发场景，暂不作为线上服务组件使用。

## 📌 当前限制
- `function` 仅支持顶层命令定义，**不支持在表达式内部嵌套定义函数**，暂未实现完整词法闭包。
- 当前仅提供 REPL 交互模式，暂不支持读取执行 `.cl` 脚本文件。
- 暂不支持 `{}` 代码块、if / while 语句，目前仅支持表达式运算。
- 后续版本会逐步补齐语句块、条件、循环、脚本文件加载等能力。

## 📄 许可证
MIT License

## 💡 设计理念
Comfort Lang 不是Python的“简化版”，而是重构了“人写代码”的交互逻辑——核心是“体验优先”，Python只是我们的扩展生态，而非底层依赖。

