import uuid
import logging
import bcrypt
import jwt
from datetime import datetime, timedelta
from proto import user_service_pb2
from .general_struct import UserStruct
from myapp.repository.user_repository import getUserByEmail, createUser, getUserById

logger = logging.getLogger('myapp')

def createUserHandler(request) -> user_service_pb2.CreateUserResponse:
  if not request.email:
      return user_service_pb2.CreateUserResponse(isSuccess=False, userId=0, errorMsg= "Email must not be empty")
  elif "@" not in request.email:
      return user_service_pb2.CreateUserResponse(isSuccess=False, userId=0, errorMsg= "Invalid email format")
  elif not request.password:
      return user_service_pb2.CreateUserResponse(isSuccess=False, userId=0, errorMsg= "Password must not be empty")
  elif len(request.password) < 6:
      return user_service_pb2.CreateUserResponse(isSuccess=False, userId=0, errorMsg= "Password must be at least 6 characters")
  elif not request.name:
      return user_service_pb2.CreateUserResponse(isSuccess=False, userId=0, errorMsg= "Name must not be empty")

  user = getUserByEmail(request.email)

  if user:
      return user_service_pb2.CreateUserResponse(isSuccess=False, userId=0, errorMsg= "email already registered")

  userData = UserStruct(name=request.name, email=request.email, password=request.password, role="admin")

  user = createUser(userData)

  return user_service_pb2.CreateUserResponse(isSuccess=True, userId=user.id, errorMsg= "")

def authenticationHandler(request) -> user_service_pb2.AuthResponse:
    if not request.email:
        return user_service_pb2.AuthResponse(isSuccess=False, errorMsg="Email must not be empty", accessToken="", refreshToken="")
    elif "@" not in request.email:
        return user_service_pb2.AuthResponse(isSuccess=False, errorMsg="Invalid email format", accessToken="", refreshToken="")
    elif not request.password:
        return user_service_pb2.AuthResponse(isSuccess=False, errorMsg="Password must not be empty", accessToken="", refreshToken="")
    elif len(request.password) < 6:
        return user_service_pb2.AuthResponse(isSuccess=False, errorMsg="Password must be at least 6 characters", accessToken="", refreshToken="")
    
    user = getUserByEmail(request.email)

    if not user:
        return user_service_pb2.AuthResponse(isSuccess=False, errorMsg="email or password is incorrect", accessToken="", refreshToken="")

    isValid = bcrypt.checkpw(request.password.encode('utf-8'), user.hashed_password.encode('utf-8'))

    if not isValid:
        return user_service_pb2.AuthResponse(isSuccess=False, errorMsg="email or password is incorrect", accessToken="", refreshToken="")

    accessToken, refreshToken = generateJwtToken({"id": user.id, "role": user.role})

    return user_service_pb2.AuthResponse(isSuccess=True, errorMsg="", accessToken=accessToken, refreshToken=refreshToken)

def getUserByIdHandler(request) -> user_service_pb2.GetUserByIdResponse:
    if not request.id:
        return getUserByIdErrorResponse("user id must not be empty")
    
    user = getUserById(request.id)

    if not user:
        return getUserByIdErrorResponse("user not found")

    return user_service_pb2.GetUserByIdResponse(isSuccess=True, errorMsg="", name=user.name)

def getUserByIdErrorResponse(errorMsg: str) -> user_service_pb2.GetUserByIdResponse:
    return user_service_pb2.GetUserByIdResponse(isSuccess=False, errorMsg=errorMsg, name="")

SECRET_KEY = "your-secret-key"


def generateJwtToken(data: dict) -> list[str]:
    print("Generating token for data:", data)
    
    # Access token expiration (15 minutes)
    access_exp = datetime.now() + timedelta(minutes=60)
    
    # Refresh token expiration (7 days)
    refresh_exp = datetime.now() + timedelta(hours=24)

    jti = str(uuid.uuid4())
    
    # Create access token
    access_token = jwt.encode(
        {
            "user_id": data["id"],
            "user_role": data["role"],  # User role
            "exp": access_exp,  # Expiry time
            "token_type": "access",
            "jti": jti 
        },
        SECRET_KEY,
        algorithm="HS256"
    )
    
    # Create refresh token
    refresh_token = jwt.encode(
        {
            "user_id": data["id"],
            "user_role": data["role"],  # User role
            "exp": refresh_exp,  # Expiry time
            "token_type": "refresh",
            "jti": jti 
        },
        SECRET_KEY,
        algorithm="HS256"
    )
    
    decodeJwtToken(access_token)

    # Return both tokens
    return [access_token, refresh_token]

def decodeJwtToken(token: str):
    try:
        
        logger.info("here11 %s", token)
        logger.info("here1")
        # Decode the token
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        logger.info("here2 %s", decoded)

    except jwt.ExpiredSignatureError:
        logger.info("here3 %s", jwt.ExpiredSignatureError)
        
    
    except jwt.InvalidTokenError:
        logger.info("here4 %s", str(jwt.InvalidTokenError))
        
    
