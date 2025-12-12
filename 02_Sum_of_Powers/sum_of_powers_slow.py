def slow_solver(a, N):
    # نبدأ المجموع من الصفر
    total = 0

    # نكرر من i = 1 إلى N (شامل)
    for i in range(1, N + 1):

        # إذا كان الرقم فردي → نضيف a^i
        if i % 2 != 0:
            total += a**i
        
        # إذا كان الرقم زوجي → نطرح a^i
        else:
            total -= a**i

    # نرجّع الناتج النهائي
    return total


# عدد الحدود في التسلسل
N = 10000

# قيمة a
a = 2

# استدعاء الدالة لحساب التسلسل بالطريقة البطيئة
slow = slow_solver(a, N)

# طباعة الناتج
print(slow)
