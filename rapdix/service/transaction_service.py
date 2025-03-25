import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.model.page_entity import PageEntity
from rapdix.model.request.transcation.transaction_pageable_request import TransactionPageableRequest
from rapdix.model.request.transcation.transaction_request import TransactionRequest
from rapdix.model.vo.transcation.transaction_vo import TransactionVO
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService
from rapdix.model.request.transcation.transaction_archive_request import TransactionArchiveRequest
from rapdix.model.vo.transcation.transaction_archive_vo import TransactionArchiveVO

class TransactionService(BaseService):
    def query_transaction(self, request: TransactionRequest) -> Optional[ApiResponse[List[TransactionVO]]]:
        """
        Query transaction records
        
        Args:
            request: Transaction query request
        """
        url = f"{self.host}{APIConstants.TRANSACTION}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, TransactionVO)
    
    def query_transaction_pageable(self, request: TransactionPageableRequest) -> Optional[ApiResponse[PageEntity[TransactionVO]]]:
        """
        Query paginated transaction records
        
        Args:
            request: Transaction pageable query request
        """
        url = f"{self.host}{APIConstants.TRANSACTION_PAGEABLE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, TransactionVO)

    def query_transaction_archive(self, request: TransactionArchiveRequest) -> Optional[ApiResponse[PageEntity[TransactionArchiveVO]]]:
        """
        Query archived transaction records
        
        Args:
            request: Archive query request
        """
        url = f"{self.host}{APIConstants.TRANSACTION_PAGEABLE_ARCHIVE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, TransactionArchiveVO)
