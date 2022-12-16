import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Joseph Biancamano",  
    layout="wide")


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Blog", "Contact"],
        icons=["house", "book","pencil-square" ,"envelope"],
        default_index=0,
       
    )
   
if selected == "Home":
    st.markdown(""" <style> .font {
    font-size:20px ;
    font-family: 'MERRIWEATHER';
    }
    </style> """, unsafe_allow_html=True)
        # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.write('')
        st.write('')
        st.image('/Users/josephbiancamano/Downloads/jport2.png')

    with col2:
        st.title("Joseph Biancamano")
        st.write("Passionate about finance and blockchain. Constantly focused on learning, improving, and innovating. Eager to analyze financial markets and data using Python! I am driven and detail oriented indivdual with the ability to thrive in high pressure enviroments.   Main areas of interest include derivatives and decentralized finance.")           
        
    col1,col2,col3 = st.columns(3)
    with col1:
        st.title("[GitHub](https://github.com/webn3ewbie)")
    with col2:
        st.title("[LinkedIn ](https://www.linkedin.com/in/joseph-biancamano/)")
    with col3:
        st.title("[Twitter ](https://twitter.com/DirtyDefi)")
        
    with st.container():
        st.write("---")
        st.header("About Me")
        st.write("##")
        st.markdown('<p class="font"> I am a determined and enthusiastic indivdual with a passion for financial market and blockchain. recognized for bringing strategic perspective to projects and tool development. Team leader, able to inspire others to deliver solutions in a collaborative way. Highly productive with a passion for learning and applying new skills to improve project outcomes. Known for the ability to identify relevant issues and develop alternate paths to proceed. Strengths include: Achiever, Learner, Focus, Strategic, Futuristic.</p>',unsafe_allow_html=True)
        st.markdown('<p class="font"> I am  driven and detail oriented indivdual with the ability to thrive in high pressure enviroments</p>',unsafe_allow_html=True)
        st.markdown('<p class="font"> I am skilled in Python, with an emphasis in Pandas, Numpy, and Streamlit. I am an active learner, currently studying machine learning, algorithms, and blockchain.</p>',unsafe_allow_html=True)
        st.markdown('<p class="font">I enjoy furthering my knowledge and experience in financial analytics. Current passions are time series analysis andextracting data insights through statistical techniques and quantitative methods that enhance decision-making and drive competitive growth.</p>',unsafe_allow_html=True)
        st.markdown('<p class="font"> I am seeking a position where I can use my skills to add business value and contribute to the success of my team. Eager to connect with you to learn more about what I can do to provide data-centric solutions for your organization.</p>',unsafe_allow_html=True) 
                       
# Projects
   
