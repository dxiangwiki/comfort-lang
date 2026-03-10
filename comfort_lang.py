#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comfort Lang - 以极致清爽交互为核心的新型命令式编程语言
核心特色：
1. 无冗余语法：批量声明/赋值、极简函数定义
2. 直觉式交互：自动反馈结果，无需print
3. 兼容Python：扩展调用Python安全内置函数
作者：（填你的名字/昵称）
版本：1.0.0
"""

import re
import sys
import builtins

class ComfortLang:
    """Comfort Lang 核心解释器类"""
    def __init__(self):
        # 1. 定义需要屏蔽的危险/无关Python内置函数（保障安全+纯粹性）
        self.blocked_funcs = {
            # 系统操作类（避免文件/系统级操作）
            'os', 'sys', 'subprocess', 'open', 'exec', 'eval', 'compile', '__import__',
            # 危险操作类（避免环境篡改）
            'globals', 'locals', 'vars', 'dir', 'help',
            # 交互类（和本语言交互逻辑冲突）
            'input', 'print', 'exit', 'quit'
        }

        # 2. 初始化环境：自定义变量/函数 + 安全的Python内置函数
        self.env = self._load_safe_builtins()

    def _load_safe_builtins(self):
        """加载Python安全的内置函数，作为扩展能力"""
        safe_builtins = {}
        # 遍历所有Python内置函数，过滤危险的
        for name in dir(builtins):
            if (not name.startswith('_')          # 排除私有函数
                and name not in self.blocked_funcs # 排除危险函数
                and callable(getattr(builtins, name))): # 只保留可调用的函数
                safe_builtins[name] = getattr(builtins, name)
        return safe_builtins

    def execute_command(self, cmd):
        """执行单条命令，返回格式化结果"""
        cmd = cmd.strip()
        # 空命令直接返回成功
        if not cmd:
            return "[success]"

        # 1. 批量变量声明：def a b c
        if cmd.startswith('def '):
            try:
                vars_to_define = cmd[4:].split()
                for var in vars_to_define:
                    # 变量名合法性检查
                    if not var.isidentifier():
                        return f"[error] 变量名'{var}'不合法"
                    self.env[var] = None  # 初始值为null
                return "[success]"
            except Exception as e:
                return f"[error] 声明变量失败: {str(e)}"

        # 2. 函数定义：function add = (x,y) => x+y
        elif cmd.startswith('function '):
            try:
                # 拆分函数名和函数体
                func_part = cmd[9:].split(' = ', 1)
                if len(func_part) != 2:
                    return "[error] 函数定义格式错误，正确示例：function add=(x,y)=>x+y"
                func_name, func_body = func_part

                # 解析参数和表达式
                param_match = re.match(r'\((.*?)\) => (.*)', func_body)
                if not param_match:
                    return "[error] 函数体格式错误，正确示例：(x,y)=>x+y"
                params = [p.strip() for p in param_match.group(1).split(',')] if param_match.group(1) else []
                expr = param_match.group(2).strip()

                # 检查参数名合法性
                for param in params:
                    if param and not param.isidentifier():
                        return f"[error] 函数参数名'{param}'不合法"

                # 动态创建函数
                if not params:
                    self.env[func_name] = lambda: eval(expr, self.env)
                else:
                    self.env[func_name] = eval(f"lambda {','.join(params)}: {expr}", self.env)
                return "[success]"
            except Exception as e:
                return f"[error] 定义函数失败: {str(e)}"

        # 3. 多变量赋值：a=10,b=20,c="test"
        elif '=' in cmd and not cmd.startswith('function'):
            try:
                assign_parts = [p.strip() for p in cmd.split(',')]
                for part in assign_parts:
                    var, val = [p.strip() for p in part.split('=', 1)]
                    # 变量名合法性检查
                    if not var.isidentifier():
                        return f"[error] 变量名'{var}'不合法"
                    # 执行赋值（支持Python内置函数扩展）
                    self.env[var] = eval(val, self.env)
                return "[success]"
            except Exception as e:
                return f"[error] 赋值失败: {str(e)}"

        # 4. 变量查询/表达式/函数调用：a / a+b / abs(-10) / add(a,b)
        else:
            try:
                result = eval(cmd, self.env)
                return f"[{result}]"
            except NameError:
                return "[null]"
            except Exception as e:
                return f"[error] 执行失败: {str(e)}"

    def run_repl(self):
        """启动交互式解释器（REPL）"""
        print("="*50)
        print("✨ Comfort Lang - 清爽命令式编程语言 v1.0.0 ✨")
        print("核心特色：无冗余语法 | 直觉式交互 | 兼容Python安全函数")
        print("使用说明：输入 'exit' 退出，输入任意命令直接执行")
        print("="*50 + "\n")

        while True:
            try:
                # 显示提示符，等待用户输入
                cmd = input("> ")
                if cmd.lower() == 'exit':
                    print("\n👋 感谢使用 Comfort Lang！")
                    break
                # 执行命令并输出结果
                result = self.execute_command(cmd)
                print(result)
            except KeyboardInterrupt:
                print("\n[error] 操作被中断（按exit正常退出）")
            except EOFError:
                print("\n👋 感谢使用 Comfort Lang！")
                sys.exit(0)

# 程序入口
if __name__ == "__main__":
    # 创建解释器实例并启动交互模式
    interpreter = ComfortLang()
    interpreter.run_repl()