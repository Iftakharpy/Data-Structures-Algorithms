# file comparison
with open('my_dict_entry.txt','r') as f1, open('real_dict_entry.txt','r') as f2, open('result_entry.txt','w') as result:
    for (line_f1,line_f2) in zip(f1,f2):
        if line_f1==line_f2:
            continue
        result.write(f'{line_f1[:-1]} != {line_f2[:-1]}\n')
print('result_entry.txt is created')

with open('retrived_records_from_my_dict.txt','r') as f1, open('retrived_records_from_real_dict.txt','r') as f2, open('result_retrived.txt','w') as result:
    for (line_f1,line_f2) in zip(f1,f2):
        if line_f1==line_f2:
            continue
        result.write(f'{line_f1[:-1]} != {line_f2[:-1]}\n')
print('result_retrived.txt is created')