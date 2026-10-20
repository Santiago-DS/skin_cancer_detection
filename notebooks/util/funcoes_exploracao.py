import polars as pl


def pl_contagem_valores(df, col, excluir_na=False):
    instrucao_calc_percent = (pl.col(f'qtd_{col}') / pl.col(f'qtd_{col}').sum() * 100).round(2)

    if excluir_na:
        intrucao_filtro = ~pl.col(col).is_null()
    else:
        intrucao_filtro = True
    
    df_result = (
        df
            .filter(intrucao_filtro)
            .select(col)
            .group_by(pl.col(col))
            .agg( pl.len().alias(f'qtd_{col}') )
            .with_columns( instrucao_calc_percent.alias(f'percent_{col}') )
    )

    return df_result



def pl_dist_nulos(df, limiar=1):

    qtd_linhas = df.select(pl.len()).collect().item()
    df_nul = (
        df
            .null_count()
            .collect()
            .unpivot(variable_name='variaveis', value_name='qtd_nulos')
            .filter(pl.col('qtd_nulos') >= limiar)
            .sort('qtd_nulos', descending=True)
            .with_columns(percent_nulos = ((pl.col('qtd_nulos') / qtd_linhas)*100).round(2)
            )
    )

    return df_nul