import pandas as pd 
dict = {
    "Name" : ["Prince","Akash","Saurabh","Abhishek"],
    "Marks" : [92,45,63,42],
    "City" : ["Noida","Azamgarh","Greater Noida","Bihar"]
}
df = pd.DataFrame(dict)
print(df)
# df.to_csv('friends.csv')
df.to_csv('friends.csv',index=False) # If opened already then returns error
print(df.head(2)) # first two rows
print(df.tail(2)) # last two rows

print(df.describe())

train = pd.read_csv('train.csv')
print(train)

print(train['Speed']) # Gives speed column

train['Speed'][2] = 50 # Speed changed for that particular train at row 2nd

print(train)

train.to_csv('train.csv',index=False)

train.index = ['first','second','third','fourth']

print(train)