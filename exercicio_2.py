variantes = [
    {"id": "rs789", "frequencia": 0.07},
    {"id": "rs101112", "frequencia": 0.03},
    {"id": "rs131415", "frequencia": 0.0005},
    {"id": "rs161718", "frequencia": 0.05},
    {"id": "rs192021", "frequencia": 0.09},
    {"id": "rs222324", "frequencia": 0.012},
    {"id": "rs252627", "frequencia": 0.0001},
    {"id": "rs282930", "frequencia": 0.06},
] 

print ("As variantes raras são: ")

for variante_rara in variantes:
    if variante_rara ["frequencia"] < 0.01:
        print (variante_rara ["id"])
