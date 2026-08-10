import streamlit as st
import time

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
    # st.markdown("<h1 style='text-align: center; color: baby pink;'>As this little birthday card comes to an end, I just want to say one thing—I am truly grateful that someone as wonderful as you exists in my life. ❤️</h1>", unsafe_allow_html=True)
    # st.markdown("<h1 style='text-align: center; color: pink;'>Happy Birthday! 🎂💫You deserve all the happiness in the world. ❤️</h1>", unsafe_allow_html=True)
    
        
def reasons():
    with st.expander("💗 1000 Reasons I Need You"):
        
        reasons = [
        "Your little reactions",
        "Your random texts",
        "Your silly jokes",
        "Your honesty",
        "Your weirdness",
        "Your kindness",
        "Your curiosity",
        "Your smile",
        "Your laugh",
        "Your beautiful eyes",
        "Your voice",
        "Your good-morning messages",
        "Your good-night messages",
        "Your hugs",
        "Your presence",
        "Your patience",
        "Your adorable anger",
        "Your sleepy voice",
        "Your excitement",
        "Your confidence",
        "Your softness",
        "Your beautiful heart",
        "Your little habits",
        "Your compliments",
        "Your attention",
        "Your care",
        "Your support",
        "Your encouragement",
        "Your advice",
        "Your stories",
        "Your charm",
        "Your innocence",
        "Your creativity",
        "Your enthusiasm",
        "Your stubbornness",
        "Your teasing",
        "Your flirting",
        "Your voice notes",
        "Your photos",
        "Your selfies",
        'Your "hehe"',
        'Your "hmm"',
        'Your "okayyy"',
        "Your dramatic reactions",
        "Your tiny complaints",
        "Your random questions",
        "Your random thoughts",
        "Your late-night conversations",
        "Your morning conversations",
        "Your funny stories",
        "Your beautiful smile",
        "Your adorable laugh",
        "Your hugs after a bad day",
        "Your ability to cheer me up",
        "Your ability to make me smile",
        "Your ability to calm me down",
        "Your ability to make ordinary days special",
        "Your ability to make me blush",
        "Your ability to surprise me",
        "Your ability to understand me",
        "Your ability to annoy me cutely",
        "Your ability to make me miss you",
        "Because you make life sweeter",
        "Because you make me happier",
        "Because you make me laugh",
        "Because you make me feel special",
        "Because you make me feel understood",
        "Because you make me feel appreciated",
        "Because you make me feel lucky",
        "Because you make me feel loved",
        "Because you make me feel safe",
        "Because you're adorable",
        "Because you're precious",
        "Because you're irreplaceable",
        "Because you're unforgettable",
        "Because you're one of a kind",
        "Because you're my favorite person",
        "Because you're my favorite notification",
        "Because you're my favorite distraction",
        "Because you're my favorite conversation",
        "Because you're my favorite thought",
        "Because you're my favorite smile",
        "Because you're my favorite reason to smile",
        "Because you're my favorite goodnight",
        'Because you ask "what are you doing?"',
        "Because you're my favorite person to annoy",
        "Because you're my favorite person to tease",
        "Because you're my favorite person to miss",
        "Because you're simply you",
        "Because you make me feel complete",
        "Because you bring peace to my chaos",
        "Because you make silence comfortable",
        "Because you make conversations endless",
        "Because you understand my weird side",
        "Because you accept my flaws",
        "Because you know how to make me laugh",
        "Because you know when I need comfort",
        "Because you respect me",
        "Because you appreciate me",
        "Because you inspire me",
        ]
        
        reason_placeholder = st.empty()
        for i, reason in enumerate(reasons, start=1):
            reason_placeholder.markdown(
            f"""
            <div style="
                text-align: center;
                padding: 20px;
                font-size: 24px;
                color: #ff4b6e;
                font-weight: bold;
            ">
                💗 Reason #{i} 💗
                <br><br>
                {reason}
            </div>
            """,
            unsafe_allow_html=True
            )
            
            time.sleep(0.5)  

        st.markdown("---")
        reason_placeholder.markdown(
        """
        <div style="
            text-align: center;
            padding: 30px;
            font-size: 28px;
            color: #ff4b6e;
            font-weight: bold;
        ">
            💕 And after all 1000 reasons... 💕
            <br><br>
            There are probably a million more reasons I could write.
            <br><br>
            But if I had to choose just one...
            <br><br>
            ❤️ I need you because you're YOU. ❤️
            <br><br>
            🥹💗
        </div>
        """,
        unsafe_allow_html=True
        )
        st.markdown("<h3 style='text-align: center; color: pink;'>❤️ I don't need 1000 reasons to need you. I just need one—you make my world a little happier by standing by me. 🎉🎂🎁</h3>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: baby pink;'>As this little birthday card comes to an end, I just want to say one thing—I am truly grateful that someone as wonderful as you exists in my life. ❤️</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: pink;'>Happy Birthday! 🎂💫You deserve all the happiness in the world. ❤️</h1>", unsafe_allow_html=True)
    

def check_plans():
    bool2=False
    check=st.button("Let's Check today plans")
    if check:
        bool2=True
        
        #Staring the 2nd while loop to check the plans for today
    while bool2:
        st.markdown("<h3 style='text-align: center; color: pink;'>Tamluk</h3>", unsafe_allow_html=True)
        st.write("See you at the temple at 08:00 AM")
        st.image("https://thumbs.dreamstime.com/b/bargabhima-temple-courtyard-golden-domes-devotees-tamluk-west-bengal-india-medinipur-august-view-historic-398908606.jpg", 
                 caption="Bargabhima Temple, Tamluk")
                
        st.data_editor(
                data={
                    "Time": ["08:00 AM",  "10:00 AM"],
                    "Activity": ["Temple Visit", "Return Home"]
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
    reasons()
    # check_plans()
    
    
       
        
     
if __name__ == "__main__":
    main()

