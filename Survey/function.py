import openai
from django.conf import settings

def survey(query):
    openai.api_key = settings.OPENAI_API_KEY
    model = "gpt-4-turbo"

    query = ''' 
        "name": "최진호",
        "gender": "여자",
        "age": 50,
        "height": 150,
        "weight": 50,
        "current_medications_or_supplements": "없음",
        "allergies": "집먼지 진드기 알레르기",
        "exercise_frequency_per_week": "3회",
        "average_sleep_hours_per_day": "5시간 이하",
        "smoking_status": "예",
        "alcohol_consumption": "6회 이상",
        "average_meals_per_day": 3,
        "main_foods": "채식 위주",
        "snacks": ["견과류"],
        "health_goals": ["피부 건강", "눈 건강"],
        "interested_supplements": ["오메가-3"],
        "specific_health_issue_to_improve": "탈모"
        "혈관_혈액 순환" : "상처가 잘 낫지 않아요, 손발 끝이 자주 저려요"
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
            결과를 json형식으로 반환해줘, key 값은 영어, value는 한글로 해
            """},
        {"role": "user", "content": query}
    ]


    response = openai.ChatCompletion.create(
        temperature=0,
        model=model,
        messages=messages
    )
    return response['choices'][0]['message']['content']

