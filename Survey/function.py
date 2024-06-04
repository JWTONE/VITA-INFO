import openai
from django.conf import settings

def survey(query):
    openai.api_key = settings.OPENAI_API_KEY

    model = "gpt-4-turbo"

    user_query = f'''
        "name": "{query.get('name')}",
        "gender": "{query.get('gender')}",
        "age": {query.get('age')},
        "height": {query.get('height')},
        "weight": {query.get('weight')},
        "current_medications_or_supplements": "{query.get('current_medications_or_supplements')}",
        "allergies": "{query.get('allergies')}",
        "exercise_frequency_per_week": "{query.get('exercise_frequency_per_week')}",
        "average_sleep_hours_per_day": "{query.get('average_sleep_hours_per_day')}",
        "smoking_status": "{query.get('smoking_status')}",
        "alcohol_consumption": "{query.get('alcohol_consumption')}",
        "average_meals_per_day": {query.get('average_meals_per_day')},
        "main_foods": "{query.get('main_foods')}",
        "snacks": "{query.get('snacks')}",
        "health_goals": "{query.get('health_goals')}",
        "interested_supplements": "{query.get('interested_supplements')}",
        "specific_health_issue_to_improve": "{query.get('specific_health_issue_to_improve')}"
    '''

    messages = [
        {"role": "system", "content": """
            너는 훌륭한 AI영양사야.
            각각 내용과 부연설명 해
            recommended_nutrients
            1. 
            2. 
            3.
            synergistic_nutrients
            1. 
            2. 
            3.
            antagonistic_nutrients
            1. 
            2. 
            3.
            alternative_foods
            1. 
            2. 
            3.
            incompatible_foods
            1. 
            2. 
            3.
            
            (이 아래는 절대 출력하지마)
            매우 중요: 사용자의 알레르기 정보, 현재 복용중인 약물이나 영양제,
            특별히 개선하고싶은 증상이나 건강문제, 혈관_혈액 순환을 반드시 고려해야 해.
            같이 섭취하면 좋은 영양소, 같이 섭취하면 안되는 영양소, 같이 섭취하면 안되는 음식은
            처음에 추천한 영양소와 반드시 연관되도록 해
            어떠한 경우에도 위의 폼대로 출력해
            반드시 python dictionary 형태로 key 값은 영어, value는 한글로 해서 줘
        """},
        {"role": "user", "content": user_query}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    answer = response['choices'][0]['message']['content']

    return answer
