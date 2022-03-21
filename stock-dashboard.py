import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Finance Dashboard")

tickers = ('GOOGL','AMZN','TSLA','AAPL','MSFT','BTC-USD','ETH-USD','AAL','ACN','ADBE','TWTR','CTSH','INTU')

dropdown_menu = st.multiselect('Select assets', tickers)
start_date = st.date_input('Start', value=pd.to_datetime('2021-01-01'))
end_date = st.date_input('End', value=pd.to_datetime('today'))

def Returns(df):
    ret = df.pct_change()
    cumreturn = (1+ret).cumprod() - 1
    cumreturn = cumreturn.fillna(0)
    return cumreturn

if len(dropdown_menu) > 0:
    df = Returns(yf.download(dropdown_menu, start_date, end_date)['Adj Close'])
    st.header('Returns of {}'.format(dropdown_menu))
    st.line_chart(df)




