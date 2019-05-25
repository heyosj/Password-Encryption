from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes = ['pbkdf2_sha256'],
    default = 'pbkdf2_sha256',
    pbkdf2_sha256__default_rounds = 30000
)

def encrypt_password(password):
    print(pwd_context.encrypt(password)) ## Change print to return statement

def check_encrypted_password(password, hashed):
    print(pwd_context.verify(password, hashed))


encrypt_password('abc') ## Test

check_encrypted_password('abc', '$pbkdf2-sha256$30000$hLBWinFOydk7B8B4rzVGSA$LGw50SfZ0x/dLQLMZ0Wm5.DV07qwf91VTaN5/34VK4w') ## Output True
check_encrypted_password('password', '$pbkdf2-sha256$30000$hLBWinFOydk7B8B4rzVGSA$LGw50SfZ0x/dLQLMZ0Wm5.DV07qwf91VTaN5/34VK4w') ## Output False