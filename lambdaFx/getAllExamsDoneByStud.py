import boto3
import json

dynamodb = boto3.client('dynamodb')

#Dato un id dammi lo studente
def lambda_handler(event, context):

    # ID dello studente che si desidera cercare (passato come parametro nell'evento)
    stud_id = 'SOSTITUISCIMI CON L'id' NEL TOKEN'

    try:
        # Cerca lo studente nel database utilizzando l'ID come chiave primaria
        response = dynamodb.get_item(
            TableName = 'students',
            Key={
                'id': {'S': stud_id}
            }
        )

        # Estrai i dati dello studente dalla risposta
        student = response.get('Item', None)

        if student:
             
            
            try:
                response = dynamodb.scan(
                    TableName='examresults',
                    FilterExpression='studentId = :stud_id',
                    ExpressionAttributeValues={':stud_id': {'S': stud_id}}
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
            # Lo studente non è stato trovato
            return {
                'statusCode': 404,
                'body': 'No student found'
            }
    except Exception as e:
        # Gestione delle eccezioni
        return {
            'statusCode': 500,
            'body': str(e)
        }
