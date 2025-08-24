# TimeKeeper OS Uploader API Documentation

This document provides details on the API endpoints for the TimeKeeper OS Uploader service.

## API Base Path: `/upload`

---

### 1. File Upload

- **Endpoint**: `POST /upload/file`
- **Description**: Uploads a standard file (e.g., JSON, XML, CSV, TXT). The file is validated for size and type, and a checksum is calculated.
- **Request**: `multipart/form-data` with a single file part.
- **Response**:
  ```json
  {
    "status": "success",
    "filepath": "uploads/example.json",
    "metadata": {
      "filename": "example.json",
      "content_type": "application/json",
      "size_bytes": 1234,
      "sha256_checksum": "a1b2c3d4..."
    }
  }
  ```

---

### 2. Blockchain Data Upload

- **Endpoint**: `POST /upload/blockchain`
- **Description**: Submits blockchain-related data, such as a transaction, to be processed and associated with a TimeKeeper chronon.
- **Request**: `application/json`
- **Request Body**:
  ```json
  {
    "chain": "bitcoin",
    "tx_data": {
      "transaction_hash": "abc123def456"
    }
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Blockchain data received and acknowledged.",
    "chain": "bitcoin",
    "received_data": {
      "transaction_hash": "abc123def456"
    },
    "chronon_id": 1
  }
  ```

---

### 3. Spacetime Data Upload

- **Endpoint**: `POST /upload/spacetime`
- **Description**: *(Placeholder)* This endpoint is intended for uploading spacetime data, such as quantum state information or timeline events.
- **Request**: `application/json`
- **Response (Current)**:
  ```json
  {
    "status": "not_implemented",
    "feature": "spacetime_data_upload",
    "message": "This feature is not yet implemented."
  }
  ```

---

### 4. Smart Contract Upload

- **Endpoint**: `POST /upload/smart_contract`
- **Description**: *(Placeholder)* This endpoint is intended for uploading smart contracts (e.g., Solidity code) for compilation and deployment.
- **Request**: `application/json`
- **Response (Current)**:
  ```json
  {
    "status": "not_implemented",
    "feature": "smart_contract_upload",
    "message": "This feature is not yet implemented."
  }
  ```
