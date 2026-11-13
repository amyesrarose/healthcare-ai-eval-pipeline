from dotenv import load_dotenv
load_dotenv()
from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase , LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval
from app.health_chatbot import health_chatbot


def test_answer_relevancy_costum():

    query = "What is my out-of-pocket amount"
    output = """Your yearly out of pocket amount is for indivudual is $1500 for a family $3000.
    If you dont have a family to save """

    test_case = LLMTestCase(
        input = query,
        actual_output = output
    )

    answer_relevancy =GEval(
        name = "Answer Relevancy",
        criteria="Check if the answer is relevant",
        evaluation_params=[
                        LLMTestCaseParams.INPUT,
                        LLMTestCaseParams.ACTUAL_OUTPUT
                        ],
        evaluation_steps=[        
                        "Check if the answer is fully relevant to the query"
                        "If answer is not relevant lower the score"
        ],
        threshold = 0.8
    )

    result =evaluate([test_case],[answer_relevancy])
    print (result)

