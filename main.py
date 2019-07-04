from data_clean import *
import matplotlib.pyplot as plt

data_jour = read_data("/home/dao/projet/Projet7_king-marcel/Dvore_data/reporting_jour.csv")
data_produits = read_data("/home/dao/projet/Projet7_king-marcel/Dvore_data/reporting_produits.csv")
data_meteo = read_data("/home/dao/projet/Projet7_king-marcel/Dvore_data/meteo.csv")
data_promotions = read_data("/home/dao/projet/Projet7_king-marcel/Dvore_data/promotions.csv")
data_vacances = read_data("/home/dao/projet/Projet7_king-marcel/Dvore_data/vacances.csv")


#print(data_jour[(data_jour['frequentation'] <= 0) & (data_jour['ca_ttc'] != 0)])

"""
print("--------------------------------------")
print("1) This is data_reporting_jour")
print(read_info(data_jour))

print("--------------------------------------")
print("2) This is data_reporting_produits")
print(read_info(data_produits))
data_produits = data_produits[['quantite','ca_item_ttc', 'produit','date_commande']]
print(data_produits[(data_produits['quantite'] <= 0) | (data_produits['ca_item_ttc'] < 0)])

print("--------------------------------------")
print("3) This is data_meteo")
print(read_info(data_meteo))

print("--------------------------------------")
print("4) This is data_promotions")
print(read_info(data_promotions))

print("--------------------------------------")
print("5) This is data_vacances")
print(read_info(data_vacances))
"""

table_jour(data_jour)
journee(data_jour)
midi_soir(data_jour)



