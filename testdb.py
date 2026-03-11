from sqlite import init_db, save_user, get_user

# 1. On initialise (juste au cas où)
init_db()

# 2. On insère un utilisateur test
save_user(12345, "Nicolas", "test_token_abc123")

# 3. On tente de le récupérer
user = get_user(12345)
print(f"Utilisateur récupéré : {user}")