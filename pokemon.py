import pandas as pd


class Pokemon(pd.DataFrame):
    
    def __init__(self, file_path: str):

        try:
            df = pd.read_csv(filepath_or_buffer=file_path)
            super().__init__(df)
        except FileNotFoundError as e:
            print(f"File not found")
            super().__init__(pd.DataFrame())
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            super().__init__(pd.DataFrame())
        
        
    def search_by_types(self, type_column: str, *args):
        types_set = set([type_.lower().strip() for type_ in args])
        foo = pd.DataFrame({col: pd.Series(dtype=dtype) for col, dtype in zip(self.columns.to_list(), self.dtypes.to_list())})
        
        for _, row in self.iterrows():
            row_type = set([row[type_column].lower().strip()])
            if types_set.issuperset(row_type):
                foo.loc[foo.shape[0]] = row
                
        return foo
        