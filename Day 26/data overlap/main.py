import pandas

file_path1= './Day 26/data overlap/file1.txt'
file_path2 = './Day 26/data overlap/file2.txt'

# list_1=[]
# list_2= []

# data1= pandas.read_csv(file_path1, names=['elements1'], sep='\t')
# data1= pandas.read_csv(file_path2, names=['elements2'], sep='\t')

# elements1= data1['elements1'].tolist()

with open(file_path1) as file1:
    file_1_data = file1.readlines()

with open(file_path2) as file2:
    file_2_data = file2.readlines()
    # print(file_2_data)
results =[int(num)  for num in file_1_data if num in file_2_data  ]
print(results)