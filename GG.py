class Calculator:
    def __init__(self):
        self.memory = 0  # 记忆功能
        self.history = []  # 历史记录

    def add(self, a, b):
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result

    def _add_to_history(self, operation):
        self.history.append(operation)
        # 限制历史记录条数
        if len(self.history) > 10:
            self.history.pop(0)

    def memory_add(self, value):
        self.memory += value
        return self.memory

    def memory_subtract(self, value):
        self.memory -= value
        return self.memory

    def memory_clear(self):
        self.memory = 0
        return self.memory

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        return "历史记录已清空"

def main():
    calc = Calculator()
    print("简易计算器 (输入 'q' 退出)")
    print("可用操作: +, -, *, /, m+, m-, mc, hist, clear")

    while True:
        user_input = input("请输入表达式 (例如 2 + 3): ").strip()

        if user_input == 'q':
            print("退出计算器")
            break

        #处理记忆功能
        if user_input.lower() == 'm+':
            try:
                value = float(input("输入要加到记忆的数字: "))
                print(f"记忆值: {calc.memory_add(value)}")
            except ValueError:
                print("无效输入")
            continue

        if user_input.lower() == 'm-':
            try:
                value = float(input("输入要从记忆减去的数字: "))
                print(f"记忆值: {calc.memory_subtract(value)}")
            except ValueError:
                print("无效输入")
            continue

        if user_input.lower() == 'mc':
            print(f"记忆已清除: {calc.memory_clear()}")
            continue

        #处理历史记录
        if user_input.lower() == 'hist':
            print("\n计算历史")
            for item in calc.get_history():
                print(item)
            print()
            continue

        if user_input.lower() == 'clear':
            print(calc.clear_history())
            continue

        #处理普通计算
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("格式错误，应为: 数字 运算符 数字")
                continue

            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])

            if op == '+':
                print(f'结果：{calc.add(a,b)}')
            elif op == '-':
                print(f'结果：{calc.subtract(a,b)}')
            elif op == '*':
                print(f'结果：{calc.multiply(a, b)}')
            elif op == '/':
                try:
                    print(f'结果：{calc.divide(a, b)}')
                except ValueError as e:
                    print(e)
            else:
                print("不支持的操作符")
        except ValueError:
            print("无效的数字输入")

if __name__ == "__main__":
    main()
