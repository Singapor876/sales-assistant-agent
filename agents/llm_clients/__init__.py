from .llms import get_llm
# 加载配置信息
from dotenv import load_dotenv

load_dotenv()

llm, llm_embedding = get_llm("qwen")
