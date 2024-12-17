import streamlit as st
import matplotlib.pyplot as plt
import matplotlib  # 글씨 깨짐 해결을 위해 추가
from matplotlib import rc

from PIL import Image
rc('font', family='Malgun Gothic')  # Windows 환경에서 'Malgun Gothic' 사용
plt.rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지

# 페이지 구성
st.set_page_config(page_title="편의점에서 물건 구매하기", layout="wide")

# 선택 메뉴
page = st.sidebar.selectbox(
    "페이지를 선택하세요", 
    ["수업 소개", "편의점 지도", "예산 확인", "마트 예절", "물건 구매", "구매 성공"]
)

if page == "수업 소개":
    # 첫 번째 페이지: 수업 소개
    st.title("편의점에서 물건 구매하기")
    st.write(
        """
        이 수업은 학생들이 실제 편의점에서 물건을 구매하며 필요한 사회적 기술과 
        계산 능력을 익히는 것을 목표로 합니다.
        """
    )

    # 로컬 이미지 불러오기
    image_path = "C:/Users/User/Downloads/물건구매_그림/서울경운학교.png"  # 경운학교 사진 경로
    image = Image.open(image_path)

    # 이미지 출력
    st.image(image, caption="서울경운학교", width=600)

    # 수업 목표
    st.subheader("수업 목표")
    st.write(
        """
        - 실제 생활에서 필요한 금전 관리 기술을 배웁니다.
        - 타인과의 대화 및 기본적인 예의 표현을 익힙니다.
        - 물건을 선택하고 계산하는 과정에서 의사결정을 연습합니다.
        """
    )

elif page == "편의점 지도":
    # 두 번째 페이지: 네이버 지도
    st.title("종로3가역 주변 편의점 검색")
    st.write("아래에 종로3가역 주변 편의점 검색 결과를 표시합니다. 네이버 지도에서 자세히 확인할 수 있습니다.")
    naver_maps_url = (
        "https://map.naver.com/v5/search/%EC%A2%85%EB%A1%9C3%EA%B0%80%EC%97%AD%20%ED%8E%B8%EC%9D%98%EC%A0%90"
    )
    st.components.v1.iframe(naver_maps_url, width=1600, height=1200)

elif page == "예산 확인":
    # 세 번째 페이지: 예산 확인
    st.title("예산 확인")
    st.write("현재 예산은 총 **10,000원**입니다. 아래에서 예산을 다양한 형태로 확인할 수 있습니다.")

    # 예산 그림 표현
    st.subheader("예산 구성")

    # 로컬 이미지 파일 경로 설정
    image_10000 = "C:/Users/User/Downloads/물건구매_그림/만원.jpg"
    image_5000 = "C:/Users/User/Downloads/물건구매_그림/오천원.jpg"
    image_1000 = "C:/Users/User/Downloads/물건구매_그림/천원.jpg"

    # 만원 한 장
    st.write("- 10,000원 한 장")
    image = Image.open(image_10000)
    st.image(image, width=200, caption="10,000원")

    # 오천원 두 장
    st.write("- 5,000원 두 장")
    image = Image.open(image_5000)
    st.image(image, width=200, caption="5,000원 X 2")
    st.image(image, width=200)

 
    # 오천원 한 장과 천원 다섯 장
    st.write("- 5,000원 한 장과 1,000원 다섯 장")
    image_5000 = Image.open(image_5000)
    image_1000 = Image.open(image_1000)
    st.image(image_5000, width=200, caption="5,000원 X 1")
    cols = st.columns(5)
    for col in cols:
        col.image(image_1000, width=200)

    st.write("예산은 각 페이지에서 구매할 때 고려하세요!")

elif page == "마트 예절":
    # 네 번째 페이지: 마트 예절
    st.title("마트에서 지켜야 할 예절")
    st.write("마트에서 물건을 구매할 때 지켜야 할 기본적인 예절을 배워봅시다!")

    st.subheader("1. 줄을 설 때")
    st.write("다른 사람을 밀거나 끼어들지 않고 차례대로 줄을 섭니다.")

    st.subheader("2. 물건을 고를 때")
    st.write(
        """
        - 필요 없는 물건은 함부로 만지지 않습니다.
        - 원래 자리에 있던 물건은 다시 제자리에 놓습니다.
        """
    )

    st.subheader("3. 계산할 때")
    st.write(
        """
        - 계산대에서 점원에게 밝고 친절하게 인사합니다.
        - 돈을 정확히 계산하고 차례를 기다립니다.
        """
    )

    st.subheader("4. 주변 사람들에게")
    st.write(
        """
        - 조용히 행동하며 소리를 지르지 않습니다.
        - 다른 사람의 물건을 만지지 않습니다.
        """
    )

    # 로컬 이미지 사용
    image_path = "C:/Users/User/Downloads/물건구매_그림/마트예절.png"  # 이미지 파일 경로
    image = Image.open(image_path)
    
    st.image(image, caption="마트에서 예절을 지키는 모습", width=1000)

