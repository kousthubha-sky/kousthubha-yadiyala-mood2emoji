# 😀 Mood2Emoji: Kid-Safe Text-Mood Detector

A simple, educational web app that helps students (ages 12-16) understand how computers can detect emotions in text. Built with Python, Streamlit, and TextBlob.

## 🎯 What Does This Do?

Mood2Emoji takes a sentence you type and tells you if it sounds happy 😀, neutral 😐, or sad 😞. It's a beginner-friendly introduction to:
- **Natural Language Processing (NLP)**: Teaching computers to understand human language
- **Sentiment Analysis**: Detecting emotions in text
- **AI Safety**: Building responsible technology that's appropriate for young users

## 🚀 Quick Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd mood2emoji
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download TextBlob data** (one-time setup)
```bash
python -m textblob.download_corpora
```

4. **Run the app**
```bash
streamlit run app.py
```

5. **Open your browser** to `http://localhost:8501`

## 📚 How Kids Learn From This

### Key Learning Outcomes
1. **AI Fundamentals**: Students see how computers analyze text (not magic!)
2. **Sentiment Analysis**: Understanding that words carry emotional weight
3. **Polarity Scores**: Numbers can represent feelings (-1 to +1 scale)
4. **Responsible AI**: Why filtering inappropriate content matters
5. **Cause & Effect**: Different words → different results

### Hands-On Discovery
- Students type sentences and immediately see results
- "Teacher Mode" reveals the logic behind the scenes
- Trial and error helps them understand patterns
- Safe environment for experimentation

## 🎓 Teaching This in 60 Minutes

### Lesson Structure

**Phase 1: Introduction (10 minutes)**
- Demo the app with fun examples
- Ask: "How do you think computers understand feelings?"
- Explain the concept of sentiment analysis in simple terms

**Phase 2: Hands-On Exploration (15 minutes)**
- Students try the app with their own sentences
- Challenge: Find sentences that give each emoji
- Worksheet: Record 3 happy, 3 neutral, 3 sad examples

**Phase 3: Teacher Mode Deep Dive (15 minutes)**
- Enable Teacher Mode together
- Explain polarity scores with examples
- Show the flowchart of how the app works
- Discuss: Why do we filter certain words?

**Phase 4: Code Walkthrough (15 minutes)**
- Open `app.py` together
- Point out key sections (input → analysis → output)
- Explain the `if/elif/else` logic for emoji selection
- Optional: Students modify the emoji thresholds

**Phase 5: Reflection & Extension (5 minutes)**
- Discuss: What are the limitations?
- Where else is sentiment analysis used? (Movie reviews, customer feedback)
- Challenge: Think of new features to add

### Differentiation Strategies
- **Beginners**: Focus on using the app and understanding inputs/outputs
- **Intermediate**: Explore Teacher Mode and polarity scores
- **Advanced**: Look at code structure and modify thresholds

## 🔧 How It Works (Technical Overview)

1. **Input Validation**: Checks for empty text
2. **Safety Filter**: Scans for inappropriate words (basic list)
3. **TextBlob Analysis**: 
   - Tokenizes the sentence into words
   - Assigns polarity scores based on word sentiment
   - Averages scores to get overall sentiment (-1 to +1)
4. **Emoji Mapping**:
   - Polarity > 0.1 → 😀 Happy
   - Polarity < -0.1 → 😞 Sad
   - Polarity between -0.1 and 0.1 → 😐 Neutral
5. **Output**: Displays emoji + kid-friendly explanation

### Example Flow
```
Input: "I love learning about robots!"
   ↓
Safety Check: ✅ Pass
   ↓
TextBlob Analysis: Polarity = +0.5 (positive word: "love")
   ↓
Emoji Selection: 0.5 > 0.1 → 😀
   ↓
Output: 😀 "Sounds happy and positive!"
```

## ⚠️ Known Limitations

1. **Simple Sentiment Model**: TextBlob uses basic word matching, not deep learning
   - May misinterpret sarcasm: "Oh great, more homework" (might show 😀)
   - Struggles with context: "I'm not happy" vs "I'm happy"

2. **Limited Bad Word Filter**: The filter is minimal
   - Should be extended for real classroom use
   - Consider using a more comprehensive profanity library

3. **English Only**: TextBlob primarily works with English text
   - Non-English sentences may give unpredictable results

4. **Short Sentences**: Works best with 5-30 word sentences
   - Very short input ("Hi") may always show neutral
   - Very long paragraphs might average out to neutral

5. **Emoji Thresholds**: The 0.1/-0.1 thresholds are arbitrary
   - Could be adjusted based on testing with students
   - No "very happy" or "very sad" distinction

## 🎨 Extension Ideas

For students ready for more:
- Add more emojis (😡 angry, 😍 excited, 😴 bored)
- Adjust polarity thresholds and test differences
- Create a "word cloud" showing which words influenced the result
- Build a game: Guess the emoji before revealing
- Track history of analyzed sentences in the session
- Add multilingual support with language detection

## 📖 Educational Standards Alignment

This project supports:
- **Computer Science**: Algorithms, conditionals, data processing
- **Mathematics**: Number lines, ranges, averaging
- **Language Arts**: Understanding word connotations
- **Digital Citizenship**: Responsible online communication
- **Critical Thinking**: Limitations of AI, bias awareness

## 🛡️ Safety Features

- Input character limit (200 chars) to prevent spam
- Basic profanity filter with neutral fallback
- No data storage or user tracking
- Age-appropriate language throughout
- Teacher Mode for adult supervision

## 🙏 Credits & References

- **TextBlob**: [https://textblob.readthedocs.io/](https://textblob.readthedocs.io/)
- **Streamlit**: [https://streamlit.io/](https://streamlit.io/)
- Sentiment analysis concept based on academic research in NLP
- Original code developed for educational purposes

## 📄 License

This project is created for educational use. Feel free to adapt for classroom teaching while maintaining appropriate credit.

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'textblob'"**
- Run: `pip install -r requirements.txt`

**"LookupError: Resource punkt not found"**
- Run: `python -m textblob.download_corpora`

**App won't start**
- Ensure Python 3.9+ is installed: `python --version`
- Check all dependencies installed: `pip list`

**Incorrect emoji shown**
- Try rephrasing with clearer emotional words
- Remember: The model is simple and has limitations

## 📧 Questions?

This is a teaching tool designed for classroom use. For technical questions, please refer to the TextBlob and Streamlit documentation linked above.

---

**Made with ❤️ for curious young minds learning about AI**