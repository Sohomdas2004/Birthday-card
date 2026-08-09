import streamlit as st

def birthday_wish():
    bool1=False
    start=st.button("Start the Magic")
    if start:
        bool1=True
        
    #Writing all the code for the app in a while loop to keep it running until the user closes the app
    while bool1:
        st.write("🎉🎂🎁")
        st.balloons()
        st.success("Let's celebrate your special day! 🎉🎂🎁")
        st.markdown("<h1 style='text-align: center; color: pink;'>Happy Birthday! 🎉🎂🎁</h1>", unsafe_allow_html=True)
        st.write("""
                     I hope your day is filled with happiness, laughter, beautiful moments, and 
                     everything your heart wishes for. Thank you for always being such an amazing 
                     person and for bringing so much positivity into my life. Stay happy, keep smiling, 
                     and have the most wonderful birthday! 🥳🎉💖
                     """)
        bool1=False
    
def check_plans():
    bool2=False
    check=st.button("Let's Check today plans")
    if check:
        bool2=True
        
        #Staring the 2nd while loop to check the plans for today
    while bool2:
        col1, col2 = st.columns(2)
        with col1:
            st.header("Tamluk")
            st.write("See you at the temple at 10:00 AM")
            st.image("https://thumbs.dreamstime.com/b/bargabhima-temple-courtyard-golden-domes-devotees-tamluk-west-bengal-india-medinipur-august-view-historic-398908606.jpg", 
                     width=300)
                    
        with col2:
            st.header("Haldia")
            st.write("After the temple visit, we will go to Haldia")
            st.image("https://i.ytimg.com/vi/sioPVFIqyJ0/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGDwgZSgsMA8=&rs=AOn4CLDkOqYYfLCTYvHtCRIZgPI1YBClqQ", 
                     width=400)
        st.data_editor(
                data={
                    "Time": ["10:00 AM",  "1:00 PM", "02:00 PM", "05:00 PM"],
                    "Activity": ["Temple Visit",  "Lunch at The Temple", "Going to Haldia", "Return Home"]
                },
                column_config={
                    "Time": st.column_config.TextColumn("Time"),
                    "Activity": st.column_config.TextColumn("Activity")
                },
                hide_index=True,
                key="plans"
            )

            
            
        bool2=False
 
def main():
    #This is the page cofiguration for the streamlit app
    st.set_page_config(
    page_title="Birthday Magic 🎂",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
    )
    st.title("🎉🎂🎁 Birthday Magic 🎁🎂🎉")
    st.write("Welcome to the Birthday Magic! Let's make your special day even more magical! 🎉🎂🎁")
    birthday_wish()
    #st.write("Now, let's check the plans for today! 🗓️")
    check_plans()
       
        
     
if __name__ == "__main__":
    main()

