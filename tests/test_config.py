import os
from unittest.mock import patch, Mock
import pytest

from config import create_client

def test_create_client_success():
    with patch('os.getenv', return_value='mock_api_key'), \
         patch('instructor.patch') as mock_patch, \
         patch('instructor.from_openai') as mock_from_openai, \
         patch('logfire.configure'), \
         patch('logfire.instrument_openai'):
        mock_patch.return_value = Mock()
        mock_from_openai.return_value = 'mock_instructor_client'
        
        client = create_client()
        
        assert client == 'mock_instructor_client'
        os.getenv.assert_called_once_with("FIREWORKS_API_KEY")
        mock_patch.assert_called()
        mock_from_openai.assert_called()

def test_create_client_no_api_key():
    with patch('os.getenv', return_value=None):
        with pytest.raises(ValueError) as excinfo:
            create_client()
        assert str(excinfo.value) == "FIREWORKS_API_KEY is not set in the environment variables."
