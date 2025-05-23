from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "astral-name-458713-g7"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load3",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://dataflow-job-metadata-bkt/udf.js",
        "JSONPath": "gs://dataflow-job-metadata-bkt/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "astral-name-458713-g7:cricket_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": "gs://cricket-ranking-bkt/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://dataflow-job-metadata-bkt",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

