class roiCalc():

    def __init__(self):
        print("Hello, welcome to your return-on-investment (ROI) calculator.\nWe will calculate your cash on cash ROI by collecting some information.")
        print("Part 1/4: General Information")
        self.Name = input("What is your property name? ")
        # property taxes use assessed value
        self.PropertyValue = input("What is the value of your property? ")

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
            "rent": 0,
            "laundry": 0,
            "storage": 0,
            "parking": 0,
            "pet-rent": 0,
            "miscellaneous": 0
        }
        dict_income["rent"] = input("How much rent do you collect each month?")
        dict_income["laundry"] = input(
            "How much laundry fees do you collect each month?")
        dict_income["storage"] = input(
            "How much storage fess do you collect each month?")
        dict_income["parking"] = input(
            "How much parking fees do you collect each month?")
        dict_income["pet-rent"] = input(
            "How much pet-rent do you collect each month?")
        dict_income["miscellaneous"] = input(
            "How much miscellaneous fees do you collect each month?")
        askIncome = sum(int(costs) for x, costs in dict_income.items())
        return askIncome

    def cal_expenses(self):
        dict_expenses = {
            "tax": 0,
            "insurance": 0,
            "utilities": 0,
            "HOA": 0,
            "vacancy": 0,
            "miscellaneous": 0
        }
        dict_expenses["tax"] = input(
            "What is the tax rate for your property in %? (Applied to home value)")
        dict_expenses["insurance"] = input(
            "How much do you pay per month for insurance? ")
        dict_expenses["utilities"] = input(
            "How much do you pay per month for utilities? ")
        dict_expenses["HOA"] = input(
            "How much do you pay per month for HOA fees? ")
        dict_expenses["vacancy"] = input(
            "How much do you save aside per month for vacancy?")
        dict_expenses["miscellaneous"] = input(
            "What other monthly costs are there? ")
        askExpenses = sum(int(costs) for x, costs in dict_expenses.items())
        return askExpenses

    def cal_cashflow(self):
        askCashFlow = self.Income - self.Expenses
        print("Your monthly cash flow is {}".format(str(askCashFlow)))
        return askCashFlow

    def cal_investment(self):
        dict_inv = {
            "advancepayment": 0,
            "closingcost": 0,
            "repairs": 0,
            "miscellaneous": 0
        }
        dict_inv["advancepayment"] = input(
            "How much did you pay for in advance? (i.e. downpayment) ")
        dict_inv["closingcost"] = input("What are your closing costs? ")
        dict_inv["repairs"] = input(
            "How much did you spend on repairing the house when you first bought it? ")
        dict_inv["miscellaneous"] = input(
            "What other costs were there when you initially bought the house? ")
        askInvestment = sum(int(costs) for x, costs in dict_inv.items())
        return askInvestment

    def cal_roi(self):
        annual_cashflow = 12 * self.Cashflow
        askROI = 100 * annual_cashflow / self.Investment
        print("Your cash on cash ROI is {}%.".format(str(askROI)))
        return askROI


prop1 = roiCalc()
