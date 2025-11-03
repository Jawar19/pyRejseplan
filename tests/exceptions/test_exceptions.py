"""Tests for pyRejseplan exceptions."""
import pytest
from py_rejseplan.exceptions import (
    RejseplanError,
    APIError,
    HTTPError,
    ConnectionError,
    DepartureError,
    ValidationError,
    # Backward compatibility aliases
    RPAPIError,
    RPHTTPError,
    RPConnectionError,
    DepartureAPIError,
    RPValidationError,
)


class TestExceptionHierarchy:
    """Test the exception inheritance hierarchy."""
    
    def test_base_exception_hierarchy(self):
        """Test that all exceptions inherit from RejseplanError."""
        assert issubclass(APIError, RejseplanError)
        assert issubclass(HTTPError, RejseplanError)
        assert issubclass(ConnectionError, RejseplanError)
        assert issubclass(ValidationError, RejseplanError)
        assert issubclass(DepartureError, APIError)
        
    def test_rejseplan_error_inherits_from_exception(self):
        """Test that RejseplanError inherits from Exception."""
        assert issubclass(RejseplanError, Exception)
        
    def test_departure_error_hierarchy(self):
        """Test that DepartureError inherits from APIError."""
        assert issubclass(DepartureError, APIError)
        assert issubclass(DepartureError, RejseplanError)
        assert issubclass(DepartureError, Exception)


class TestRejseplanError:
    """Test the base RejseplanError class."""
    
    def test_basic_error_creation(self):
        """Test basic error creation with message only."""
        error = RejseplanError("Test error")
        assert error.message == "Test error"
        assert error.status_code is None
        assert error.response is None
        
    def test_error_with_status_code(self):
        """Test error creation with status code."""
        error = RejseplanError("Test error", status_code=400)
        assert error.message == "Test error"
        assert error.status_code == 400
        assert error.response is None
        
    def test_error_with_response(self):
        """Test error creation with response object."""
        mock_response = {"status": "error"}
        error = RejseplanError("Test error", response=mock_response)
        assert error.message == "Test error"
        assert error.status_code is None
        assert error.response == mock_response
        
    def test_error_str_without_status_code(self):
        """Test string representation without status code."""
        error = RejseplanError("Test error")
        expected = "RejseplanError: Test error"
        assert str(error) == expected
        
    def test_error_str_with_status_code(self):
        """Test string representation with status code."""
        error = RejseplanError("Test error", status_code=404)
        expected = "RejseplanError (status code: 404): Test error"
        assert str(error) == expected
        
    def test_error_repr(self):
        """Test repr representation."""
        error = RejseplanError("Test error", status_code=500)
        expected = 'RejseplanError(message="Test error", status_code=500)'
        assert repr(error) == expected


class TestAPIError:
    """Test the APIError class."""
    
    def test_api_error_creation(self):
        """Test APIError creation."""
        error = APIError("API failed", status_code=500)
        assert isinstance(error, RejseplanError)
        assert error.message == "API failed"
        assert error.status_code == 500
        
    def test_api_error_str(self):
        """Test APIError string representation."""
        error = APIError("API failed", status_code=500)
        expected = "APIError (status code: 500): API failed"
        assert str(error) == expected


class TestDepartureError:
    """Test the DepartureError class."""
    
    def test_departure_error_creation(self):
        """Test DepartureError creation."""
        error = DepartureError("Departure API failed")
        assert isinstance(error, APIError)
        assert isinstance(error, RejseplanError)
        assert error.message == "Departure API failed"
        
    def test_departure_error_with_response(self):
        """Test DepartureError with response."""
        mock_response = {"error": "Invalid stop ID"}
        error = DepartureError("Invalid request", status_code=400, response=mock_response)
        assert error.status_code == 400
        assert error.response == mock_response


