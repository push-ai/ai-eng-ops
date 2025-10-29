"""
Tests for FileProcessor demonstrating how good error messages help debugging.
"""

import pytest
import tempfile
import os
from pathlib import Path
from main import (
    FileProcessor,
    FileNotFoundError,
    InvalidFileError,
    InvalidOperationError
)


class TestFileProcessor:
    """Tests for FileProcessor with focus on error messages."""
    
    def setup_method(self):
        """Set up test fixture."""
        self.processor = FileProcessor()
        self.temp_dir = tempfile.mkdtemp()
    
    def teardown_method(self):
        """Clean up test files."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_read_nonexistent_file_raises_clear_error(self):
        """Test that reading nonexistent file gives clear error message."""
        filepath = os.path.join(self.temp_dir, "nonexistent.txt")
        
        with pytest.raises(FileNotFoundError) as exc_info:
            self.processor.read_file(filepath)
        
        error_msg = str(exc_info.value)
        assert "does not exist" in error_msg
        assert filepath in error_msg
        assert "Check that the file path" in error_msg
    
    def test_read_directory_raises_clear_error(self):
        """Test that reading a directory gives clear error."""
        with pytest.raises(InvalidFileError) as exc_info:
            self.processor.read_file(self.temp_dir)
        
        error_msg = str(exc_info.value)
        assert "is not a file" in error_msg
        assert "it may be a directory" in error_msg
    
    def test_write_nonexistent_directory_raises_clear_error(self):
        """Test that writing to nonexistent directory gives clear error."""
        filepath = os.path.join(self.temp_dir, "nonexistent", "file.txt")
        
        with pytest.raises(FileNotFoundError) as exc_info:
            self.processor.write_file(filepath, "content")
        
        error_msg = str(exc_info.value)
        assert "Parent directory" in error_msg
        assert "does not exist" in error_msg
        assert "Create the directory first" in error_msg
    
    def test_process_invalid_json_raises_clear_error(self):
        """Test that invalid JSON gives clear error with location."""
        filepath = os.path.join(self.temp_dir, "invalid.json")
        self.processor.write_file(filepath, "{ invalid json }")
        
        with pytest.raises(InvalidFileError) as exc_info:
            self.processor.process_json_file(filepath)
        
        error_msg = str(exc_info.value)
        assert "Invalid JSON format" in error_msg
        assert "line" in error_msg.lower() or "column" in error_msg.lower()
    
    def test_process_empty_json_raises_clear_error(self):
        """Test that empty JSON file gives clear error."""
        filepath = os.path.join(self.temp_dir, "empty.json")
        self.processor.write_file(filepath, "")
        
        with pytest.raises(InvalidFileError) as exc_info:
            self.processor.process_json_file(filepath)
        
        error_msg = str(exc_info.value)
        assert "File is empty" in error_msg
        assert "must contain valid JSON" in error_msg
    
    def test_process_data_invalid_operation_raises_clear_error(self):
        """Test that invalid operation gives clear error with valid options."""
        filepath = os.path.join(self.temp_dir, "data.json")
        self.processor.write_file(filepath, "[1, 2, 3]")
        
        with pytest.raises(InvalidOperationError) as exc_info:
            self.processor.process_data(filepath, "invalid_op")
        
        error_msg = str(exc_info.value)
        assert "Invalid operation" in error_msg
        assert "invalid_op" in error_msg
        assert "sum" in error_msg or "count" in error_msg or "average" in error_msg
    
    def test_process_data_wrong_type_raises_clear_error(self):
        """Test that wrong data type gives clear error."""
        filepath = os.path.join(self.temp_dir, "not_list.json")
        self.processor.write_file(filepath, '{"key": "value"}')
        
        with pytest.raises(InvalidFileError) as exc_info:
            self.processor.process_data(filepath, "sum")
        
        error_msg = str(exc_info.value)
        assert "Expected data to be a list" in error_msg
        assert "dict" in error_msg.lower() or "object" in error_msg.lower()
    
    def test_process_data_empty_list_average_raises_clear_error(self):
        """Test that empty list for average gives clear error."""
        filepath = os.path.join(self.temp_dir, "empty_list.json")
        self.processor.write_file(filepath, "[]")
        
        with pytest.raises(InvalidFileError) as exc_info:
            self.processor.process_data(filepath, "average")
        
        error_msg = str(exc_info.value)
        assert "List is empty" in error_msg
        assert "at least one element" in error_msg
    
    def test_process_data_non_numeric_sum_raises_clear_error(self):
        """Test that non-numeric values give clear error."""
        filepath = os.path.join(self.temp_dir, "non_numeric.json")
        self.processor.write_file(filepath, '["a", "b", "c"]')
        
        with pytest.raises(InvalidFileError) as exc_info:
            self.processor.process_data(filepath, "sum")
        
        error_msg = str(exc_info.value)
        assert "non-numeric" in error_msg.lower()
        assert "must be numbers" in error_msg.lower()
    
    def test_successful_operations(self):
        """Test that valid operations work correctly."""
        filepath = os.path.join(self.temp_dir, "data.json")
        self.processor.write_file(filepath, "[1, 2, 3, 4, 5]")
        
        assert self.processor.process_data(filepath, "sum") == 15
        assert self.processor.process_data(filepath, "count") == 5
        assert self.processor.process_data(filepath, "average") == 3.0

