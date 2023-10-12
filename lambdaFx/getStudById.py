import boto3
import json

dynamodb = boto3.client('dynamodb')

#Dato un id dammi lo studente
def lambda_handler(event, context):

    # ID dello studente che si desidera cercare (passato come parametro nell'evento)
    student_id = 'SOSTITUISCIMI CON L'id' NEL TOKEN'

    try:
        # Cerca lo studente nel database utilizzando l'ID come chiave primaria
        response = dynamodb.get_item(
            TableName = 'students',
            Key={
                'id': {'S': student_id}
            }
        )

        # Estrai i dati dello studente dalla risposta
        student = response.get('Item', None)

        if student:
            # Lo studente è stato trovato, restituisci i dati
            return {
                'statusCode': 200,
                'body': student
            }
        else:
            # Lo studente non è stato trovato
            return {
                'statusCode': 404,
                'body': 'Studente non trovato'
            }
    except Exception as e:
        # Gestione delle eccezioni
        return {
            'statusCode': 500,
            'body': str(e)
        }
