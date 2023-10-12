import boto3
import json

dynamodb = boto3.client('dynamodb')
students_table = 'students'
professors_table = 'professors'
courses_table = 'courses'
examresults_table = 'examresults'

def lambda_handler(event, context):
    # Estrai i dati di input dal payload JSON
    #body = json.loads(event['body'])
    examName = #body.get('examName')
    courseId = #body.get('CourseId')
    studentId = #body.get('studentId')
    #ATTENZIONE A INT
    mark = #int(body.get('mark'))
    date = #body.get('date')
    nameStud = #body.get('nameStud')
    surnStud = #body.get('surnStud')
    profId = #body.get('profId')

    # Controllo che studentId sia presente nella tabella "students"
    if not check_existence(students_table, 'id', studentId):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'studentId not found in students table'})
        }

    # Controllo che mark sia compreso tra 18 e 30
    if not (18 <= mark <= 30):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'mark should be between 18 and 30'})
        }

    # Controllo che profId sia presente nella tabella "professors"
    if not check_existence(professors_table, 'id', profId):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'profId not found in professors table'})
        }

    # Controllo che courseId sia presente nella tabella "courses"
    if not check_existence(courses_table, 'courseId', courseId):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'CourseId not found in courses table'})
        }

    # Genera un nuovo ID univoco per la tabella "examresults"
    new_id = str(abs(hash(examName + courseId + studentId + str(mark) + date + nameStud + surnStud + profId)))

    # Inserisci una nuova entità nella tabella "examresults"
    try:
        response = dynamodb.put_item(
            TableName=examresults_table,
            Item={
                'idER': {'S': new_id},
                'exam': {'S': examName},
                'courseId': {'S': courseId},
                'studentId': {'S': studentId},
                'mark': {'N': str(mark)},
                'date': {'S': date},
                'name': {'S': nameStud},
                'surname': {'S': surnStud},
                'profId': {'S': profId}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'New exam result added successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error adding the exam result: ' + str(e)})
        }

def check_existence(table_name, key_name, key_value):
    # Verifica l'esistenza di un elemento in una tabella DynamoDB
    try:
        response = dynamodb.get_item(
            TableName=table_name,
            Key={key_name: {'S': key_value}}
        )
        return 'Item' in response
    except Exception as e:
        return False