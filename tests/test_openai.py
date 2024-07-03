from MPOPlayWright.Payload.ai_helper import generate_test_input
from MPOPlayWright.utils.logger import setup_logger
import logging


logger = setup_logger()
# Setup logger
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def test_openai(page):
    prompt = "Generate a realistic username for testing login functionality."
    username = generate_test_input(prompt)
    password_prompt = "Generate a realistic password for testing login functionality."
    password = generate_test_input(password_prompt)

    print(f"AI Generated Username: {username}")
    logger.info(f"AI Model Response: "
                f": User Name->: {username} ")
    logger.info(f"AI Model Response: "
                f": Password->: {password} ")



