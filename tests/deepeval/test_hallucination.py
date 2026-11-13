from dotenv import load_dotenv
load_dotenv()
from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric
from app.health_chatbot import health_chatbot


def test_hallucination_metrics():
    query = "Can you confirm if our health plan covers the new FDA-approved drug 'Glucoril-X' for Type 2 diabetes, and what the exact copay tier is?"
    output = health_chatbot(query)
    print(output)

    context=[
        "Maximum out of pocket amount is $1000",
        "Out of pocket amount restart end end each year"
    ]

    test_case = LLMTestCase(
        input = query,
        actual_output= output,
        context = context
    )
    hal_metric = HallucinationMetric(threshold=0.8)

    result = evaluate([test_case],[hal_metric])

    print(result)
    

    #$env:PYTHONPATH="."
#deepeval test run tests\deepeval\test_hallucination.py2wsx