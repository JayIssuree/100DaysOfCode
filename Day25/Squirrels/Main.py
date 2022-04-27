import pandas

data = pandas.read_csv("Squirrel_Data.csv")
counts = data["Primary Fur Color"].value_counts()
pandas.DataFrame(counts).to_csv("primay_fur_counts.csv")