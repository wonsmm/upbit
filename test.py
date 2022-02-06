import pyupbit

access = "eEaEmaxDDWefCH2LFPxLxqbEvrDQibDqZDOw9mvA"          # 본인 값으로 변경
secret = "iEaHt3GUPTUuJDx4GW6lPp2kMjnK1yaaprcgarSc"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-SAND"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회