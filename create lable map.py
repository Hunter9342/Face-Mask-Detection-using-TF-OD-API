lables =[{'name':'with_mask','id':1},{'name':'without_mask','id':2},{'name':'mask_weared_incorrect','id':3}]

with open('data\label_map.pbtxt','w') as f:
    for label in lables:
        f.write('item{\n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n') 
        