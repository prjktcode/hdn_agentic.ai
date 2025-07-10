from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

llm = ChatOpenAI(openai_api_key="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", model_name="gpt 4")

symptom_parser_template = """
Given the following free-text description of a patient's symptoms, extract the structured list of medical symptoms.

Text: "{text}"
Extracted Symptoms (in list form):
"""

parser_prompt = PromptTemplate(
    input_variables=["text"],
    template=symptom_parser_template
)

symptom_parser_chain = LLMChain(llm=llm, prompt=parser_prompt)

def extract_symptoms_from_text(text):
    response = symptom_parser_chain.run(text)
    try:
        return eval(response.strip())  
    except:
        return []
