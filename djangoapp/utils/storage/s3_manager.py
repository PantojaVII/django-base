import os
import boto3
from botocore.exceptions import ClientError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class S3Manager:
    """
    Gerenciador de operações no Amazon S3.
    Fornece métodos para upload, exclusão e geração de URLs assinadas.
    """
    
    def __init__(self):
        """Inicializa o cliente S3 com as credenciais do settings."""
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
        self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    
    def upload_file(self, file_obj, key, content_type=None):
        """
        Faz upload de um arquivo para o S3.
        
        Args:
            file_obj: Objeto de arquivo (Django UploadedFile ou similar)
            key: Caminho/chave do arquivo no bucket S3
            content_type: Tipo MIME do arquivo (opcional)
        
        Returns:
            bool: True se o upload foi bem-sucedido, False caso contrário
        """
        try:
            extra_args = {}
            if content_type:
                extra_args['ContentType'] = content_type
            
            # Reset file pointer to beginning
            file_obj.seek(0)
            
            self.s3_client.upload_fileobj(
                file_obj,
                self.bucket_name,
                key,
                ExtraArgs=extra_args
            )
            
            logger.info(f"Arquivo enviado com sucesso para S3: {key}")
            return True
            
        except ClientError as e:
            logger.error(f"Erro ao fazer upload para S3: {e}")
            return False
    
    def delete_file(self, key):
        """
        Remove um arquivo do S3.
        
        Args:
            key: Caminho/chave do arquivo no bucket S3
        
        Returns:
            bool: True se a exclusão foi bem-sucedida, False caso contrário
        """
        try:
            self.s3_client.delete_object(
                Bucket=self.bucket_name,
                Key=key
            )
            logger.info(f"Arquivo removido com sucesso do S3: {key}")
            return True
            
        except ClientError as e:
            logger.error(f"Erro ao deletar arquivo do S3: {e}")
            return False
    
    def generate_presigned_url(self, key, expiration=3600):
        """
        Gera uma URL assinada temporária para acesso ao arquivo.
        
        Args:
            key: Caminho/chave do arquivo no bucket S3
            expiration: Tempo de expiração da URL em segundos (padrão: 1 hora)
        
        Returns:
            str: URL assinada ou None em caso de erro
        """
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': self.bucket_name,
                    'Key': key
                },
                ExpiresIn=expiration
            )
            return url
            
        except ClientError as e:
            logger.error(f"Erro ao gerar URL assinada: {e}")
            return None
    
    def file_exists(self, key):
        """
        Verifica se um arquivo existe no S3.
        
        Args:
            key: Caminho/chave do arquivo no bucket S3
        
        Returns:
            bool: True se o arquivo existe, False caso contrário
        """
        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=key)
            return True
        except ClientError:
            return False
    
    def get_file_size(self, key):
        """
        Obtém o tamanho de um arquivo no S3.
        
        Args:
            key: Caminho/chave do arquivo no bucket S3
        
        Returns:
            int: Tamanho do arquivo em bytes ou None se não encontrado
        """
        try:
            response = self.s3_client.head_object(Bucket=self.bucket_name, Key=key)
            return response['ContentLength']
        except ClientError as e:
            logger.error(f"Erro ao obter tamanho do arquivo: {e}")
            return None
