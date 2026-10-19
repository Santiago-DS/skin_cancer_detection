import polars as pl


def pl_value_counts(df, colum, drop_na=False):
    instrucao_calc_percent = (pl.col(f'qtd_{colum}') / pl.col(f'qtd_{colum}').sum() * 100).round(2)

    if drop_na:
        intrucao_filtro = ~pl.col(colum).is_null()
    else:
        intrucao_filtro = True
    
    df_result = (
        df
            .filter(intrucao_filtro)
            .select(colum)
            .group_by(pl.col(colum))
            .agg( pl.len().alias(f'qtd_{colum}') )
            .with_columns( instrucao_calc_percent.alias(f'percent_{colum}') )
    )

    return df_result