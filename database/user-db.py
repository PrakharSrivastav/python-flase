class UserDBClass(UserDBInterface):
    """Extract text from an email"""
    def save(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        # actual logic goes here

        pass

    def delete(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


