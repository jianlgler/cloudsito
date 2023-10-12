import json
import boto3

dynamodb = boto3.client('dynamodb')
examresults_table = 'examresults'  

def lambda_handler(event, context):
    # Estrai i dati di input dal payload JSON
    #body = json.loads(event['body'])
    courseId = 'GESTISCI' #body.get('courseId')
    studentId = 'GESTISCI' #body.get('studentId')
    #NON METTERE APICI IN MARK
    mark = GESTISCI #int(body.get('mark'))
    profId = 'GESTISCI' #body.get('profId')

    mark_str = str(mark)

    # Cerca l'entità nella tabella "examresults" in base ai parametri forniti
    response = dynamodb.scan(
        TableName=examresults_table,
        FilterExpression='courseId = :courseId AND studentId = :studentId AND mark = :mark AND profId = :profId',
        ExpressionAttributeValues={
            ':courseId': {'S': courseId},
            ':studentId': {'S': studentId},
            ':mark': {'N': mark_str},
            ':profId': {'S': profId}
        }
    )

    # Verifica se è stata trovata un'entità corrispondente
    if response.get('Items'):
        # Elimina l'entità trovata
        item = response['Items'][0]
        idER = item['idER']['S']
        try:
            dynamodb.delete_item(
                TableName=examresults_table,
                Key={'idER': {'S': idER}}
            )
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Result deleted successfully'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error deleting the result: ' + str(e)})
            }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'No matching result found'})
        }
