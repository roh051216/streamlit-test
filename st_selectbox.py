import streamlit as st

st.title('st.form')

st.header('')
st.subheader('커피 머신')
with st.form('my_form'):
    st.subheader("***커피 주문하기***")

    coffee_bean_val = st.select_box('커피콩',['아라비카','로부스터'])
    coffee_roast_val = st.select_box('커피 로스팅',['라이트','미디엄','다크'])
    brewing_val = st.select_box('추출 방법',['에어로프레스','드랍','프렌치 프레스','모카 포트','사이폰'])
    
    serving_type_val = st.select_box('서빙 형식',['힛','아이스','프라페'])
    milk_val = st.select_slider('우유 강도',['없음','낮음','중간','높음'])
    owncup_val = st.check_box('자신의 컵 가져오기')
    submitted = st.form_submit_button('제출')
if submitted:
    st.markdown(f'''
                주문하신 내용:
                -커피콩: '{coffee_bean_val}'
                -커피 로스팅 : '{coffee_roast_val}'
                -추출 방밥 : '{brewing_val}'
                -서빙 형식 : {serving_type_val}'
                -우유 : '{milk_val}'
                -자신의 컵 가져오기: '{owncup_val}'
                ''')

else:
    st.write('¶ 주문하세요 ! ')
    
option = st.select_box(
     '가장 좋아하는 색상은 무엇인가요?',
     ('파랑', '빨강', '초록'))

st.write('당신이 좋아하는 색상은 ', option)
