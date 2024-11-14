import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class ExpenseTracker:
    def __init__(self, path):
        self.path = path

    def analysis(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        
        # Extract data
        names = [entry["name"] for entry in data]
        ages = [entry["age"] for entry in data]
        genders = [entry["gender"] for entry in data]
        cities = [entry["city"] for entry in data]
        degrees = [entry["degree"] for entry in data]

        # __________________ AGES __________________
        unique_ages = list(set(ages))
        numAges = [ages.count(age) for age in unique_ages]
        age_labels = [f'{age} years old' for age in unique_ages]
        
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return f'{val} Students'
            return my_autopct

        # Create age pie chart
        fig1, ax1 = plt.subplots()
        ax1.pie(numAges, labels=age_labels, colors=['red', 'orange', 'blue', 'green', 'purple'][:len(unique_ages)],
                startangle=140, autopct=make_autopct(numAges), wedgeprops={'edgecolor': 'black', 'linewidth': 1})
        ax1.set_title('Number of Students at Each Age')
        ax1.axis('equal')

        # _________________ CITIES ___________________
        unique_cities = list(set(cities))
        numCity = [cities.count(city) for city in unique_cities]
        
        # Create city pie chart
        fig2, ax2 = plt.subplots()
        ax2.pie(numCity, labels=unique_cities, colors=['red', 'orange', 'blue', 'green', 'purple'][:len(unique_cities)],
                startangle=140, autopct=make_autopct(numCity), wedgeprops={'edgecolor': 'black', 'linewidth': 1})
        ax2.set_title('Number of Students by City')
        ax2.axis('equal')

        # _________________ DEGREES __________________
        degree_ranges = {"0-5": 0, "6-10": 0, "11-15": 0, "16+": 0}
        for degree in degrees:
            if degree <= 5:
                degree_ranges["0-5"] += 1
            elif degree <= 10:
                degree_ranges["6-10"] += 1
            elif degree <= 15:
                degree_ranges["11-15"] += 1
            else:
                degree_ranges["16+"] += 1
        
        filtered_ranges = {key: value for key, value in degree_ranges.items() if value > 0}
        labels = list(filtered_ranges.keys())
        values = list(filtered_ranges.values())

        # Create degree pie chart
        fig3, ax3 = plt.subplots()
        ax3.pie(values, labels=labels, colors=['red', 'orange', 'blue', 'green'][:len(labels)],
                startangle=140, autopct=make_autopct(values), wedgeprops={'edgecolor': 'black', 'linewidth': 1})
        ax3.set_title('Number of Students in Each Degree Range')
        ax3.axis('equal')

        # Save all plots to a single PDF
        with PdfPages('students_analysis.pdf') as pdf:
            pdf.savefig(fig1)
            pdf.savefig(fig2)
            pdf.savefig(fig3)
        
        plt.show()

# Usage
PATH = "studentsManagement/cityStudent.json"

tracker = ExpenseTracker(PATH)
tracker.analysis()
