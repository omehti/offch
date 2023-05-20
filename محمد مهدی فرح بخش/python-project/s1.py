def merge_lists(list1, list2):
    merged_list = []
    length = min(len(list1), len(list2))  # بررسی طول کوتاه‌ترین لیست

    for i in range(length):
        merged_list.append(list1[i])
        merged_list.append(list2[i])

    # اضافه کردن عناصر باقی‌مانده از لیست‌ها بزرگتر
    if len(list1) > length:
        merged_list.extend(list1[length:])
    elif len(list2) > length:
        merged_list.extend(list2[length:])

    return merged_list


# مثال استفاده
list1 = input((" enter list 1 (Example : 123  output : [1,2,3]): "))#عدد ۱۲۳ را اینجا
list2 = list(input(" enter list 2 : (Example : 123  output : [1,2,3])"))#عدد ۴۵۶ را اینجا 
#در صورتی که اعداد طبق کامنت بالا داده شود خروجی  می شود : 1,4,2,5,3,6
result = merge_lists(list1, list2)
print(result)