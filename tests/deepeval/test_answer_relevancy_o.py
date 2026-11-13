
from dotenv import load_dotenv
load_dotenv()
from deepeval.evaluate import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from app.health_chatbot import health_chatbot

def test_answer_relevancy(): # pytest understand whe start with "test is test case"

    query = "What is IRA?" #input
    output = health_chatbot(query)

    # create test case
 
    test_case = LLMTestCase(
        input = query,
        actual_output= output
    )

    #define metric first
    answer_relevancy_metric = AnswerRelevancyMetric(threshold = 0.8)

    # Add assertion
    assert_test(test_case,[answer_relevancy_metric])