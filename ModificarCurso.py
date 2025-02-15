import boto3

def lambda_handler(event, context):
    # Entrada (json)
    curso_id = event['body']['curso_id']
    datos = event['body']['datos']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cursos')
    response = table.update_item(
        Key={
            'curso_id': curso_id
        },
        UpdateExpression="set datos=:datos_a_actualizar",
        ExpressionAttributeValues={
            ':datos_a_actualizar': datos
        },
        ReturnValues="UPDATED_NEW"
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
