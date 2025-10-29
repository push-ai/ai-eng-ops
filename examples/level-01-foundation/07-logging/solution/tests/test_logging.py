"""
Tests for logging functionality demonstrating how logs help identify root causes.
"""

import pytest
import logging
from io import StringIO
from main import DataProcessor, OrderProcessor


class TestDataProcessorLogging:
    """Tests for DataProcessor logging."""
    
    def setup_method(self):
        """Set up test fixture."""
        self.processor = DataProcessor()
        # Capture logs
        self.log_capture = StringIO()
        handler = logging.StreamHandler(self.log_capture)
        handler.setLevel(logging.DEBUG)
        logger = logging.getLogger('__main__')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    
    def test_fetch_data_logs_operation(self):
        """Test that fetch_data logs operation details."""
        data = self.processor.fetch_data("test_source")
        
        log_output = self.log_capture.getvalue()
        assert "Fetching data" in log_output
        assert "test_source" in log_output
        assert "Data fetched successfully" in log_output
    
    def test_validate_data_logs_validation_results(self):
        """Test that validate_data logs validation results."""
        # Test with valid data
        valid_data = [1, 2, 3, 4, 5]
        result = self.processor.validate_data(valid_data)
        
        log_output = self.log_capture.getvalue()
        assert "Data validation passed" in log_output
        
        # Test with invalid data
        self.log_capture.seek(0)
        self.log_capture.truncate(0)
        invalid_data = [1, 2]
        result = self.processor.validate_data(invalid_data)
        
        log_output = self.log_capture.getvalue()
        assert "Validation failed" in log_output or "insufficient data" in log_output
    
    def test_process_logs_correlation_id(self):
        """Test that process logs include correlation ID."""
        self.processor.process("test_source", "test_dest")
        
        log_output = self.log_capture.getvalue()
        assert "correlation_id" in log_output
        assert "Starting data processing" in log_output
    
    def test_process_logs_performance(self):
        """Test that process logs performance metrics."""
        self.processor.process("test_source", "test_dest")
        
        log_output = self.log_capture.getvalue()
        assert "duration_ms" in log_output or "duration" in log_output
        assert "total_duration_ms" in log_output


class TestOrderProcessorLogging:
    """Tests for OrderProcessor logging."""
    
    def setup_method(self):
        """Set up test fixture."""
        self.processor = OrderProcessor()
        # Capture logs
        self.log_capture = StringIO()
        handler = logging.StreamHandler(self.log_capture)
        handler.setLevel(logging.DEBUG)
        logger = logging.getLogger('__main__')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    
    def test_process_order_logs_order_details(self):
        """Test that process_order logs order details."""
        result = self.processor.process_order("order123", {"item1": 2})
        
        log_output = self.log_capture.getvalue()
        assert "Processing order" in log_output
        assert "order123" in log_output
        assert "Order processed successfully" in log_output
    
    def test_process_order_logs_inventory_changes(self):
        """Test that process_order logs inventory state changes."""
        initial_inventory = self.processor.inventory["item1"]
        result = self.processor.process_order("order123", {"item1": 2})
        
        log_output = self.log_capture.getvalue()
        assert "Inventory reserved" in log_output
        assert "inventory_changes" in log_output or "old" in log_output
    
    def test_process_order_logs_failure_reason(self):
        """Test that process_order logs failure reason."""
        result = self.processor.process_order("order124", {"item3": 1})
        
        log_output = self.log_capture.getvalue()
        assert "Order processing failed" in log_output or "insufficient inventory" in log_output
        assert "item3" in log_output
    
    def test_check_inventory_logs_details(self):
        """Test that check_inventory logs checking details."""
        self.processor.check_inventory("item1", 5)
        
        log_output = self.log_capture.getvalue()
        assert "Checking inventory" in log_output or "inventory" in log_output.lower()
    
    def test_check_inventory_logs_shortage(self):
        """Test that check_inventory logs shortage details."""
        self.processor.check_inventory("item1", 100)  # More than available
        
        log_output = self.log_capture.getvalue()
        assert "Insufficient inventory" in log_output or "shortage" in log_output.lower()

