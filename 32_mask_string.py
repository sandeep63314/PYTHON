def mask(strng,substr,*args):
    mskstr = ''
    for tup in enumerate(strng):
        idx,ch = tup
        if idx in args:
            mskstr += ch
        else:
            mskstr += substr
    return mskstr

msk = mask('239430899385','*',8,9,10,11)
print(msk)