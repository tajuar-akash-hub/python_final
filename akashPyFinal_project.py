import random

class User:
    user_list= []
    def __init__(self,name,user_email,user_address,acc_type):
        
        self.name=name
        self.user_email=user_email
        self.user_address=user_address
        self.acc_type=acc_type
        self.Balance=0
        self.account_number = self.generate_account_number()
        self.Transaction_history = []
        self.loan_count = 2
        User.user_list.append(self)

    
    loan_enabled=True
    is_bankrupt=False

    @staticmethod
    def generate_account_number():
        return random.randint(10000, 99999)
    
    def deposit(self,depo_Amount):
        if(depo_Amount>=0):
            self.Balance+=depo_Amount
            self.Transaction_history.append(f'Desposite:{depo_Amount}')
        else:
            print("Invalid deposite Amount")

    def Withdraw(self,withdraw_Amount):
        if(withdraw_Amount>=0 and withdraw_Amount<=self.Balance):
            self.Balance-=withdraw_Amount
            self.Transaction_history.append(f'withdraw:{withdraw_Amount}')
        elif(withdraw_Amount>self.Balance):
            print("Withdrawal amount exceeded")

    def Check_balance(self):
        print(f'current Balance is {self.Balance}')

    def Check_Transaction_Transaction_history(self):
        return self.Transaction_history
    
    def take_loan(self, loan_amount):
        if User.is_bankrupt==True:
            print("Bank is bankrupt. Loan Can't Possible.")
            return False

        if User.loan_enabled==True and self.loan_count > 0 and self.Balance >= loan_amount and loan_amount <= 10000:
            self.Balance += loan_amount
            self.loan_count -= 1
            self.Transaction_history.append(f'Loan: +{loan_amount}')
            # return True
        elif  User.loan_enabled==False:
            print("Loan is now closed.")
            return False
        elif self.loan_count <= 0:
            print("\nCan't take loan more than twice.")
            return False
        elif loan_amount > 10000:
            print("Loan limit Exceeded.")
            return False
        else:
            print("Denied.")
            return False
        
    def transfer(self,transfer_to_user,transfer_amount):
        if User.is_bankrupt==True:
            print("Bank is bankrupt.")
            return False

        if self.Balance >= transfer_amount and transfer_to_user is not None:
            self.Balance-=transfer_amount
            transfer_to_user.Balance+=transfer_amount
            self.Transaction_history.append(f'Transfer: {transfer_amount}')
            transfer_to_user.Transaction_history.append(f'Transfer: +{transfer_amount}')
            return True
        else:
            print("Account does not exist")
            return False
    @staticmethod
    def user_exists(account_no):
        for user in User.user_list:
            if user.account_number == account_no:
                return user
        return None
class Admin:
    def __init__(self) -> None:
        pass
    def admin_login(self):
        username = input("Admin Username: ")
        password = input("Admin Password: ")
        return username == "admin" , password == "admin"
    def create_account(self,name,email,address,account_type):
        user = User(name, email, address, account_type)
        User.user_list.append(user)
        
    def delete_account(self,ac_number):

        for user in User.user_list:
            if(user.account_number==ac_number):
                User.user_list.remove(user)

    def see_user_Accounts(self):
        for user in User.user_list:
            print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.Balance}\n")

   
    def check_total_balance(self):
        total_balance = sum(user.Balance for user in User.user_list)
        return total_balance
    def Total_loan_Amount(self):
        pass
   
    def toggle_loan_feature(self, Enable):
        User.loan_enabled = Enable

    def toggle_bankrupt_status(self, is_bankrupt):
        User.is_bankrupt = is_bankrupt

# replica of the system 

current_user = None
admin = Admin()

