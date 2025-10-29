"""
A file processor with poor error messages.
This example demonstrates how vague errors make debugging difficult.
"""

import os
import json


class FileProcessor:
    """Processes files and performs operations on them."""
    
    def read_file(self, filepath):
        """Read contents of a file."""
        with open(filepath, 'r') as f:
            return f.read()
    
    def write_file(self, filepath, content):
        """Write content to a file."""
        with open(filepath, 'w') as f:
            f.write(content)
    
    def process_json_file(self, filepath):
        """Process a JSON file and return parsed data."""
        data = self.read_file(filepath)
        return json.loads(data)
    
    def validate_file_exists(self, filepath):
        """Check if file exists."""
        return os.path.exists(filepath)
    
    def get_file_size(self, filepath):
        """Get file size in bytes."""
        return os.path.getsize(filepath)
    
    def process_data(self, filepath, operation):
        """Process data from file with given operation."""
        if not self.validate_file_exists(filepath):
            raise Exception("Error")
        
        data = self.process_json_file(filepath)
        
        if operation == "sum":
            if not isinstance(data, list):
                raise Exception("Invalid")
            return sum(data)
        elif operation == "count":
            return len(data)
        elif operation == "average":
            if not isinstance(data, list):
                raise Exception("Invalid")
            if len(data) == 0:
                raise Exception("Error")
            return sum(data) / len(data)
        else:
            raise Exception("Unknown")


# Example usage demonstrating poor error messages
if __name__ == "__main__":
    processor = FileProcessor()
    
    # This will fail with vague error
    try:
        result = processor.process_data("nonexistent.json", "sum")
    except Exception as e:
        print(f"Error occurred: {e}")
        print("What went wrong? Hard to tell from this message!")
    
    # This will also fail with vague error
    try:
        processor.write_file("/readonly/file.json", "{}")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("What went wrong? Hard to tell from this message!")
    
    # Create a test file with invalid JSON
    processor.write_file("invalid.json", "{ invalid json }")
    
    try:
        result = processor.process_data("invalid.json", "sum")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("What went wrong? Hard to tell from this message!")

