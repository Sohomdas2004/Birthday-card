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
        st.snow()
        st.success("Let's celebrate your special day! 🎉🎂🎁")
        st.markdown("<h1 style='text-align: center; color: pink;'>Happy Birthday! 🎉🎂🎁</h1>", unsafe_allow_html=True)
        st.write("""
                     I hope your day is filled with happiness, laughter, beautiful moments, and 
                     everything your heart wishes for. Thank you for always being such an amazing 
                     person and for bringing so much positivity into my life. Stay happy, keep smiling, 
                     and have the most wonderful birthday! 🥳🎉💖
                     """)
        bool1=False
        

def message():
    st.write("🎉🎂🎁")
    st.write("""
             And one last little confession… 🙈❤️

                I honestly **can not wait to see you today!** 🥰
                I have been waiting for this day, and I have a feeling that seeing you in person is going to be my favorite part of it. 💕

                So please come soon… because this birthday girl has someone very excited to see her. 😏✨

                Now hurry up! I am running out of patience… and I am blaming you for it. 😂❤️

                **Happy Birthday, beautiful! 🎂💖**

                """)
    st.markdown("<h1 style='text-align: center; color: baby pink;'>As this little birthday card comes to an end, I just want to say one thing—I am truly grateful that someone as wonderful as you exists in my life. ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: pink;'>Happy Birthday! 🎂💫You deserve all the happiness in the world. ❤️</h1>", unsafe_allow_html=True)
    

def check_plans():
    bool2=False
    check=st.button("Let's Check today plans")
    if check:
        bool2=True
        
        #Staring the 2nd while loop to check the plans for today
    while bool2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h3 style='text-align: center; color: pink;'>Tamluk</h3>", unsafe_allow_html=True)
            st.write("See you at the temple at 10:00 AM")
            st.image("https://thumbs.dreamstime.com/b/bargabhima-temple-courtyard-golden-domes-devotees-tamluk-west-bengal-india-medinipur-august-view-historic-398908606.jpg", 
                     )
                    
        with col2:
            st.markdown("<h3 style='text-align: center; color: pink;'>Haldia</h3>", unsafe_allow_html=True)
            st.write("After the temple visit")
            st.image("https://i.ytimg.com/vi/sioPVFIqyJ0/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGDwgZSgsMA8=&rs=AOn4CLDkOqYYfLCTYvHtCRIZgPI1YBClqQ", 
                     )
        st.data_editor(
                data={
                    "Time": ["10:00 AM",  "1:00 PM", "02:00 PM", "05:00 PM"],
                    "Activity": ["Temple Visit",  "Lunch at The Temple", "Haldia Township", "Return Home"]
                },
                column_config={
                    "Time": st.column_config.TextColumn("Time"),
                    "Activity": st.column_config.TextColumn("Activity")
                },
                hide_index=True,
                key="plans"
            )

        message()
            
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

