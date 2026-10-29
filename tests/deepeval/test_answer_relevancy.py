from dotenv import load_dotenv
load_dotenv()
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval import assert_test
from app.health_chatbot import health_chatbot


def test_answer_relevancy():
    query = "How to file a claim"
    output = health_chatbot(query)

    test_case = LLMTestCase(
        input = query,
        actual_output = output

    )

    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.8)

    assert_test(test_case,[answer_relevancy_metric])
    print(assert_test)

 