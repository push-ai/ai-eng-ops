"""
A file processor with clear, contextual error messages.
This improved version demonstrates error messages that help AI self-correct and humans debug quickly.
"""

import os
import json
from pathlib import Path


class FileProcessorError(Exception):
    """Base exception for FileProcessor errors."""
    pass


class FileNotFoundError(FileProcessorError):
    """Raised when a file cannot be found."""
    pass


class InvalidFileError(FileProcessorError):
    """Raised when a file is invalid or cannot be processed."""
    pass


class InvalidOperationError(FileProcessorError):
    """Raised when an invalid operation is requested."""
    pass


class FileProcessor:
    """Processes files and performs operations on them."""
    
    def read_file(self, filepath):
        """
        Read contents of a file.
        
        Args:
            filepath: Path to the file to read
        
        Returns:
            File contents as string
        
        Raises:
            FileNotFoundError: If file doesn't exist
            PermissionError: If file cannot be read
        """
        filepath = Path(filepath)
        
        if not filepath.exists():
            raise FileNotFoundError(
                f"Cannot read file '{filepath}': File does not exist. "
                f"Check that the file path is correct and the file has been created."
            )
        
        if not filepath.is_file():
            raise InvalidFileError(
                f"Cannot read '{filepath}': Path exists but is not a file "
                f"(it may be a directory). Provide a file path instead."
            )
        
        if not os.access(filepath, os.R_OK):
            raise PermissionError(
                f"Cannot read file '{filepath}': Permission denied. "
                f"Check file permissions and ensure you have read access."
            )
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError as e:
            raise InvalidFileError(
                f"Cannot read file '{filepath}': Invalid encoding. "
                f"File appears to be binary or uses unsupported encoding. "
                f"Error details: {str(e)}"
            )
    
    def write_file(self, filepath, content):
        """
        Write content to a file.
        
        Args:
            filepath: Path to the file to write
            content: Content to write (string)
        
        Raises:
            PermissionError: If file cannot be written
            ValueError: If content is invalid
        """
        filepath = Path(filepath)
        
        if content is None:
            raise ValueError(
                "Cannot write file: Content is None. "
                "Provide a string value for content."
            )
        
        # Check if parent directory exists
        parent_dir = filepath.parent
        if not parent_dir.exists():
            raise FileNotFoundError(
                f"Cannot write file '{filepath}': Parent directory '{parent_dir}' does not exist. "
                f"Create the directory first or check the file path."
            )
        
        if not os.access(parent_dir, os.W_OK):
            raise PermissionError(
                f"Cannot write file '{filepath}': Permission denied for directory '{parent_dir}'. "
                f"Check directory permissions and ensure you have write access."
            )
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(content))
        except IOError as e:
            raise PermissionError(
                f"Cannot write file '{filepath}': I/O error occurred. "
                f"Error details: {str(e)}. "
                f"Check disk space and file permissions."
            )
    
    def process_json_file(self, filepath):
        """
        Process a JSON file and return parsed data.
        
        Args:
            filepath: Path to the JSON file
        
        Returns:
            Parsed JSON data
        
        Raises:
            FileNotFoundError: If file doesn't exist
            InvalidFileError: If file contains invalid JSON
        """
        try:
            data = self.read_file(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Cannot process JSON file '{filepath}': File not found. "
                f"Ensure the file exists before processing."
            )
        
        if not data.strip():
            raise InvalidFileError(
                f"Cannot process JSON file '{filepath}': File is empty. "
                f"JSON files must contain valid JSON data."
            )
        
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            raise InvalidFileError(
                f"Cannot process JSON file '{filepath}': Invalid JSON format. "
                f"Error at line {e.lineno}, column {e.colno}: {e.msg}. "
                f"Please validate the JSON syntax. "
                f"Problematic content: {data[max(0, e.pos-20):e.pos+20]}"
            )
    
    def validate_file_exists(self, filepath):
        """Check if file exists."""
        return Path(filepath).exists()
    
    def get_file_size(self, filepath):
        """Get file size in bytes."""
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(
                f"Cannot get file size for '{filepath}': File does not exist."
            )
        return filepath.stat().st_size
    
    def process_data(self, filepath, operation):
        """
        Process data from file with given operation.
        
        Args:
            filepath: Path to JSON file containing data
            operation: Operation to perform ('sum', 'count', or 'average')
        
        Returns:
            Result of the operation
        
        Raises:
            FileNotFoundError: If file doesn't exist
            InvalidFileError: If file contains invalid JSON or data type
            InvalidOperationError: If operation is not supported
        """
        if not self.validate_file_exists(filepath):
            raise FileNotFoundError(
                f"Cannot process data: File '{filepath}' does not exist. "
                f"Check that the file path is correct. "
                f"Current working directory: {os.getcwd()}"
            )
        
        try:
            data = self.process_json_file(filepath)
        except InvalidFileError as e:
            raise InvalidFileError(
                f"Cannot process data from '{filepath}': {str(e)}"
            )
        
        # Validate operation
        valid_operations = ['sum', 'count', 'average']
        if operation not in valid_operations:
            raise InvalidOperationError(
                f"Invalid operation '{operation}'. "
                f"Supported operations are: {', '.join(valid_operations)}. "
                f"Received: '{operation}'"
            )
        
        # Validate data type
        if not isinstance(data, list):
            raise InvalidFileError(
                f"Cannot perform '{operation}' operation on data from '{filepath}': "
                f"Expected data to be a list, but got {type(data).__name__}. "
                f"Data value: {str(data)[:100]}"
            )
        
        # Perform operation
        if operation == "sum":
            try:
                return sum(data)
            except TypeError as e:
                raise InvalidFileError(
                    f"Cannot calculate sum from '{filepath}': "
                    f"List contains non-numeric values. "
                    f"All elements must be numbers. Error: {str(e)}"
                )
        
        elif operation == "count":
            return len(data)
        
        elif operation == "average":
            if len(data) == 0:
                raise InvalidFileError(
                    f"Cannot calculate average from '{filepath}': "
                    f"List is empty. Provide a list with at least one element."
                )
            try:
                return sum(data) / len(data)
            except TypeError as e:
                raise InvalidFileError(
                    f"Cannot calculate average from '{filepath}': "
                    f"List contains non-numeric values. "
                    f"All elements must be numbers. Error: {str(e)}"
                )


# Example usage demonstrating improved error messages
if __name__ == "__main__":
    processor = FileProcessor()
    
    # This will fail with clear error
    try:
        result = processor.process_data("nonexistent.json", "sum")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        print("✓ Clear error message with context and guidance!\n")
    
    # This will also fail with clear error
    try:
        processor.write_file("/readonly/file.json", "{}")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
        print("✓ Clear error message explains what went wrong!\n")
    
    # Create a test file with invalid JSON
    processor.write_file("invalid.json", "{ invalid json }")
    
    try:
        result = processor.process_data("invalid.json", "sum")
    except InvalidFileError as e:
        print(f"InvalidFileError: {e}")
        print("✓ Error message shows where JSON is invalid!\n")
    
    # Test with valid file but invalid operation
    processor.write_file("valid.json", "[1, 2, 3, 4, 5]")
    
    try:
        result = processor.process_data("valid.json", "invalid_op")
    except InvalidOperationError as e:
        print(f"InvalidOperationError: {e}")
        print("✓ Error message lists valid operations!")