if selected == "Projects":
    
    
# NFA
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.markdown(""" <style> .font {
            font-size:20px ;
            font-family: 'MERRIWEATHER';
            }
            </style> """,
                        unsafe_allow_html=True)
        
       
        st.subheader("[Openbb x Streamlit Financial Dashboard](https://openbb.streamlit.app/)")
        components.iframe("https://openbb.streamlitapp.com/?embedded=true",height =500)
        st.markdown('<p class="font"> Simple financial dashboard powered by OpenBB and Streamlit. App displays stocks, bonds, currencies, cryptos, indices, and alt economic data all in one place! Furthermore the app provides data to the latest trades by members of congress, latestest government contracts for companies </p>',unsafe_allow_html=True)
        st.markdown('<p class="font"> Some Libraries used:  streamlit, pandas, datetime, matplotlib, plotly, Openbb </p>',unsafe_allow_html=True)
        st.subheader("[GitHub Repo ](https://github.com/webn3ewbie/OpenBBxStreamlit)")


        
    with st.container():
            st.subheader("[ExtractAlpha](https://equities.streamlit.app)")
            components.iframe("https://equities.streamlitapp.com/?embedded=true",height =500)
            st.markdown('<p class="font"> ExtractAlpha is an open-source Streamlit app built specifically to analyze equities, bonds, commodities, currencies, and cryptos. ExtractAlpha supports any asset available on YahooFinance.com. ExtractAlpha consists of multiple unique dashboards that feature Asset Returns, Asset Price Comparisons, Asset Price Predictions, Monte Carlo Simulation, and Equity Fundamental Analysis. The Asset Price Prediction leverages Facebook Prophet to predict prices up to 5 years in the future. The model is trained from data of the assets daily opening and closing price based on the time period entered by the user. Select a dashboard and see what ExtractAlpha can do! </p>',unsafe_allow_html=True)
            st.markdown('<p class="font"> Some Libraries used: streamlit, datetime, pandas, plotly, prophet, numpy, seaborn, scipy, yfinance </p>',unsafe_allow_html=True)
            st.subheader("[GitHub Repo ](https://github.com/webn3ewbie/Streamlit-Asset-Analysis-Prediction-App)")

   
    with st.container():
            st.subheader("[MACRO Terminal](https://macroquant.streamlit.app/)")
            components.iframe("https://macroquant.streamlitapp.com/?embedded=true",height =500)
            st.markdown('<p class="font"> MACRO Terminal is an open-source Streamlit app built specifically to analyze equities, bonds, commodities, and currencies. MACRO Terminal leverages the FRED API, which allow users to analyze a wide ranging number of macro datasets. MACRO Terminal consists of multiple unique dashboards that feature Overall Economic Activity, Labor Markets, Fed Tools, Inflation, Volatility, Commodities, and Recession Risks. Select a dashboard and see what MACRO Terminal can do! </p>',unsafe_allow_html=True) 
            st.markdown('<p class="font"> Some Libraries used: streamlit, pandas, FRED API, </p>',unsafe_allow_html=True)   
            st.subheader("[GitHub Repo](https://github.com/webn3ewbie/Economic-Data-Terminal)")
            
    with st.container():
             st.subheader("[DEFI Terminal](https://decentralizedfinance.streamlit.app/)")
             components.iframe("https://decentralizedfinance.streamlitapp.com/?embedded=true",height =500)
             st.markdown('<p class="font"> DEFI Terminal is an open-source Streamlit app built specifically to analyze the crypto market. DEFI Terminal allows you to analyze thousands of protocols and pools. DEFI Terminal is powered by Defi Llama. DEFI Terminal consists of multiple dashboards that feature Total Value Locked vs Protocol Market Cap, Top Protocols by Category, and Pools APY. Select a dashboard and see what DEFI Terminal can do! </p>',unsafe_allow_html=True) 
             st.markdown('<p class="font"> Some Libraries used: streamlit, pandas, numpy, plotly, DefiLlama </p>',unsafe_allow_html=True)   
             st.subheader("[GitHub Repo](https://github.com/webn3ewbie/defiterm)")
             
    with st.container():
              st.subheader("[Crypto Historical Investment Calculator](https://bitcoins.streamlit.app/)")
              components.iframe("https://bitcoins.streamlitapp.com/?embedded=true",height =500)
              st.markdown('<p class="font"> This calculator allows you to explore how much a hypothetical historical investment in crypto assests would be worth today! </p>',unsafe_allow_html=True) 
              st.markdown('<p class="font"> Some Libraries used: streamlit, pandas, pycoingecko, datetime </p>',unsafe_allow_html=True)   
              st.subheader("[GitHub Repo](https://github.com/webn3ewbie/crypto-investment-backtest)")
              st.write('Yes, you probably guessed it, my favorite color is red :)')


if selected == "Blog":
    
    

    with st.container():
        st.header("[Blog Hosted On Blockchain](https://mirror.xyz/0x05721B0aD76eC33DefB59Abd613E30FbF4b4127C)")
        st.markdown(""" <style> .font {
            font-size:20px ;
            font-family: 'MERRIWEATHER';
            }
            </style> """,
                        unsafe_allow_html=True)
        
       
       
        components.iframe("https://mirror.xyz/0x05721B0aD76eC33DefB59Abd613E30FbF4b4127C/?embedded=true",height=1000)
        
######################
# Contact
######################    
if selected == "Contact":   
    st.header(":mailbox: Get In Touch With Me!")
    st.write("Please use this for business and collaboration purposes. I love to talk anything financial markets, blockchain, and programming. However please shoot me a DM on [twitter](https://openbbx.streamlit.app/) for those chats!")
    contact_form = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""
