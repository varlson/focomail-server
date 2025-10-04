def user_helper(content) -> dict:
    return {
        "id": str(content["_id"]),
        "name": content["name"],
        "email": content["email"]
    }
