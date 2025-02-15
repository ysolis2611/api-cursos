import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    curso_id = event['body']['curso_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cursos')
    response = table.query(
        KeyConditionExpression=Key('curso_id').eq(curso_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }
