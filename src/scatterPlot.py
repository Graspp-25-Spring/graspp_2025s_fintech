import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to create a scatter plot with OLS regression line
# This function allows the user to select x and y columns from a dataset
# Parameters:
# - fileName: The path to the CSV file containing the dataset (default is 'Data/processed/merged_5.csv')
# Returns:
# - None: Displays the scatter plot and saves it as a PNG file


def scatterPlot(fileName='Data/processed/merged_5.csv'):
    # df = sns.load_dataset(fileName)  # Load dataset using seaborn
    df = pd.read_csv(fileName)

    # Check if the dataset is loaded correctly
    if df.empty:
        print(f"Dataset '{fileName}' is empty or not found.")
        return

    # Keep only columns with numeric (continuous) data
    df = df.select_dtypes(include=['number'])

    # Display the columns in the DataFrame
    i = 0
    for col in df.columns:
        i += 1
        print(f"Column({i}): {col}")

    # wait for user input to select x and y columns
    while True:
        userChoice = input(
            "select your x and y by column number from the above list, separated by a comma (e.g., '12, 8'): ")
        try:
            x_col, y_col = map(int, userChoice.split(','))
            if x_col < 1 or y_col < 1 or x_col > len(df.columns) or y_col > len(df.columns):
                print(
                    "Invalid input. Please enter two valid column numbers separated by a comma.")
            else:
                print(
                    f"You selected column({x_col}) for X and column({y_col}) for Y.")
                x_var = df.columns[x_col - 1]
                y_var = df.columns[y_col - 1]
                print(f"X:{x_var}")
                print(f"Y:{y_var}")
                break
        except ValueError:
            print("Invalid input. Please enter two column numbers separated by a comma.")
            continue

    # Create a scatter plot with OLS regression line
    sns.regplot(data=df, x=x_var, y=y_var)

    # Set the x and y labels and title
    plt.xlabel(x_var, wrap=True)
    plt.ylabel(y_var, wrap=True)
    plt.title(f"Scatter plot for {x_var} vs {y_var}", wrap=True)

    # adjust the layout to fit labels
    plt.tight_layout()

    # Save as PNG with high resolution
    fileName = f"scatter_{x_var}_{y_var}.png"
    # Ensure the file name is valid by removing path and extension
    fileName = fileName.replace('/', '&').replace('\\', '&')
    plt.savefig("graph/" + fileName, dpi=300)
    plt.show()


# Example usage
scatterPlot()
