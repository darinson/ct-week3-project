import re


class roiCalc():

    def __init__(self):
        print("\nHello, welcome to your return-on-investment (ROI) calculator.\nWe will calculate your cash on cash ROI by collecting some information.")
        print("\nPart 1/4: General Information")
        self.Name = input("What is your property name? ")
        self.PropertyValue = self.checkNum(
            "What is the value of your property? $")

        print("\nPart 2/4: Initial Investment Costs")
        self.Investment = self.cal_investment()

        print("\nPart 3/4: Monthly Income")
        self.Income = self.cal_income()

        print("\nPart 4/4: Monthly Expenses")
        self.Expenses = self.cal_expenses()

        print("\nCalculating monthly cash flow...")
        self.Cashflow = self.cal_cashflow()

        print("\nCalculating cash on cash return on investment...")
        self.ROI = self.cal_roi()
        self.showSummary()

    def cal_income(self):
        self.dict_income = {
            "Rent": 0
        }
        print("Monthly Income = money you earn from the property every month.")
        print("This includes rent from your tenants.")
        other_inputs = input(
            "Are there other sources of income you would like to include? (y/n) ")
        while other_inputs.lower() != "n":
            if other_inputs != "y":
                other_inputs = input(
                    "Are there other sources of income you would like to include? (y/n) ")
            else:
                new_key = input(
                    "What source of income would you like to include? ")
                self.dict_income[new_key] = 0
                other_inputs = input(
                    "Would you like to add another source of income? (y/n) ")

        for key in self.dict_income:
            ask_value = self.checkNum(
                f"Please enter your monthly earnings from {key}: $")
            self.dict_income[key] = ask_value

        askIncome = sum(float(costs) for x, costs in self.dict_income.items())
        return askIncome

    def cal_expenses(self):
        self.dict_expenses = {
            "Property Tax": 0,
            "Insurance": 0,
            "Mortgage": 0,
            "Utilities": 0,
            "HOA Fees": 0,
            "Vacancy": 0
        }
        print("Monthly Expenses = what you pay for the property every month.")
        print("This includes property tax, insurance, mortgage, utility bills, HOA fees, vacancy.")
        other_inputs = input(
            "Are there other types of expenses you would like to include? (y/n) ")
        while other_inputs.lower() != "n":
            if other_inputs != "y":
                other_inputs = input(
                    "Are there other types of expenses you would like to include? (y/n) ")
            else:
                new_key = input(
                    "What type of expense would you like to include? ")
                self.dict_expenses[new_key] = 0
                other_inputs = input(
                    "Would you like to add another type of expense? (y/n) ")

        for key in self.dict_expenses:
            ask_value = self.checkNum(
                f"Please enter your monthly expenses for {key}: $")
            self.dict_expenses[key] = ask_value

        askExpenses = sum(float(costs)
                          for x, costs in self.dict_expenses.items())
        return askExpenses

    def cal_cashflow(self):
        askCashFlow = self.Income - self.Expenses
        print("Your monthly cash flow is ${:.2f}.".format(askCashFlow))
        return askCashFlow

    def cal_investment(self):
        self.dict_inv = {
            "Down Payment": 0,
            "Repairs": 0,
            "Closing Costs": 0
        }
        print("Initial investment costs = what you paid before and when you bought the property.")
        print("This includes down payments, repairs and closing costs.")
        other_inputs = input(
            "Are there other types of investment costs you would like to include? (y/n) ")
        while other_inputs.lower() != "n":
            if other_inputs != "y":
                other_inputs = input(
                    "Are there other types of investment costs you would like to include? (y/n) ")
            else:
                new_key = input(
                    "What type of investment cost would you like to include? ")
                self.dict_inv[new_key] = 0
                other_inputs = input(
                    "Would you like to add another type of investment cost? (y/n) ")

        for key in self.dict_inv:
            ask_value = self.checkNum(f"Please enter the value of {key}: $")
            self.dict_inv[key] = ask_value

        askInvestment = sum(float(costs) for x, costs in self.dict_inv.items())
        return askInvestment

    def cal_roi(self):
        self.AnnualCashflow = 12 * self.Cashflow
        askROI = 100 * self.AnnualCashflow / self.Investment
        print("Your cash on cash ROI is {:.2f}%.".format(askROI))
        self.YearsPayOff = 100/askROI
        return askROI

    def showSummary(self):
        summary = input(
            "\nWould you like a summary of the calculations? (y/n)")
        while summary.lower() != "n":
            if summary.lower() != "y":
                summary = input(
                    "\nWould you like a summary of the calculations? (y/n)")
            else:
                print(
                    "\n==========================Summary of Calculations==========================")
                print("\nPart 1: General Info\nProperty Name: {}\nProperty Value: ${:.2f}".format(
                    self.Name.title(), self.PropertyValue))
                print("\nPart 2: Initial Investment Costs")
                for key, value in self.dict_inv.items():
                    print("{}: ${:.2f}".format(key.title(), value))
                print("\nPart 3: Monthly Income")
                for key, value in self.dict_income.items():
                    print("{}: ${:.2f}".format(key.title(), value))
                print("\nPart 4: Monthly Expenses")
                for key, value in self.dict_expenses.items():
                    print("{}: ${:.2f}".format(key.title(), value))
                print("\n==========================\nEach year, you have a net operating income of ${:.2f} from the property.\nWith your total investment of ${:.2f},\n\tyour cash on cash return on investment is {:.2f}% per year.\nWithout inflation, you will earn your investment back in {:.0f} years.".format(
                    self.AnnualCashflow, self.Investment, self.ROI, self.YearsPayOff))

                summary = "n"

    def checkNum(self, prompt):
        valueNum = input(prompt)
        patNum = re.compile(r"^[\d]+\.*[\d]*")
        while not patNum.search(valueNum):
            valueNum = input("Please enter a numeric value. " + prompt)
        return float(valueNum)


prop1 = roiCalc()
