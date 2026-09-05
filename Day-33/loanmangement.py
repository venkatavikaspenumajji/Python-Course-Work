class Customer:
    def _init_(self,customer_id,name,age,email,phone,income,credit_score):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.income = income
        self.credit_score = credit_score

    def check_eligibility(self):
        if self.age<21 or self.credit_score<650 or self.income<25000:
            return False
        return True

    def display_customer(self):
        print("\nCustomer details")
        print("-------------------")
        print("Customer ID: ",self.customer_id)
        print("Name: ",self.name)
        print("Phone: ",self.phone)
        print("Age: ",self.age)
        print("Income: ",self.income)
        print("Credit Score: ",self.credit_score)
        @abstractmethod
    def calculate_emi(self):
        pass

    def check_loan_eligibility(self):

        if not self.customer.check_eligibility():
            self.status = "Rejected"
            return False
        return True

    def sanction_loan(self):
        if self.status == "Rejected":
            print("Loan application rejected")
            return
        if not self.check_loan_eligibility():
            print("Customer is not eligible for the loan")
            return

        self.status = "Sanctioned"
        print("\nLoan sactioned successfully")

    def repay(self,amount):
        if self.status == "Sactioned":
            print("Repayment is not allowed")
            print("Loan status",self.status)
            