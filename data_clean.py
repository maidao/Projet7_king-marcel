import pandas as pd
import matplotlib.pyplot as plt

def read_data(path):
    data = pd.read_csv(path, low_memory=False, sep=';')
    return data

def read_info(data):
    print(data.columns)
    print('len of data: ',len(data))
    print('shape of data:', data.shape)
    print(data.info())
    print(data.describe())
    print(data.head(5))

def table_jour(data_jour):
    print("1) This is data_reporting_jour")
    data_jour = data_jour[['frequentation', 'ca_ttc', 'date_commande']]
    data_jour = data_jour.drop(data_jour[(data_jour['frequentation'] == 0.0) & (data_jour['ca_ttc'] == 0.0)].index)
    data_jour['date_commande'] = pd.to_datetime(data_jour['date_commande'])
    data_jour = data_jour.groupby(data_jour['date_commande']).sum()
    data_jour['moyen'] = data_jour['ca_ttc'] / data_jour['frequentation']
    print(read_info(data_jour))
    print(data_jour)

    plt.figure("test")
    plt.bar(data_jour.index[:21], data_jour['frequentation'][:21])
    #plt.savefig('semaine.png', bbox_inches='tight')
    plt.show()

def journee(data_jour):
    data_jour = data_jour[['frequentation', 'ca_ttc', 'jour_semaine']]
    data_jour = data_jour.drop(data_jour[(data_jour['frequentation'] == 0.0) & (data_jour['ca_ttc'] == 0.0)].index)
    data_jour = data_jour.groupby(data_jour['jour_semaine']).sum()
    data_jour['prix_moyen'] = data_jour['ca_ttc'] / data_jour['frequentation']
    print(read_info(data_jour))
    print(data_jour)

    plt.figure("test")
    plt.bar(data_jour.index[:21], data_jour['frequentation'][:21])
    #plt.savefig('journee.png', bbox_inches='tight')
    plt.show()


def midi_soir(data_jour):
    data_jour = data_jour[['frequentation', 'ca_ttc', 'midi_soir']]
    data_jour = data_jour.drop(data_jour[(data_jour['frequentation'] == 0.0) & (data_jour['ca_ttc'] == 0.0)].index)
    data_jour = data_jour.groupby(data_jour['midi_soir']).sum()
    data_jour['prix_moyen'] = data_jour['ca_ttc'] / data_jour['frequentation']
    print(read_info(data_jour))
    print(data_jour)

    plt.figure("test")
    plt.bar(data_jour.index[:21], data_jour['frequentation'][:21])
    #plt.savefig('midi_soir.png', bbox_inches='tight')
    plt.show()