def coin_change(v,items):
    ans = 99
    if v <= 0:
        return 0;
    for item in items:
        if v - item >= 0:
            update = 1 + coin_change(v - item, items)
            ans = min(ans, update);
    return ans;
    
print(coin_change(4, [1,2,3,5]))