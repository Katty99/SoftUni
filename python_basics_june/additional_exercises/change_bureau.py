number_of_bitcoins = int(input())
number_of_yuan = float(input())
commission = float(input())

bitcoin_to_lv = 1168
total_bitcoin_in_lv = bitcoin_to_lv * number_of_bitcoins
yuan_to_usd = 0.15
usd_to_lv = 1.76
yuan_to_lv = number_of_yuan * yuan_to_usd * usd_to_lv
eur_to_lv = 1.95
lv_to_eur = 1 / eur_to_lv
total_currencies_to_eur = (total_bitcoin_in_lv + yuan_to_lv) * lv_to_eur
commission_total = total_currencies_to_eur * commission / 100
total_sum = total_currencies_to_eur - commission_total
print(f'{total_sum:.2f}')