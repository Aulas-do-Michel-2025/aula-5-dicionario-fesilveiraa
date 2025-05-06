genes = {
    "BRCA1": 81188,
    "TP53": 19054,
    "EGFR": 192612,
    "APOE": 3597,
    "CFTR": 250000,
    "HBB": 1606,
    "F8": 186000,
    "DMD": 2400000,
    "HTT": 169451,
    "FMR1": 38000,
} 

nome_gene = input ("Digite o nome do gene:  ")

if nome_gene in genes:
    print (f"O tamanho gene {nome_gene} é {genes [nome_gene]}")
else:
    print ("Gene não encontrado.") 
