print("----------莎莎宝贝婴幼儿公司物流运费计费系统----------")
freight = float(input("请输入您的运费（元）:"))

# 运费不打折
if freight < 500:
    print("您当前的运费不打折。")
    act_freight = freight
# 运费9.5折
elif freight >= 500 and freight < 1000:
    print("您当前的运费折扣为9.5折。")
    act_freight = freight * 0.95
# 运费9折
elif freight >= 1000 and freight < 2000:
    print("您当前的运费折扣为9折。")
    act_freight = freight * 0.9
# 运费8折
elif freight >= 2000 and freight < 5000:
    print("您当前的运费折扣为8折。")
    act_freight = freight * 0.8
# 运费7.5折
else:
    print("您当前的运费折扣为7.5折。")
    act_freight = freight * 0.75

# 输出实际付费
print("您实际应付运费（元）:%.2f" % (act_freight))
