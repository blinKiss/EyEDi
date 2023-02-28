import pandas as pd

data = {
    'id' : [1000,2000,3000,4000],
    'name' : ['dev','mng','sale','plan'],
    'location' : [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# csv 저장하려면
df.to_csv('./data/test_save.csv', index=False)

print(df)