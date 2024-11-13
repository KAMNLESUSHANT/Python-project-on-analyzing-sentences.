from textblob import TextBlob

def demo(text):

    a = TextBlob(text)
    ab = a.sentiment.polarity

    if ab > 0:
        return "😊 Positive"
    elif ab < 0:
        return "😠 Negative"
    else:
        return "😐 Neutral"
if __name__ == "__main__":
    while True:
        print("Enter quit to exit")
        text = input("Enter your text: ")
        if text=='quit':
            break
        ab = demo(text)
        print(f"Sentiment: {ab}")    