elif page == "물건 구매":
    # 다섯 번째 페이지: 물건 구매 시뮬레이터
    st.title("물건 구매 시뮬레이터")
    st.write(
        """
        **목표**: 예산을 초과하지 않도록 물건을 구매하세요!  
        총 합계가 10,000원을 넘으면 실패입니다.
        """
    )

    # 물품 리스트와 가격 및 이미지
    items = {
    "가나초콜릿": (2000, "C:/Users/User/Downloads/물건구매_그림/가나초콜릿.png"),
    "코카콜라": (2500, "C:/Users/User/Downloads/물건구매_그림/코카콜라.png"),
    "지우개": (1000, "C:/Users/User/Downloads/물건구매_그림/지우개.jpg"),
    "부루마블": (9000, "C:/Users/User/Downloads/물건구매_그림/부루마블.jpg"),
    "서울우유": (1500, "C:/Users/User/Downloads/물건구매_그림/서울우유.png"),
    "필통": (4000, "C:/Users/User/Downloads/물건구매_그림/필통.jpg"),
    "허니버터칩": (3000, "C:/Users/User/Downloads/물건구매_그림/허니버터칩.jpg"),
    "귤": (1000, "C:/Users/User/Downloads/물건구매_그림/귤.jpg"),
    "바나나": (1500, "C:/Users/User/Downloads/물건구매_그림/바나나.jpeg"),
}

    # 페이지 레이아웃: 왼쪽에 물품 선택, 오른쪽 위에 막대그래프
    col1, col2 = st.columns([3, 1])

    # 물품 선택 (왼쪽)
    with col1:
        st.subheader("구매할 물건을 선택하세요:")
        selected_items = []

        for item, (price, img_url) in items.items():
            with st.container():
                sub_col1, sub_col2 = st.columns([1, 5])
                with sub_col1:
                    st.image(img_url, width=200)
                with sub_col2:
                    if st.checkbox(f"{item} - {price}원", key=item):
                        selected_items.append(item)
        # 구분선 추가
            st.markdown("---")

    # 합계 계산
    total = sum(items[item][0] for item in selected_items)

    # 막대그래프 (오른쪽)
    with col2:
        st.subheader("예산 비교")
        fig, ax = plt.subplots(figsize=(3, 4))
        colors = ["green" if total <= 10000 else "red"]
        bars = ax.bar(["현재 금액"], [total], color=colors)

        # 예산선 추가
        ax.axhline(10000, color="blue", linestyle="--", label="예산 (10,000원)")
        ax.set_ylim(0, 15000)
        ax.set_title("예산 비교")
        ax.legend()

        # 막대 안에 숫자 추가
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, f"{height}원", ha="center", va="bottom")

        st.pyplot(fig)

    # 현재 선택한 물품 및 총 금액 표시 (아래)
    st.write(f"현재 선택한 물품: {', '.join(selected_items) if selected_items else '선택한 물품이 없습니다.'}")
    st.write(f"총 구매 금액: **{total}원**")

    # 구매 버튼
    if st.button("구매"):
        if total > 10000:
            st.error("예산 초과! 구매 실패입니다.")
        elif total > 0:
            st.success("구매 성공! 칭찬 페이지로 이동합니다.")
            # 세션 상태 업데이트 및 이동
            st.session_state["selected_items"] = selected_items
            st.session_state["total"] = total
            st.experimental_set_query_params(page="구매 성공")
        else:
            st.warning("물건을 선택하지 않았습니다.")


elif page == "구매 성공":
    # 여섯 번째 페이지: 구매 성공
    st.title("구매 성공!")
    st.write("축하합니다! 예산 내에서 성공적으로 물건을 구매했습니다.")
    
    # 로컬 이미지 경로 설정 및 불러오기
    image_path = "C:/Users/User/Downloads/물건구매_그림/참잘했어요.png"  # 로컬 이미지 경로
    image = Image.open(image_path)

    # 이미지 출력
    st.image(image, caption="잘했어요! 🎉", width=800)

    if "selected_items" in st.session_state and "total" in st.session_state:
        st.write(f"구매한 물품: {', '.join(st.session_state['selected_items'])}")
        st.write(f"총 금액: {st.session_state['total']}원")
    if st.button("다시 구매하기"):
        # 세션 상태 초기화 및 이동
        st.session_state.clear()
        st.experimental_set_query_params(page="물건 구매")



        


## streamlit run "C:/Users/User/Downloads/test_app.py"