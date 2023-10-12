import boto3
import json

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Estrai i dati di input dal payload JSON
    #body = json.loads(event['body'])
    name = 'GESTISCI INPUT NOME BACKEND'
    surname = 'GESTISCI INPUT COGNOME BACKEND'

    # Verifica se name e surname sono stati forniti
    if not name or not surname:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Name and surname are mandatory'})
        }

    # Genera un nuovo ID univoco (puoi usarlo in base alle tue esigenze)
    new_id = str(abs(hash(name + surname)))

    # Crea un nuovo elemento nella tabella "students"
    try:
        response = dynamodb.put_item(
            TableName='students',
            Item={
                'id': {'S': new_id},
                'name': {'S': name},
                'surname': {'S': surname}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Student added successfully.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Errore durante l\'inserimento nell\'entità: ' + str(e)})
        }
