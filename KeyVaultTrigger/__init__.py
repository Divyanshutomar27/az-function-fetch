import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing request to retrieve secret from Azure Key Vault.")

    # Replace with your Azure Key Vault URL
    key_vault_url = "https://test-az-function.vault.azure.net/"

    # Replace with your secret name
    secret_name = "key1"

    try:
        # Authenticate and connect to Key Vault
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=key_vault_url, credential=credential)

        # Retrieve the secret value
        secret = client.get_secret(secret_name)

        logging.info(f"Retrieved secret: {secret_name}")
        return func.HttpResponse(f"Secret Value: {secret.value}")
    except Exception as e:
        logging.error(f"Error retrieving secret: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
