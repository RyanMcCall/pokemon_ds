import pandas as pd
from acquire import acquire_data

def prepare_data():
    pokemon = acquire_data()

    #Remove unnecessary columns
    pokemon = pokemon.drop(columns=['abilities', 'against_bug', 'against_dark', 'against_dragon',
       'against_electric', 'against_fairy', 'against_fight', 'against_fire',
       'against_flying', 'against_ghost', 'against_grass', 'against_ground',
       'against_ice', 'against_normal', 'against_poison', 'against_psychic',
       'against_rock', 'against_steel', 'against_water', 'classfication', 'japanese_name'])
    
    # Fix a value
    pokemon.at[773, 'capture_rate'] = '30'

    # Fix type of capture rate
    pokemon.capture_rate = pokemon.capture_rate.astype(int)

    return pokemon