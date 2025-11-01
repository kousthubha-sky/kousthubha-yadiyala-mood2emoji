import streamlit as st
from textblob import TextBlob
import re

# Bad words filter (basic list - extend as needed)
BAD_WORDS = ['hate', 'stupid', 'idiot', 'dumb', 'shut up']

def contains_bad_words(text):
    """Check if text contains filtered words"""
    text_lower = text.lower()
    for word in BAD_WORDS:
        if word in text_lower:
            return True
    return False

def analyze_mood(text):
    """
    Analyze text mood using TextBlob polarity
    Returns: emoji, explanation, polarity_score
    """
    if not text.strip():
        return "😐", "Please type something!", 0.0
    
    # Safety check
    if contains_bad_words(text):
        return "😐", "Let's keep our words kind and respectful!", 0.0
    
    # Use TextBlob for sentiment analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Map polarity to emoji and explanation
    if polarity > 0.1:
        emoji = "😀"
        explanation = "Sounds happy and positive!"
    elif polarity < -0.1:
        emoji = "😞"
        explanation = "Sounds a bit sad or negative."
    else:
        emoji = "😐"
        explanation = "Sounds neutral or calm."
    
    return emoji, explanation, polarity

def show_teacher_mode():
    """Display how the app works for teachers"""
    st.markdown("### 🎓 Teacher Mode: How It Works")
    
    # Visual flow diagram
    st.markdown("#### 📊 Flow Diagram")
    st.markdown("""
    ```
    ┌─────────────────────┐
    │  User types text    │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │  Is text empty?     │───Yes──→ Show "Please type something!"
    └──────────┬──────────┘
               │ No
               ▼
    ┌─────────────────────┐
    │ Contains bad words? │───Yes──→ Show 😐 "Keep words kind!"
    └──────────┬──────────┘
               │ No
               ▼
    ┌─────────────────────┐
    │ TextBlob Analysis   │
    │ Calculate Polarity  │
    │   (-1.0 to +1.0)    │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ Polarity > 0.1?     │───Yes──→ 😀 "Sounds happy!"
    └──────────┬──────────┘
               │ No
               ▼
    ┌─────────────────────┐
    │ Polarity < -0.1?    │───Yes──→ 😞 "Sounds sad!"
    └──────────┬──────────┘
               │ No
               ▼
           😐 "Sounds neutral!"
    ```
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **The app follows these steps:**
    
    1. **Input Check**: First, we make sure the text isn't empty
    2. **Safety Filter**: We check for unkind words and reject them
    3. **Sentiment Analysis**: We use TextBlob to analyze the mood
       - TextBlob gives us a *polarity score* between -1 and +1
       - Negative = sad, Positive = happy, Near zero = neutral
    4. **Emoji Selection**: Based on the score, we pick an emoji
       - Score > 0.1 → 😀 Happy
       - Score < -0.1 → 😞 Sad
       - Score in between → 😐 Neutral
    5. **Kid-Friendly Explanation**: We show simple feedback
    
    **Example Scores:**
    - "I love pizza!" → Polarity: +0.5 (positive)
    - "I feel okay." → Polarity: 0.0 (neutral)
    - "This is terrible." → Polarity: -1.0 (negative)
    """)
    
    st.info("💡 **Teaching Tip**: Have students try different sentences and guess the emoji before seeing the result!")

# Main App
def main():
    st.set_page_config(page_title="Mood2Emoji", page_icon="😀")
    
    st.title("😀 Mood2Emoji Detector")
    st.markdown("*Type a sentence and discover its mood!*")
    
    # Sidebar for Teacher Mode
    with st.sidebar:
        st.header("Settings")
        teacher_mode = st.checkbox("🎓 Teacher Mode", help="Show how the app works")
    
    # Main input
    user_text = st.text_input(
        "Enter your sentence:",
        placeholder="E.g., I'm excited about the science fair!",
        max_chars=200
    )
    
    # Analyze button
    if st.button("🔍 Detect Mood", type="primary"):
        if user_text:
            emoji, explanation, score = analyze_mood(user_text)
            
            # Display results
            st.markdown("---")
            col1, col2 = st.columns([1, 3])
            
            with col1:
                st.markdown(f"<h1 style='text-align: center;'>{emoji}</h1>", 
                          unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"### {explanation}")
                if teacher_mode:
                    st.caption(f"*Polarity Score: {score:.2f}*")
            
            st.markdown("---")
        else:
            st.warning("⚠️ Please enter a sentence first!")
    
    # Show teacher mode if enabled
    if teacher_mode:
        st.markdown("---")
        show_teacher_mode()
    
    # Fun examples section
    with st.expander("💡 Try These Examples"):
        st.markdown("""
        - "I aced my math test!"
        - "The weather is okay today."
        - "I'm feeling down about the game."
        - "Science class was amazing!"
        - "I don't know how I feel."
        """)
    
    # Footer
    st.markdown("---")
    st.caption("🎓 Built for learning about AI and text analysis | Ages 12-16")

if __name__ == "__main__":
    main()