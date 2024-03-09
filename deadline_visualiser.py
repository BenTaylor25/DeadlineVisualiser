import matplotlib.pyplot as plt
from datetime import date
from deadlines import deadlines

def main():
    current_date = date.today()

    fig, ax = plt.subplots()

    ax.set_title("Deadlines Visualiser")
    ax.set_xlabel("Timeline")
    ax.set_yticks(range(len(deadlines)))
    ax.set_yticklabels([deadline["label"] for deadline in deadlines])

    for i, deadline in enumerate(deadlines):
        days_remaining = (deadline["deadline"] - current_date).days
        ax.barh(i, days_remaining, left=current_date, color="skyblue", edgecolor="black", height=0.6)
        ax.text(current_date, i, f" {days_remaining} days", va="center", ha="left", fontsize=8)

    plt.show()


if __name__ == "__main__":
    main()
