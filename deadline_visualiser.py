import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
from deadlines import deadlines

def main():
    current_date = date.today()

    fig, ax = plt.subplots()

    ax.set_title("Deadlines Visualiser")
    ax.set_xlabel("Timeline")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
    ax.set_yticks(range(len(deadlines)))
    ax.set_yticklabels([deadline["label"] for deadline in deadlines])

    for i, deadline in enumerate(deadlines):
        days_remaining = (deadline["deadline"] - current_date).days

        # Horizontal bar.
        ax.barh(
            y=i,
            width=days_remaining,
            left=current_date,
            color="skyblue",
            edgecolor="black",
            height=0.6
        )

        # Text inside the bar.
        ax.text(
            x=current_date,
            y=i,
            s=f" {days_remaining} day{'s' if days_remaining != 1 else ''}",
            va="center",
            ha="left",
            fontsize=8
        )

    plt.show()


if __name__ == "__main__":
    main()