while True:
    if current_user is None:
        print("No User Logged in!")
        op=input('Login or Register or Admin (L/R/A): ')
        if op=='R':
            name=input('Name: ')
            email=input('Email: ')
            address=input('Address: ')
            account_type=input('(sv/cu)? ')
            current_user=User(name,email,address,account_type)
            User.user_list.append(current_user)
            print(f'Account successfully registered!\nAccount Number: {current_user.account_number}')
        
        elif op=='L':
         
                ac_no = int(input('Account Number: '))
          
                current_user = User.user_exists(ac_no)
                if not  current_user:
                    print("Account dosn't exist.")
                    continue

        elif op=='A':
            admin = Admin()
            if admin.admin_login():
                print("Admin Menu:")
                print("1. Create Account")
                print("2. Delete User Account")
                print("3. ON or OFF Loan Feature")
                print("4. View User Accounts")
                print("5. Check Total Balance")
                print("6. Check Total Loan Amount")
                print("7. ON or OFF Bankrupt Status")
                print("8. Logout.")
                Admin_choice = int(input("Enter your choice: "))

                if Admin_choice == 1:
                    name = input("Enter User's Name: ")
                    email = input("Enter User's Email: ")
                    address = input("Enter User's Address: ")
                    account_type = input("Enter User's Account Type Savings or Current (sv/cu): ")
                    admin.create_account(name, email, address, account_type)
                elif Admin_choice == 2:
                    ac_no = int(input("Enter User's Account Number to delete: "))
                    admin.delete_account(ac_no)
                elif Admin_choice == 3:
                    toggle_option = input("Loan Feature On/Off (True/False): ")
                    admin.toggle_loan_feature(toggle_option == 'True')
                elif Admin_choice == 4:
                    admin.see_user_Accounts()
                elif Admin_choice == 5:
                    print("Total Balance: ", admin.check_total_balance())
                elif Admin_choice == 6:
                    print("Total Loan Amount: ", admin.Total_loan_Amount())
                elif Admin_choice == 7:
                    toggle_option = input("Bankrupt Status On/Off (True/False): ")
                    admin.toggle_bankrupt_status(toggle_option == 'True')
                elif Admin_choice == 8:
                    print("Admin Logged-out Successfully.\n")
                else:
                    print("Invalid.")
            else:
                print("Unsuccessfull.")
        else:
            print('Invalid choice\n')

    else:
        print(f'\nWelcome {current_user.name}!\n')
        if current_user.acc_type == 'sv':
            print('\n1. Show Info')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Check Balance')
            print('5. Change Info')
            print('6. Show Transaction Transaction_history')
            print('7. Take Loan')
            print('8. Transfer Money')
            print('9. Logout')

            op = input('Choose Option: ')

            if op=='1':
                print(f'Name: {current_user.name}')
                print(f'Account Number: {current_user.account_number}')
                print(f'Account Type: {current_user.acc_type}')
                print(f'Balance: {current_user.Balance}')
            elif op=='2':
                amount = float(input('Amount: '))
                current_user.deposit(amount)
            elif op=='3':
                amount = float(input('Amount: '))
                current_user.Withdraw(amount)
            elif op=='4':
                print(f'Available Balance: {current_user.Check_balance()}')
            elif op=='5':
                name = input('New Name: ')
                email = input('New Email: ')
                address = input('New Address: ')
                account_type = input('New Account Type Savings or Current (sv/cu): ')
                current_user.name = name
                current_user.email = email
                current_user.address = address
                current_user.account_type = account_type
            elif op=='6':
                print('Transaction_history:')
                for transaction in current_user.Transaction_history:
                    print(transaction)
            elif op=='7':
                if current_user.loan_count > 0:
                    loan_amount = float(input('Loan Amount: '))
                    current_user.take_loan(loan_amount)
            elif op=='8':
                recipient_account = int(input('Recipient Account Number: '))
                recipient = User.user_exists(recipient_account)
                if recipient is None:
                    print('Recipient account does not exist.')
                else:
                    transfer_amount = float(input('Amount to Transfer: '))
                    current_user.transfer(recipient, transfer_amount)
            elif op=='9':
                current_user = None
                print('\nLogout Successful\n')
            else:
                print('Invalid option.')
        elif current_user.acc_type == 'cu':
            print('\n1. Show Info')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Change Info')
            print('5. Show Transaction ')
            print('6. Logout')

            op=input('Choose Option: ')

            if op=='1':
                print(f'Name: {current_user.name}')
                print(f'Account Number: {current_user.account_number}')
                print(f'Account Type: {current_user.acc_type}')
                print(f'Balance: {current_user.Balance}')
            elif op=='2':
                amount = float(input('Amount: '))
                current_user.deposit(amount)
            elif op=='3':
                amount = float(input('Amount: '))
                current_user.Withdraw(amount)
            elif op=='4':
                name=input('New Name: ')
                email=input('New Email: ')
                address=input('New Address: ')
                account_type=input('New Account Type Savings or Current (sv/cu) ')
                current_user.name = name
                current_user.email = email
                current_user.address = address
                current_user.acc_type = account_type
            elif op=='5':
                print('Transaction_history:')
                for transaction in current_user.Transaction_history:
                    print(transaction)
            elif op=='6':
                current_user = None
                print('\nLogout Successful\n')
            else:
                print('Invalid option.')






   
        
    

        









    


            
    


    

        
