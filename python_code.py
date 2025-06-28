## started 8:02 pm est 6/27/2025

target = {
    1: 'A',
    2: 'A',
    3: None,
    5: 'A',
    8: 'A',
    9: None,
    10: None
}

source = {
    1: None,
    2: 'B',
    4: 'B',
    8: 'B',
    9: 'B',
    10: None,
    11: None
}

##use for lookup
targetKeys = target.keys()
sourceKeys = source.keys()

print(targetKeys)

## Update function
## the logic is that it replaces the values
## in target from the values in source, 
## does not include if it's not in the target

updated_table = target.copy()
print('update')
def update():
    for i in targetKeys:
        if i in sourceKeys:
            updated_table[i] = source[i]
            continue
update()
print(updated_table)

## Update null fill 
## this logic is similar to the first one
## but in this case, it replaces the value only if
## value is None in the target 

print()
updated_table_null_fill = target.copy()
print('update null fill')
def update_null_fill():
    for i in targetKeys:
        if i in sourceKeys:
            if updated_table_null_fill[i] is None:
                updated_table_null_fill[i] = source[i]
update_null_fill()
print(updated_table_null_fill)

## Update override 
## this updates only if the source value exists and the 
## id exists in the target

updated_override = target.copy()
print('update override')

def update_override():
    for i in targetKeys:
        if i in sourceKeys and source[i] is not None:
            updated_override[i] = source[i]
            continue
update_override()
print(updated_override)

## merge
## this combines the tables, 
## the source takes precedence over target value
##, one value per id 

merge_table = target.copy()
## the merged keys will be useful later too 
mergedKeys = list(set(sourceKeys) | set(targetKeys))

def merge():
    print('merge')

    for i in mergedKeys:
        if i in sourceKeys:
            merge_table[i] = source[i]
            continue
        merge_table[i] = target[i]
merge()
print(merge_table)

## merge_null_fill 
## merge but only replace if the value in the target is 
## None

merge_nf = target.copy()
print('merge null fill')

def merge_null_fill():
    for i in mergedKeys:
        ## both exist case
        if i in sourceKeys and i in targetKeys:
            ## if and only if target val is none, replace
            if merge_nf[i] is None:
                merge_nf[i] = source[i]
        ## otherwise its the source val
        if i in sourceKeys:
            merge_nf[i] = source[i]

            
merge_null_fill()
print(merge_nf)

## merge_override
## most similar to the merge nf function
## only update the value to the associated source value if 
## it is not none

merge_override = target.copy()
print('merge over')
def merge_over():
    for i in mergedKeys:
        ## both exist case
        if i in sourceKeys and i in targetKeys:
            ## if and only if source  val is not none, replace
            if source[i] is None:
                continue
            else:
                merge_override[i] = source[i]
        ## otherwise its the source val, since the logic
        ## means this is just in the sourcekeys
        if i in sourceKeys:
            merge_override[i] = source[i]

merge_over()
print(merge_override)

## append 
## allows for multiple values for the same id

append_tab = {}
print('append')
def append_f():
    for i in mergedKeys:
        ##add for both
        if i in sourceKeys and i in targetKeys:
            arr = [target[i], source[i]]
            append_tab[i] = arr
        ##add for two indiv cases
        if i in sourceKeys:
            append_tab[i] = source[i]
        if i in targetKeys:
            append_tab[i] = target[i]
    
append_f()
print(append_tab)
        

## finished at 9:12 pm 6/27/2025






    
