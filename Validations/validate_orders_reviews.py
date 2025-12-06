def validate_orders_reviews(orders_reviews):
    import pandas as pd
    import Validations.validations as validations
    #Cria um dicionario para guardar todas os registros inválidos de cada coluna
    registros_invalidos_orders_reviews = {column: pd.DataFrame() for column in orders_reviews.columns}
    #Verifica se a coluna review_id é válida
    registros_invalidos_orders_reviews['review_id'] = validations.validar_formato_id_alfanumerico_32(orders_reviews, 'review_id')
    #Verifica se a coluna order_id é válida
    registros_invalidos_orders_reviews['order_id'] = validations.validar_formato_id_alfanumerico_32(orders_reviews, 'order_id')
    #Verifica se a coluna review_score é válida
    registros_invalidos_orders_reviews['review_score'] = validations.validar_formato_score(orders_reviews, 'review_score')
    #Verifica se a coluna review_creation_date é válida
    registros_invalidos_orders_reviews['review_creation_date'] = validations.validar_formato_data_hora(orders_reviews, 'review_creation_date')
    #Verifica se a coluna review_answer_timestamp é válida
    registros_invalidos_orders_reviews['review_answer_timestamp'] = validations.validar_formato_data_hora(orders_reviews, 'review_answer_timestamp')
    #Junta todas os dicionarios em um Dataframe e exclui as cópias para termos um Dataframe final com todos os valores inválidos
    lista_registros_invalidos_orders_reviews = list(registros_invalidos_orders_reviews.values())
    df_registros_invalidos_orders_reviews_combinado = pd.concat(lista_registros_invalidos_orders_reviews, ignore_index=True)
    dataframe_registros_orders_reviews_invalidos = df_registros_invalidos_orders_reviews_combinado.drop_duplicates(subset=['review_id'], keep='first')
    return dataframe_registros_orders_reviews_invalidos