import boto3

def lambda_handler(event, context):
    # Entrada (json)
    curso_id = event['body']['curso_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cursos')
    response = table.delete_item(
        Key={
            'curso_id': curso_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
