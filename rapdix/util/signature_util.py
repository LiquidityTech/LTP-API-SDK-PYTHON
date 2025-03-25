from datetime import datetime
import time
import hmac
import hashlib
from urllib.parse import urlencode
from typing import Dict, Any
from collections import OrderedDict

class SignatureUtil:
    @staticmethod
    def gmt_now() -> str:
        """
        Get current timestamp (seconds)
        """
        return str(int(time.time()))

    @staticmethod
    def get_sign(param: Dict[str, Any], secret_key: str, nonce: str) -> str:
        """
        Generate signature
        
        Args:
            param: Parameter dictionary
            secret_key: Secret key
            nonce: Random string
        
        Returns:
            Signature string
        """
        payload = SignatureUtil.get_payload_for_sign(param)
        payload += f"&{nonce}"
        
        try:
            # Generate signature using HMAC-SHA256 algorithm
            mac = hmac.new(
                secret_key.encode('utf-8'),
                payload.encode('utf-8'),
                hashlib.sha256
            )
            return mac.hexdigest()
        except Exception as e:
            raise RuntimeError(f"Error generating sign: {str(e)}")

    @staticmethod
    def get_payload(param_map: Dict[str, Any]) -> str:
        """
        Generate URL-encoded parameter string
        
        Args:
            param_map: Parameter dictionary
        
        Returns:
            URL-encoded parameter string
        """
        try:
            # Ensure parameters are sorted
            ordered_params = OrderedDict(sorted(param_map.items()))
            return urlencode(ordered_params)
        except Exception as e:
            raise RuntimeError(f"Error generating payload: {str(e)}")

    @staticmethod
    def get_payload_for_sign(param_map: Dict[str, Any]) -> str:
        """
        Generate parameter string for signing (without URL encoding)
        
        Args:
            param_map: Parameter dictionary
        
        Returns:
            Parameter string for signing
        """
        try:
            # Ensure parameters are sorted
            ordered_params = OrderedDict(sorted(param_map.items()))
            return '&'.join(f"{key}={value}" for key, value in ordered_params.items())
        except Exception as e:
            raise RuntimeError(f"Error generating payload for sign: {str(e)}") 