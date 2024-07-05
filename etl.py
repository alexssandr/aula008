import pandas as pd
import os
import glob


#leitura de arquivos
def ler_arquivos_json(path: str) -> pd.DataFrame:
    json_files = glob.glob(os.path.join(path,'*.json'))
    df_lista = [pd.read_json(arquivo) for arquivo in json_files]
    df_consolidado = pd.concat(df_lista,ignore_index=True)
    return df_consolidado


def calcular_total_dataframe(df_consolidado: pd.DataFrame) -> pd.DataFrame:
    df_consolidado['Total'] = df_consolidado['Quantidade'] * df_consolidado['Venda']
    return df_consolidado

def exportar_arquivo(df_transformado, tipo: list[str]):
    if 'csv' in tipo:
        df_transformado.to_csv('df_vendas.csv')
    if 'parquet' in tipo:
        df_transformado.to_parquet('df_vendas.parquet')


def pipeline_calcular_kpi(pasta, formato):
    data_frame = ler_arquivos_json(pasta)
    data_frame = calcular_total_dataframe(data_frame)
    exportar_arquivo(data_frame, formato)