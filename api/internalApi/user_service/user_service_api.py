
import httpx

from config.config import Config

config = Config()


async def is_user_registered(user_id: int) -> bool:
    url = f"{config.USER_SERVICE_BASE_URL}/user/registered/{user_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            data = response.json()
            return data.get("is_registered")
        except httpx.HTTPStatusError as exception:
            print(f"Error in getting user info for user {user_id} with error: {exception.response}")
            return False
