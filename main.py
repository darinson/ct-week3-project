class roiCalc():

    def __init__(self):
        print("\nHello, welcome to your return-on-investment (ROI) calculator.\nWe will calculate your cash on cash ROI by collecting some information.")
        print("\nPart 1/4: General Information")
        self.Name = input("What is your property name? ")
        # property taxes use assessed value
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

    def cal_income(self):
        dict_income = {
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
                dict_income[new_key] = 0
                other_inputs = input(
                    "Would you like to add another source of income? (y/n) ")

        for key in dict_income:
            ask_value = self.checkNum(
                f"Please enter your monthly earnings from {key}: $")
            dict_income[key] = ask_value

        askIncome = sum(float(costs) for x, costs in dict_income.items())
        return askIncome

    def cal_expenses(self):
        dict_expenses = {
            "Property Tax Rate": 0,
            "Insurance Rate": 0,
            "Utilities": 0,
            "HOA Fees": 0,
            "Vacancy": 0
        }
        print("Monthly Expenses = what you pay for the property every month.")
        print("This includes property tax, insurance, utility bills, HOA fees, vacancy.")
        other_inputs = input(
            "Are there other types of expenses you would like to include? (y/n) ")
        while other_inputs.lower() != "n":
            if other_inputs != "y":
                other_inputs = input(
                    "Are there other types of expenses you would like to include? (y/n) ")
            else:
                new_key = input(
                    "What type of expense would you like to include? ")
                dict_expenses[new_key] = 0
                other_inputs = input(
                    "Would you like to add another type of expense? (y/n) ")

        for key in dict_expenses:
            if "rate" in key.lower():
                ask_value = self.checkNum(
                    f"Please enter the monthly {key}:" + "%")
                ask_value *= self.PropertyValue
            else:
                ask_value = self.checkNum(
                    f"Please enter your monthly earnings from {key}: $")
            dict_expenses[key] = ask_value

        askExpenses = sum(float(costs) for x, costs in dict_expenses.items())
        return askExpenses

    def cal_cashflow(self):
        askCashFlow = self.Income - self.Expenses
        print("Your monthly cash flow is ${}.".format(str(askCashFlow)))
        return askCashFlow

    def cal_investment(self):
        dict_inv = {
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
                dict_inv[new_key] = 0
                other_inputs = input(
                    "Would you like to add another type of investment cost? (y/n) ")

        for key in dict_inv:
            ask_value = self.checkNum(f"Please enter the value of {key}: $")
            dict_inv[key] = ask_value

        askInvestment = sum(float(costs) for x, costs in dict_inv.items())
        return askInvestment

    def cal_roi(self):
        annual_cashflow = 12 * self.Cashflow
        askROI = 100 * annual_cashflow / self.Investment
        print("Your cash on cash ROI is {:.2f}%.".format(askROI))
        summary = input(
            "\nWould you like a summary of the calculations? (y/n)")
        while summary.lower() != "n":
            summary = "n"
            if summary.lower() != "y":
                summary = input(
                    "\nWould you like a summary of the calculations? (y/n)")
            else:
                self.showSummary()
        return askROI

    def showSummary(self):
        print("Summary of Calculations\n")
        print("Part 1: General Info\nProperty Name: {}\nProperty Value: ${}\n".format(
            self.Name.title(), self.PropertyValue))
        print("Part 2: Initial Investment Costs\n")
        print("Part 3: Monthly Income\n")
        print("Part 4: Monthly Expenses\n")
        print("==========================\nMonthly Cash Flow = ${:.2f}\nCash on Cash Return on Investment = {:.2f}%".format(
            self.Cashflow, self.ROI))

    def checkNum(self, prompt):
        valueNum = input(prompt)
        while not valueNum.isdigit():  # not working for decimal points?? ... consider using regex
            valueNum = input("Please enter a numeric value. " + prompt)
        return float(valueNum)


prop1 = roiCalc()
print(prop1.PropertyValue)
