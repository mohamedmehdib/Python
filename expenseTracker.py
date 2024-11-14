from datetime import datetime
import json
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        pass

    def addExpense(self):
        with open(PATH, "r") as file:
            data = json.load(file)
        
        descs = []
        for i in range(len(data)):
            descs.append(data[i]["desc"])
        descs = list(set(descs))
        
        while True:
            date = input('Enter the day (YY-MM-DD): ')
            if self.is_valid_date(date):
                break
        
        if descs:
            print("Previous descriptions: ", end="")
            for desc in descs:
                print(desc, end=", ")
            print() 
        
        desc = input('Enter description: ')
        amount = int(input('Enter amount (DT): '))
        month = datetime.strptime(date, '%y-%m-%d').strftime("%B")

        data.append({
            "desc": desc,
            "amount": amount,
            "month": month
        })
        with open(PATH, "w") as file:
            json.dump(data, file, indent=4)

    def viewExpensesStat(self):
        while True:
            choice = int(input("What do you want? \n1. View statistics of all available months\n2. View statistics of a specific month: "))
            if choice in [1, 2]:
                break
        
        with open(PATH, "r") as file:
            data = json.load(file)
        
        if choice == 1:
            months = []
            for i in range(len(data)):
                months.append(data[i]["month"])
            months = list(set(months))
            
            amounts = [0] * len(months)
            for i in range(len(months)):
                for j in range(len(data)):
                    if data[j]["month"] == months[i]:
                        amounts[i] += data[j]["amount"]
            

            
            fig, ax = plt.subplots()
            bars = ax.bar(months, amounts, color='blue')

            # Enhance the bar chart
            ax.set_title('Expenses by Month')
            ax.set_xlabel('Months')
            ax.set_ylabel('Amount (DT)')
            ax.set_ylim(0, max(amounts) + 10)

            for bar in bars:
                height = bar.get_height()
                if height > 20:
                    ax.text(bar.get_x() + bar.get_width() / 2, height - 10, f'{height} DT', ha='center', va='center', color='white', fontsize=12)
                else:
                    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height} DT', ha='center', va='bottom', color='black', fontsize=12)
            
                     
            plt.show()
        
        elif choice == 2:
            month = input("Which month do you want ? : ").capitalize()
            data = [x for x in data if x["month"]==month]
                
            descs = []
            for i in range(len(data)):
                descs.append(data[i]["desc"])
            descs = list(set(descs))
            
            amounts = [0] * len(descs)
            for i in range(len(descs)):
                for j in range(len(data)):
                    if data[j]["desc"] == descs[i]:
                        amounts[i] += data[j]["amount"]
            
            colors = ['red', 'orange', 'blue', 'green'] * (len(descs) // 4 + 1)
            total = sum(amounts)


            # Custom autopct function
            def make_autopct(values):
                def my_autopct(pct):
                    total = sum(values)
                    val = int(round(pct*total/100.0))
                    return f'{val} DT'
                return my_autopct

            plt.pie(
                amounts, labels=descs,
                colors=colors[:len(descs)], startangle=140,
                autopct=make_autopct(amounts),
                wedgeprops={'edgecolor': 'black', 'linewidth': 1}
            )
            
            plt.title(f"{month}\nTotal: {total} DT")
            plt.axis('equal')
            plt.show()

    def is_valid_date(self, date):
        try:
            datetime.strptime(date, '%y-%m-%d')
            return True
        except ValueError:
            return False

PATH = "expenseTracker/expenseTracker.json"
tracker = ExpenseTracker()

while True:
    choice = int(input("Enter your choice (1. for adding expense | 2. for viewing expenses stat ) : "))
    if choice in [1,2] :
        break

match choice :
    case 1 :
        tracker.addExpense()

    case _ :
        tracker.viewExpensesStat()
