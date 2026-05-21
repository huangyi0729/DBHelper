class BankAccount:
    def __init__(self, account_id, name, initial_balance, password):
        self.account_id = account_id
        self.name = name
        self._balance = initial_balance
        self._password = password

    def _verify_password(self, input_pwd):
        return self._password == input_pwd

    def show_balance(self, password):
        if self._verify_password(password):
            print(f"账户 {self.account_id} - {self.name} 当前余额: {self._balance:.2f}")
            return self._balance
        else:
            print("密码错误，无法查看余额！")
            return None

    def deposit(self, amount):
        if amount <= 0:
            print("存款金额必须为正数！")
            return False
        self._balance += amount
        print(f"存款成功！存入 {amount:.2f}，当前余额: {self._balance:.2f}")
        return True

    def withdraw(self, amount, password):
        if not self._verify_password(password):
            print("密码错误，无法取款！")
            return False
        if amount <= 0:
            print("取款金额必须为正数！")
            return False
        if amount > self._balance:
            print("余额不足，取款失败！")
            return False
        self._balance -= amount
        print(f"取款成功！取出 {amount:.2f}，剩余余额: {self._balance:.2f}")
        return True

    def change_password(self, old_password, new_password):
        if not self._verify_password(old_password):
            print("旧密码错误，修改失败！")
            return False
        if len(new_password) < 6:
            print("新密码长度至少为6位！")
            return False
        self._password = new_password
        print("密码修改成功！")
        return True

    def calculate_simple_interest(self, annual_rate, years):
        if annual_rate < 0 or years < 0:
            print("利率和年限不能为负数！")
            return 0.0
        interest = self._balance * annual_rate * years
        print(f"当前余额 {self._balance:.2f}，按年利率 {annual_rate * 100:.2f}%，存 {years} 年，单利利息: {interest:.2f}")
        return interest

    def calculate_compound_interest(self, annual_rate, years):
        if annual_rate < 0 or years < 0:
            print("利率和年限不能为负数！")
            return self._balance
        final_balance = self._balance * ((1 + annual_rate) ** years)
        interest = final_balance - self._balance
        print(f"复利计算：本金 {self._balance:.2f}，年利率 {annual_rate * 100:.2f}%，"
              f"存 {years} 年（利息每年滚入本金），最终本息和: {final_balance:.2f}，总利息: {interest:.2f}")
        return final_balance

    def deposit_simple_interest(self, annual_rate, years, password):
        if not self._verify_password(password):
            print("密码错误，无法存入利息！")
            return False
        interest = self.calculate_simple_interest(annual_rate, years)
        if interest > 0:
            self._balance += interest
            print(f"利息 {interest:.2f} 已存入账户，新余额: {self._balance:.2f}")
            return True
        return False


def print_menu():
    print("\n" + "=" * 40)
    print("银行账户系统")
    print("=" * 40)
    print("1. 查看余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 修改密码")
    print("5. 利息/复利计算")
    print("0. 退出系统")
    print("=" * 40)


if __name__ == "__main__":
    print("=== 银行账户开户 ===")
    account_id = input("请输入账号：")
    name = input("请输入姓名：")
    initial_balance = float(input("请输入初始余额："))
    password = input("请输入密码（至少6位）：")
    if len(password) < 6:
        print("警告：密码长度不足6位，建议修改！")

    acc = BankAccount(account_id, name, initial_balance, password)
    print(f"\n账户 {account_id} 创建成功！欢迎 {name}。")

    while True:
        print_menu()
        choice = input("请选择操作（输入数字）：").strip()

        if choice == "0":
            print("感谢使用，再见！")
            break

        elif choice == "1":
            pwd = input("请输入密码：")
            acc.show_balance(pwd)

        elif choice == "2":
            try:
                amount = float(input("请输入存款金额："))
                acc.deposit(amount)
            except ValueError:
                print("金额输入无效，请输入数字。")

        elif choice == "3":
            pwd = input("请输入密码：")
            try:
                amount = float(input("请输入取款金额："))
                acc.withdraw(amount, pwd)
            except ValueError:
                print("金额输入无效，请输入数字。")

        elif choice == "4":
            old_pwd = input("请输入旧密码：")
            new_pwd = input("请输入新密码（至少6位）：")
            acc.change_password(old_pwd, new_pwd)

        elif choice == "5":
            print("\n--- 利息/复利计算 ---")
            print("1. 查看单利利息（不存入账户）")
            print("2. 查看复利本息和（利息每年滚入本金）")
            print("3. 将单利利息存入账户（需密码）")
            print("0. 返回上级菜单")
            sub_choice = int(input("请选择（输入数字）：").strip())

            if sub_choice == "0":
                continue

            try:
                rate = float(input("请输入年利率（例如 0.035 表示 3.5%）："))
                years = float(input("请输入存款年限："))
            except ValueError:
                print("利率或年限输入无效，请输入数字。")
                continue

            if sub_choice == "1":
                acc.calculate_simple_interest(rate, years)
            elif sub_choice == "2":
                acc.calculate_compound_interest(rate, years)
            elif sub_choice == "3":
                pwd = input("请输入密码：")
                acc.deposit_simple_interest(rate, years, pwd)
            else:
                print("无效选项，返回上级菜单。")

        else:
            print("无效选项，请重新输入。")