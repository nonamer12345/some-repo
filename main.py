from pokemon import Pokemon

FILE_PATH = 'data\\pokemon.csv'

if __name__ == "__main__":
    
    poke = Pokemon(file_path=FILE_PATH)
    
    print(f"Pokemon data sample:\n\n{poke.head().to_string()}")
    print()
    