from users.schemas import CreateUser


def creae_user(user_in: CreateUser):
    user = user_in.model_dump()
    return {
        'success': True,
        'user': user,
    }
