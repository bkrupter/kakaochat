import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# Streamlit 앱 제목
st.title("챗GPT 기반 카카오톡 대화 분석기")

# 입력창: 사용자 질문/지시문
st.sidebar.title("사용자 입력")
user_input = st.sidebar.text_area("질문 또는 지시사항을 입력하세요", height=150)

# 버튼: OpenAI API 호출
if st.sidebar.button("분석 요청"):
    if user_input.strip() == "":
        st.error("질문 또는 지시사항을 입력해주세요!")
    else:
        # OpenAI API 호출
        try:
            with st.spinner("응답 생성 중... 잠시만 기다려주세요."):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "너는 사용자의 요청에 따라 카카오톡 대화를 분석하는 전문가 AI야."},
                        {"role": "user", "content": user_input},
                    ]
                )
                chat_response = response["choices"][0]["message"]["content"]
                st.success("분석 결과:")
                st.write(chat_response)
        except Exception as e:
            st.error(f"에러 발생: {str(e)}")

# 하단 설명
st.sidebar.info(
    """
    이 애플리케이션은 OpenAI GPT 모델을 기반으로 카카오톡 대화 내용을 분석합니다.
    사용자는 대화 파일을 업로드하거나 특정 질문을 입력하여 결과를 얻을 수 있습니다.
    """
)

st.sidebar.markdown("---")
st.sidebar.write("💡 **Tip:** Streamlit 애플리케이션 사용 중 문제가 있으면 새로고침하세요.")
