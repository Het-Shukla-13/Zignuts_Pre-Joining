import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass

class ConnectionManager:
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.connection=None
        self.getConnection(host, port, user, password, database)
    
    def getConnection(self, host: str, port: int, user: str, password: str, database: str):
        try:
            self.connection = connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print(f"Connected to MySQL Server...")
                print(f"Connected to database: {database}")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def closeConnection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

class BankAccount:
    def __init__(self, connection: ConnectionManager):
        self.connection=connection.connection
        self.createRel()

    def createRel(self):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    account_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    balance FLOAT NOT NULL DEFAULT 0.0
                )
            """)
            self.connection.commit()
            cursor.close()
            print("Accounts table is ready.")
        except Error as e:
            print(f"Error creating table: {e}")

    def create_account(self, name: str, initial_deposit: float = 0.0):
        try:
            cursor=self.connection.cursor()
            cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, initial_deposit))
            self.connection.commit()
            account_id=cursor.lastrowid
            cursor.close()
            print(f"Account created for {name} with ID {account_id} and initial deposit {initial_deposit}.")
        except Error as e:
            print(f"Error creating account: {e}")

    def get_account(self, acc_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT account_id, name, balance FROM accounts WHERE account_id = %s", (acc_id,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return {"account_id": result[0], "name": result[1], "balance": result[2]}
            else:
                raise ValueError("Account not found.")
        except Error as e:
            print(f"Error fetching account: {e}")
            return None

    def deposit(self, acc_id: int, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account=self.get_account(acc_id)
        if account is not None:
            try:
                cursor = self.connection.cursor()
                cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, acc_id))
                self.connection.commit()
                cursor.close()
                print(f"Deposited {amount} to account ID {acc_id}.")
            except Error as e:
                print(f"Error during deposit: {e}")
        else:
            raise ValueError("Account not found.")

    def withdraw(self, acc_id: int, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        account=self.get_account(acc_id)
        if account is None:
            raise ValueError("Account not found.")
        else:
            try:
                cursor = self.connection.cursor()
                if account["balance"] >= amount:
                    cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", (amount, acc_id))
                    self.connection.commit()
                    print(f"Withdrew {amount} from account ID {acc_id}.")
                else:
                    raise ValueError("Insufficient funds or account not found.")
                cursor.close()
            except Error as e:
                print(f"Error during withdrawal: {e}")
    
    def get_balance(self, acc_id: int) -> float:
        account=self.get_account(acc_id)
        if account is not None:
            return account["balance"]
        else:
            raise ValueError("Account not found.")
        
def main():
    host=input("Enter MySQL host: ")
    port=int(input("Enter MySQL port: "))
    user=input("Enter MySQL username: ")
    password=getpass("Enter MySQL password: ")
    database=input("Enter database name: ")

    conn_manager=ConnectionManager(host, port, user, password, database)
    bank=BankAccount(conn_manager)

    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice=input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)
        elif choice =='2':
            acc_id=int(input("Enter account ID: "))
            amount=float(input("Enter deposit amount: "))
            try:
                bank.deposit(acc_id, amount)
            except ValueError as err:
                print(err)
        elif choice == '3':
            acc_id=int(input("Enter account ID: "))
            amount=float(input("Enter withdrawal amount: "))
            try:
                bank.withdraw(acc_id, amount)
            except ValueError as err:
                print(err)
        elif choice == '4':
            acc_id=int(input("Enter account ID: "))
            try:
                balance=bank.get_balance(acc_id)
                print(f"Account ID {acc_id} has a balance of {balance}.")
            except ValueError as ve:
                print(ve)
        elif choice == '5':
            conn_manager.closeConnection()
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")

main()