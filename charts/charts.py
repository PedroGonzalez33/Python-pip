import matplotlib.pyplot as plt

def generte_pie_chart():
    labels = ['A', 'B', 'C']
    values = [100, 200, 300]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("piechart.png")
    plt.close