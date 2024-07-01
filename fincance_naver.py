import pandas as pd
import matplotlib.pyplot as plt
import warnings
import streamlit as st

warnings.filterwarnings('ignore')   # warning 무시
plt.rc('font', family='Malgun Gothic')  # font 변경

def Get_Exchange_Rate_Data(name, code, page):
    df = pd.DataFrame()

    for page_num in range(1, page+1):
            base_url = f'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{code}KRW&page={page_num}'
            temp = pd.read_html(base_url, encoding='cp949', header=1)
            
            df = pd.concat([df, temp[0]])
    
    return Total_Rate_Data_View(name, code, df)

def Total_Rate_Data_View(name, code, df):
    # 원하는 열만 선택
    df_total = df[['날짜', '매매기준율', '사실 때', '파실 때', '보내실 때', '받으실 때']]

    # 데이터 표시
    st.subheader(f'=== [{name}({code})] ===')
    st.dataframe(df_total.head(20))

    # 차트 작성
    df_total_chart = df_total.copy()    # origin data save & copy another
    df_total_chart = df_total_chart.set_index('날짜')   # index setting

    df_total_chart = df_total_chart[::-1]    # 역순으로 slicing
    ax = df_total_chart['매매기준율'].plot(figsize=(15, 6), title=f'exchange rate: {code}')  # figsize = inch
    fig = ax.get_figure()
    st.pyplot(fig)

    return df_total
    #Month_Rate_Data_View(name, df_total)

def Month_Rate_Data_View(name, month_in, df):
     # str(column내 전체 바꿈), replace("">""), astype('type')
    df['날짜'] = df['날짜'].str.replace(".","").astype('datetime64[ms]')
    df['월'] = df['날짜'].dt.month
    month_in = st.selectbox('SELECT MENU', [1,2,3,4,5,6,7,8,9,10,11,12], index=0)
    month_df = df.loc[df['월']==month_in, ['날짜', '매매기준율', '사실 때', '파실 때', '보내실 때', '받으실 때']]

    month_df_chart = month_df.copy()
    month_df_chart = month_df_chart[::-1].reset_index(drop=True)  # drop: 기존 정보 삭제 여부

    st.subheader(f'=== [{name}] ({month_in}월) ===')
    st.dataframe(month_df_chart)

    month_df_chart = month_df_chart.set_index('날짜')
    ax = month_df_chart['매매기준율'].plot(figsize=(15, 6))

    fig = ax.get_figure()
    st.pyplot(fig)

# input 입력값 = string
def exchange_main():
    dic_currency_name_symbol = {'미국 달러 / $':'USD', '유럽연합 유로 / €':'EUR', '일본 엔(100) / ¥':'JPY', '중국 위안 / ¥':'CNY'}
    
    name = st.selectbox('통화유형 선택', dic_currency_name_symbol.keys())
    code = dic_currency_name_symbol[name]
    page = 5

    clicked = st.button('SEARCH')
    if clicked :
        df_origin_exchange = Get_Exchange_Rate_Data(name, code, page)

# if __name__=="__main__":
#      exchange_main()
