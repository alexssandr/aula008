from etl import pipeline_calcular_kpi

pasta_do_arquivo: str = 'data'
formato: list[str] = ['csv', 'parquet']

pipeline_calcular_kpi(pasta_do_arquivo,formato)
