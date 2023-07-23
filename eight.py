import base64

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# 8
def decodeAndTransferBlobData():

    srcConnectionString = "DefaultEndpointsProtocol=https;AccountName=onboardingpractice;AccountKey=2qAbr+yOWtOTrtZ50YLRRDsqp8eLL/zgOXl4pdeiWyanhZ4VkFMqXwd6PMAUBRqy0oTo1QcX2F79+AStaFSy9g==;EndpointSuffix=core.windows.net"
    destConnectionString = "DefaultEndpointsProtocol=https;AccountName=shellyhafifa;AccountKey=1pO4AFwfTX0qOZeElD3GXs+omnfbpuN/K2CuMOy19Zfr9TzTP8pzcY0W0dKX6vDtUPmnh1IdwALr+AStm86TnA==;EndpointSuffix=core.windows.net"
    srcContainerName = "python"
    destContainerName = "pythondecoded"

    srcStorageAcc = BlobServiceClient.from_connection_string(conn_str=srcConnectionString)
    destStorageAcc = BlobServiceClient.from_connection_string(conn_str=destConnectionString)

    srcContainer = srcStorageAcc.get_container_client(container=srcContainerName)
    destContainer = destStorageAcc.get_container_client(container=destContainerName)

    blobsList = srcContainer.list_blob_names()

    for blobName in blobsList:
        blobContent = srcContainer.download_blob(blobName).readall()
        decodedBlobContent = decodeMessage(blobContent)
        destContainer.upload_blob(name=blobName, data=decodedBlobContent)
        
    pass

def decodeMessage(encodedMessage):
    messageBytes = encodedMessage.decode("ascii")
    decodedBytes = base64.b64decode(messageBytes)
    decodedMessage = decodedBytes.decode("ascii")

    return decodedMessage