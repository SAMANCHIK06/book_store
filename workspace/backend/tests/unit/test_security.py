import pytest
from datetime import timedelta, datetime
from workspace.backend.app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    SECRET_KEY,
    ALGORITHM
)
from jose import jwt

def test_hash_password():
    password = "testpassword123"
    hashed_pass = hash_password(password)
    assert isinstance(hashed_pass, str)
    assert len(hashed_pass) > 0
    # Har safar heshlanganda boshqa qiymat qaytarishi kerak (salt tufayli)
    assert hashed_pass != hash_password(password)

def test_verify_password_correct():
    password = "testpassword123"
    hashed_pass = hash_password(password)
    assert verify_password(password, hashed_pass) is True

def test_verify_password_incorrect():
    password = "testpassword123"
    wrong_password = "wrongpassword"
    hashed_pass = hash_password(password)
    assert verify_password(wrong_password, hashed_pass) is False

def test_create_access_token_default_expiry():
    data = {"sub": "testuser"}
    token = create_access_token(data)
    assert isinstance(token, str)
    assert len(token) > 0

    # Tokenni dekodlash va ma'lumotlarni tekshirish
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_payload["sub"] == "testuser"
    assert "exp" in decoded_payload
    
    # Expiry vaqtini tekshirish (taxminiy)
    expected_expiry_min = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    assert decoded_payload["exp"] > datetime.utcnow().timestamp()
    assert decoded_payload["exp"] < (expected_expiry_min + timedelta(minutes=1)).timestamp() # Kichik farq bo'lishi mumkin

def test_create_access_token_custom_expiry():
    data = {"sub": "testuser"}
    custom_expiry = timedelta(minutes=5)
    token = create_access_token(data, expires_delta=custom_expiry)
    
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_payload["sub"] == "testuser"
    assert "exp" in decoded_payload
    
    expected_expiry_min = datetime.utcnow() + custom_expiry
    assert decoded_payload["exp"] > datetime.utcnow().timestamp()
    assert decoded_payload["exp"] < (expected_expiry_min + timedelta(minutes=1)).timestamp()

def test_verify_token_valid():
    data = {"sub": "testuser", "user_id": 1}
    token = create_access_token(data)
    payload = verify_token(token)
    assert payload is not None
    assert payload["sub"] == "testuser"
    assert payload["user_id"] == 1

def test_verify_token_expired():
    data = {"sub": "testuser"}
    # O'tgan vaqt bilan token yaratish
    expired_delta = timedelta(minutes=-1)
    to_encode = data.copy()
    expire = datetime.utcnow() + expired_delta
    to_encode.update({"exp": expire})
    expired_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    payload = verify_token(expired_token)
    assert payload is None # Token muddati o'tgan bo'lsa, None qaytarishi kerak

def test_verify_token_invalid_signature():
    invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c_INVALID"
    payload = verify_token(invalid_token)
    assert payload is None

def test_verify_token_malformed():
    malformed_token = "this.is.not.a.jwt"
    payload = verify_token(malformed_token)
    assert payload is None
