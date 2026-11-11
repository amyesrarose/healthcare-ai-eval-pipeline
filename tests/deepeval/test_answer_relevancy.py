import pytest
from dotenv import load_dotenv
load_dotenv()
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from app.health_chatbot import health_chatbot

queries =[
    "How to file a claim",
    "What is my benefit window?",
    "Is dentist covered by insurance",
    "Is zoloft covered? If so what would be the price?",
    "My mom  does not have SSN can she be covered as my dependent.",
    ("My daugther is vomitted twice in last 3 hour. IF I take her th ER, is ER would be covered by my insurance"),
    "Is Dr.Julia Hans is in network?",
    "Bring me closets obg-yb in 32216 zipcode that in network",
    ("I live in FL. I am now visiting my Mom in Montana. If I see a pysciatrist here. Is it going to be covered by my insurance.")

]
@pytest.mark.parametrize("query",queries)
def test_answer_relevancy(query):

    output = health_chatbot(query)
    
    test_case= LLMTestCase(input=query, actual_output=output)
    metric = AnswerRelevancyMetric(threshold=0.8)
    assert_test(test_case,[metric])
   
    

 