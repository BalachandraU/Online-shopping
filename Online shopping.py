price_f=int(input())
discount_f=int(input())
shipping_f=int(input())
price_s=int(input())
discount_s=int(input())
shipping_s=int(input())
price_a=int(input())
discount_a=int(input())
shipping_a=int(input())
price_f=price_f-(price_f* discount_f/100)+shipping_f
price_s=price_s-(price_s* discount_s/100)+shipping_s
price_a=price_a-(price_a* discount_a/100)+shipping_a
print("In Flipkart: Rs.%d"%(int(price_f)))
print("In Snapdeal: Rs.%d"%(int(price_s)))
print("In Amazon: Rs.%d"%(int(price_a)))
if price_f<=price_s and price_f<=price_a:
    print("Choose Flipkart")
elif price_s<=price_f and price_s<=price_a:
    print("Choose Snapdeal")
elif price_a<=price_f and price_a<=price_s:
    print("Choose Amazon")
else:
    print("Choose Flipkart")
