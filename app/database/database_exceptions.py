class DatabaseException(Exception):
    def __init__(self,message:str):
        super().__init__(message)
        self.message = message
        
    def __str__(self):
        print(f"{self.message} error occurred")