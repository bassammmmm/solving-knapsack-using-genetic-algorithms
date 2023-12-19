from utils import *
import tkinter as tk

def run_algorithm():
    try:

        max_weight = int(max_weight_entry.get())
        values = list(map(int, values_entry.get().split()))
        weights = list(map(int, weights_entry.get().split()))
        best_solution_01, best_value_01 = genetic_algorithm(values, weights, max_weight, unbounded=False)
        best_solution_unbounded, best_value_unbounded = genetic_algorithm(values, weights, max_weight, unbounded=True)

        best_solution_01_label.config(text="Best Solution For 0-1 Knapsack: " + str(best_solution_01))
        best_value_01_label.config(text="Best Value For 0-1 Knapsack: " + str(best_value_01))
        best_solution_unbounded_label.config(text="Best Solution For Unbounded Knapsack: " + str(best_solution_unbounded))
        best_value_unbounded_label.config(text="Best Value For Unbounded Knapsack: " + str(best_value_unbounded))
    except ValueError:
        error_label.config(text="Please enter valid input (values and weights should be integers)")

root = tk.Tk()
root.title("Knapsack Problem Solver")

values_label = tk.Label(root, text="Enter values (Seperate them by space):")
values_label.grid(row=0, column=0)
values_entry = tk.Entry(root)
values_entry.grid(row=0, column=1)

weights_label = tk.Label(root, text="Enter weights (Seperate them by space):")
weights_label.grid(row=1, column=0)
weights_entry = tk.Entry(root)
weights_entry.grid(row=1, column=1)

max_weight_label = tk.Label(root, text="Enter knapsack max weight:")
max_weight_label.grid(row=2, column=0)
max_weight_entry = tk.Entry(root)
max_weight_entry.grid(row=2, column=1)

run_button = tk.Button(root, text="Run Algorithm", command=run_algorithm)
run_button.grid(row=3, columnspan=2)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=4, columnspan=2)

best_solution_01_label = tk.Label(root, text="")
best_solution_01_label.grid(row=5, columnspan=2)

best_value_01_label = tk.Label(root, text="")
best_value_01_label.grid(row=6, columnspan=2)

best_solution_unbounded_label = tk.Label(root, text="")
best_solution_unbounded_label.grid(row=7, columnspan=2)

best_value_unbounded_label = tk.Label(root, text="")
best_value_unbounded_label.grid(row=8, columnspan=2)


root.mainloop()