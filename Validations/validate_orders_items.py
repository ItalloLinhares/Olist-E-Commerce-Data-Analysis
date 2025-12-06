def validate_orders_items(order_items):
    import pandas as pd
    import Validations.validations as validations
    #Cria um dicionario para guardar todas os registros inválidos de cada coluna
    registros_invalidos_order_items = {column: pd.DataFrame() for column in order_items.columns}
    #Verifica se a coluna order_id é válida
    registros_invalidos_order_items['order_id'] = validations.validar_formato_id_alfanumerico_32(order_items, 'order_id')
    #Verifica se a coluna product_id é válida
    registros_invalidos_order_items['product_id'] = validations.validar_formato_id_alfanumerico_32(order_items, 'product_id')
    #Verifica se a coluna seller_id é válida
    registros_invalidos_order_items['seller_id'] = validations.validar_formato_id_alfanumerico_32(order_items, 'seller_id')
    #Verifica se a coluna shipping_limit_date é válida
    registros_invalidos_order_items['shipping_limit_date'] = validations.validar_formato_data_hora(order_items, 'shipping_limit_date')
    #Verifica se a coluna price é válida
    registros_invalidos_order_items['price'] = validations.validar_formato_monetario(order_items, 'price')
    #Verifica se a coluna freight_value é válida
    registros_invalidos_order_items['freight_value'] = validations.validar_formato_monetario(order_items, 'freight_value')
    lista_registros_invalidos_order_items = list(registros_invalidos_order_items.values())
    df_registros_invalidos_order_items_combinado = pd.concat(lista_registros_invalidos_order_items, ignore_index=True)
    dataframe_registros_order_items_invalidos = df_registros_invalidos_order_items_combinado.drop_duplicates(subset=['order_id'], keep='first')
    return dataframe_registros_order_items_invalidos