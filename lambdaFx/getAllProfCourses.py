import boto3
import json

dynamodb = boto3.client('dynamodb')

#Dato un id dammi lo professore
def lambda_handler(event, context):

    # ID dello professore che si desidera cercare (passato come parametro nell'evento)
    prof_id = 'SOSTITUISCIMI CON L'id' NEL TOKEN'

    try:
        # Cerca lo professore nel database utilizzando l'ID come chiave primaria
        response = dynamodb.get_item(
            TableName = 'professors',
            Key={
                'id': {'S': prof_id}
            }
        )

        # Estrai i dati dello professore dalla risposta
        professor = response.get('Item', None)

        if professor:
             
            
            try:
                response = dynamodb.scan(
                    TableName='courses',
                    FilterExpression='profId = :prof_id',
                    ExpressionAttributeValues={':prof_id': {'S': prof_id}}
                )
                items = response.get('Items', [])
    
                # Esegui ulteriori operazioni sui dati estratti, se necessario
                for item in items:
                    # Esempio: Stampa gli elementi trovati
                    print(item)
                return items
            except Exception as e:
                print("Error accessing the 'courses' table:", str(e))

    
        else:
            # Lo professore non è stato trovato
            return {
                'statusCode': 404,
                'body': 'No professor found'
            }
    except Exception as e:
        # Gestione delle eccezioni
        return {
            'statusCode': 500,
            'body': str(e)
        }
