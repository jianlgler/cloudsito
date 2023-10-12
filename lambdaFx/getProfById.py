import boto3
import json

dynamodb = boto3.client('dynamodb')

    #Dato un id dammi il professore
def lambda_handler(event, context):

    # ID dell prof che si desidera cercare (passato come parametro nell'evento)
    prof_id = 'SOSTITUISCIMI CON L'id' NEL TOKEN'

    try:
        # Cerca il professore nel database utilizzando l'ID come chiave primaria
        response = dynamodb.get_item(
            TableName='professors',
            Key={
                'id': {'S': prof_id}
            }
        )

        # Estrai i dati del prof dalla risposta
        prof = response.get('Item', None)

        if prof:
            # Il prof è stato trovato, restituisci i dati
            return {
                'statusCode': 200,
                'body': prof
            }
        else:
            # Il prof non è stato trovato
            return {
                'statusCode': 404,
                'body': 'Professor not found'
            }
    except Exception as e:
        # Gestione delle eccezioni
        return {
            'statusCode': 500,
            'body': str(e)
        }