class TestConnectionError:
    """Test the ConnectionError class."""
    
    def test_connection_error_basic(self):
        """Test basic ConnectionError."""
        error = ConnectionError("Network timeout")
        assert error.message == "Network timeout"
        assert error.original_error is None
        
    def test_connection_error_with_original(self):
        """Test ConnectionError with original exception."""
        original = ValueError("Invalid URL")
        error = ConnectionError("Connection failed", original_error=original)
        assert error.original_error == original
        
    def test_connection_error_str_with_original(self):
        """Test ConnectionError string with original error."""
        original = ValueError("Invalid URL")
        error = ConnectionError("Connection failed", original_error=original)
        expected = "ConnectionError: Connection failed (caused by: Invalid URL)"
        assert str(error) == expected
        
    def test_connection_error_repr_with_original(self):
        """Test ConnectionError repr with original error."""
        original = ValueError("Invalid URL")
        error = ConnectionError("Connection failed", original_error=original)
        expected = 'ConnectionError(message="Connection failed", status_code=None, original_error=Invalid URL)'
        assert repr(error) == expected


class TestValidationError:
    """Test the ValidationError class."""
    
    def test_validation_error_basic(self):
        """Test basic ValidationError."""
        error = ValidationError("Invalid data")
        assert error.message == "Invalid data"
        assert error.field is None
        assert error.value is None
        
    def test_validation_error_with_field(self):
        """Test ValidationError with field information."""
        error = ValidationError("Invalid value", field="stop_id", value="abc123")
        assert error.field == "stop_id"
        assert error.value == "abc123"
        
    def test_validation_error_str_with_field(self):
        """Test ValidationError string with field info."""
        error = ValidationError("Invalid value", field="stop_id", value="abc123")
        expected = "ValidationError: Invalid value (field: stop_id, value: abc123)"
        assert str(error) == expected
        
    def test_validation_error_repr(self):
        """Test ValidationError repr."""
        error = ValidationError("Invalid value", field="stop_id", value="abc123")
        expected = 'ValidationError(message="Invalid value", field="stop_id", value=abc123)'
        assert repr(error) == expected


class TestBackwardCompatibility:
    """Test backward compatibility aliases."""
    
    def test_alias_equivalence(self):
        """Test that aliases point to correct classes."""
        assert RPAPIError is APIError
        assert RPHTTPError is HTTPError
        assert RPConnectionError is ConnectionError
        assert DepartureAPIError is DepartureError
        assert RPValidationError is ValidationError
        
    def test_alias_creation(self):
        """Test creating exceptions using old names."""
        error = DepartureAPIError("Test error")
        assert isinstance(error, DepartureError)
        assert isinstance(error, APIError)
        assert error.message == "Test error"
        
    def test_alias_catching(self):
        """Test catching exceptions using old names."""
        try:
            raise DepartureError("Test error")
        except DepartureAPIError as e:
            assert e.message == "Test error"
        except Exception:
            pytest.fail("Should have caught using alias")


class TestExceptionUsage:
    """Test practical exception usage scenarios."""
    
    def test_catch_all_pyrejseplan_errors(self):
        """Test catching all library errors."""
        errors_to_test = [
            APIError("API error"),
            HTTPError("HTTP error"),
            ConnectionError("Connection error"),
            DepartureError("Departure error"),
            ValidationError("Validation error"),
        ]
        
        for error in errors_to_test:
            try:
                raise error
            except RejseplanError:
                pass  # Should catch all
            except Exception:
                pytest.fail(f"Failed to catch {type(error).__name__} as RejseplanError")
                
    def test_catch_specific_error_types(self):
        """Test catching specific error types."""
        try:
            raise DepartureError("Departure failed")
        except DepartureError as e:
            assert e.message == "Departure failed"
        except Exception:
            pytest.fail("Should have caught DepartureError")
            
        try:
            raise HTTPError("HTTP failed", status_code=404)
        except HTTPError as e:
            assert e.status_code == 404
        except Exception:
            pytest.fail("Should have caught HTTPError")