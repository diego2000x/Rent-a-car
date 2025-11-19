import bcrypt

class Encoder:
    def encode(self, string):
        # Genera hash seguro
        return bcrypt.hashpw(string.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def decode(self, string, password_hash):
        # Compara string plano con hash
        return bcrypt.checkpw(string.encode('utf-8'), password_hash.encode('utf-8'))