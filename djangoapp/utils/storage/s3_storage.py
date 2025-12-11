from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from .s3_manager import S3Manager
import mimetypes


@deconstructible
class S3Storage(Storage):
    """
    Custom storage backend para usar Amazon S3.
    """
    
    def __init__(self):
        self.s3_manager = S3Manager()
    
    def _save(self, name, content):
        """
        Salva o arquivo no S3.
        
        Args:
            name: Nome/caminho do arquivo
            content: Conteúdo do arquivo
        
        Returns:
            str: Nome do arquivo salvo
        """
        # Detectar content type
        content_type, _ = mimetypes.guess_type(name)
        
        # Upload para S3
        self.s3_manager.upload_file(content.file, name, content_type)
        return name
    
    def exists(self, name):
        """
        Verifica se um arquivo existe no S3.
        
        Args:
            name: Nome/caminho do arquivo
        
        Returns:
            bool: True se existe, False caso contrário
        """
        return self.s3_manager.file_exists(name)
    
    def url(self, name):
        """
        Retorna a URL assinada do arquivo.
        
        Args:
            name: Nome/caminho do arquivo
        
        Returns:
            str: URL assinada do arquivo
        """
        # Gera URL válida por 1 hora (3600 segundos)
        return self.s3_manager.generate_presigned_url(name, expiration=3600)
    
    def delete(self, name):
        """
        Deleta um arquivo do S3.
        
        Args:
            name: Nome/caminho do arquivo
        """
        self.s3_manager.delete_file(name)
    
    def size(self, name):
        """
        Retorna o tamanho do arquivo em bytes.
        
        Args:
            name: Nome/caminho do arquivo
        
        Returns:
            int: Tamanho do arquivo em bytes
        """
        return self.s3_manager.get_file_size(name)
    
    def get_accessed_time(self, name):
        """Não implementado para S3."""
        raise NotImplementedError("S3 storage doesn't support accessed time")
    
    def get_created_time(self, name):
        """Não implementado para S3."""
        raise NotImplementedError("S3 storage doesn't support created time")
    
    def get_modified_time(self, name):
        """Não implementado para S3."""
        raise NotImplementedError("S3 storage doesn't support modified time")
