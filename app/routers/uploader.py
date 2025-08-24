from __future__ import annotations
from typing import Any
from litestar import Router, post
from litestar.datastructures import UploadFile
from litestar.enums import RequestEncodingType
from litestar.params import Body
from ..services.uploader import UploaderService

@post(path="/file", media_type="application/json")
async def handle_file_upload(
    uploader_service: UploaderService,
    data: UploadFile = Body(media_type=RequestEncodingType.MULTI_PART),
) -> dict:
    """
    Endpoint to handle standard file uploads.
    Accepts a multipart form data with a file part.
    """
    result = await uploader_service.handle_file_upload(file=data)
    return result

@post(path="/blockchain", media_type="application/json")
async def handle_blockchain_upload(
    uploader_service: UploaderService,
    data: dict[str, Any]
) -> dict:
    """
    Endpoint to handle blockchain data submissions.
    Accepts a JSON body with 'chain' and 'tx_data'.
    """
    result = await uploader_service.handle_blockchain_data(data)
    return result

@post(path="/spacetime", media_type="application/json")
async def handle_spacetime_upload(
    uploader_service: UploaderService,
    data: dict[str, Any]
) -> dict:
    """
    Endpoint to handle spacetime data submissions.
    """
    result = await uploader_service.handle_spacetime_data(data)
    return result

@post(path="/smart_contract", media_type="application/json")
async def handle_smart_contract_upload(
    uploader_service: UploaderService,
    data: dict[str, Any]
) -> dict:
    """
    Endpoint to handle smart contract submissions.
    """
    result = await uploader_service.handle_smart_contract_upload(data)
    return result

uploader_router = Router(
    path="/upload",
    route_handlers=[
        handle_file_upload,
        handle_blockchain_upload,
        handle_spacetime_upload,
        handle_smart_contract_upload,
    ]
)
