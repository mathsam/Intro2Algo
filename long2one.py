def long2one(long_num):
    if long_num == 1:
        return 0
    last_bin = long_num & 1
    second_to_last_bin = (long_num & 2) >> 1
    if long_num.bit_length() >= 2 and last_bin == 0 and second_to_last_bin == 0:
        new_num = long_num >> 2
        return 2 + long2one(new_num)
    if last_bin == 0 and second_to_last_bin == 1:
        new_num = long_num >> 1
        return 1 + long2one(new_num)
    if last_bin == 1 and second_to_last_bin == 0:
        new_num = long_num - 1
        return 1 + long2one(new_num)
    if last_bin == 1 and second_to_last_bin == 1:
        if long_num.bit_length() > 2:
            new_num = long_num + 1
            return 1 + long2one(new_num)
        else:
            return 2

print long2one(3L)
print long2one(898693090870980985907068790890658906807806893058L)