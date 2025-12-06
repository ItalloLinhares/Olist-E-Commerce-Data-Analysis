def validate_orders_items(customers):
    import pandas as pd
    import validations as validations
    registros_invalidos_cutomers = {column: pd.DataFrame() for column in customers.columns}
    #Verifica se a coluna order_id é válida
    registros_invalidos_cutomers['customer_id'] = validations.validar_formato_id_alfanumerico_32(customers, 'customer_id')
    #Verifica se a customer_unique_id é válida
    registros_invalidos_cutomers['customer_unique_id'] = validations.validar_formato_id_alfanumerico_32(customers, 'customer_unique_id')
    #Verifica se a customer_city é válida
    registros_invalidos_cutomers['customer_city'] = validations.validar_formato_cidade(customers, 'customer_city')
    #Verifica se a customer_state é válida
    registros_invalidos_cutomers['customer_state'] = validations.validar_formato_uf(customers, 'customer_state')
    lista_registros_invalidos_customers = list(registros_invalidos_cutomers.values())
    df_registros_invalidos_customers_combinado = pd.concat(lista_registros_invalidos_customers, ignore_index=True)
    dataframe_registros_customers_invalidos = df_registros_invalidos_customers_combinado.drop_duplicates(subset=['customer_unique_id'], keep='first')
    return dataframe_registros_customers_invalidos
     


