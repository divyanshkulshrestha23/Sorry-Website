from flask import Flask, render_template

app = Flask(__name__)

# THE REFINED PERSONAL STORY
STORY = {
    "start": {
        "text": "You found the link. I wasn't sure if you'd scan it, but I'm glad you're here. I need to apologize to you, but I wanted to say it in a way that feels like 'us'.",
        "options": [
            {"text": "Apology? Who asked?", "next": "the_why1"},
            {"text": "I'm listening...", "next": "the_why"}
        ]
    },
    "the_why1": {
        "text": "Richa, if I've ever meant something to you, I'd beg of you to please listen to me. I've always been desperately in love with you, but I know what I've done has devastated you and it will take time for the wounds to heal. Nevertheless, I wish to be able to bandage those wounds at the very least so you can feel that I DO care for you, and that my love for you was never fake.",
        "options": [
            {"text": "I'm listening...", "next": "the_why"}
        ]
    },
    "the_why": {
        "text": "I know I made a huge mistake. I'm so sorry. I'm not a fan of this version of who I became. I need to and I will do better. Because I know your kindheartedness will never leave my heart. Because I know your soft touch will never be forgotten by my skin. Because I know my lips will never forget the coziness they find in your cheeks."
                "Because I know I will always be in love with you.",
        "options": [
            {"text": "Go on", "next": "the_memory"},
            {"text": "But what about the trust?", "next": "the_trust"}
        ]
    },
    "the_trust": {
        "text": "This trust, I know you value it more than anyone. I know I'm in a delicate position right now to be able to win it back. But I'm completely in your hands, Richa. I will fight day and night for this trust. I know my love is strong enough that I will be able to show how I can repair the world that I've brought so much harm on. Each cell of mine aches for you but it is also ready to go into thr restless pain while it tries to win back your love. "
                "Because I'm yours and yours only, my Richa. And I know we were destined for each other.💗💗💗",
        "options": [
            {"text": "How do you know that?", "next": "the_memory"},
            {"text": "Mine? I don't believe that.", "next": "only_yours"}
        ]
    },
    "only_yours": {
        "text": "I read books on your recommendation. I listen to ALL the songs you send me. I watch TV shows you tell me. I read up about the things you tell me that I don't know about. I wear the things you get for me. Richa Priya, you think I don't find you cool or beautiful or desirable."
                "Yet I've surrounded myself all over with media that relates to you, with items that remind me of you and if my baby says she likes my hair long but beard short, I will make sure all the hair from my chin goes to my head."
                "Because darling, you're the No.1 girl for me. You're the prettiest, hottest, coolest and most desirable person my heart could ever think of, and I need you in my life daily.❤️❤️❤️",
        "options": [
            {"text": "And that's supposed to make me feel what???", "next": "the_meaning"},
            {"text": "Do you mean that? 🥹", "next": "india_gate"}
        ]
    },
    "the_meaning": {
        "text": "I just want you to realize that we can work it out, Richa. I'll go across the universe yet you'll be the only one who will ever know me inside out. I'll love you 26 hours a day, 8 days a week, 14 months a year. And I'll hope you always see this love in my eyes.",
        "options": [
        {"text": "Ok. Keep going.", "next": "the_memory"}
        ]
    },
    "the_memory": {
        "text": "I was thinking back to where this all began. 3rd Feb. IHE Quiz competition. You were standing there with all the answers, and I was just... captivated. Admittedly, I didn't do well in the quiz, but little did I know, the key to all the answers of my life was standing right in front of me.",
        "options": [
            {"text": "I remember that.", "next": "india_gate"},
            {"text": "I don't need this flashback.", "next": "no_flashback"}
        ]
    },
    "no_flashback": {
        "text": "I understand that. But I hope you know that through all the thick and thin that we've gone through, I've only ever been able to hold onto the good moments in us. Because they stick out. Because they are gonna shine like an eternal flame for all our lives."
                "There's no other explanation to how two people can laugh so heartily on the stupidest things with each other.🤭🤭🤭",
        "options": [
            {"text": "What will does this eternal flame do?", "next": "the_vow"},
        ]
    },
    "india_gate": {
        "text": "That day in CS gardens, I think about it every day. The air was cool, and 'Can't Take My Eyes Off You' started playing. I danced like no one was watching, even though I knew *you* were. I think that was the moment the music really started for us. If given the chance, I'd like to dance again, but this time, with my no.1 girl only and THAT'S YOUUUUUUU.",
        "options": [
            {"text": "Are you still genuine like you were that day?", "next": "batman_sticker"},

        ]
    },
    "batman_sticker": {
        "text": "Every day, I look at my wall and see that Batman sticker you made for me. It’s more than just a sticker; it’s a piece of you that stays with me even when things are quiet. It reminds me of the care you put into the little things and also the fact that every night Richa is looking over me, protecting me from criminals hehe."
                "I know that in my life, I'd always and always love you more than anyone and I'd do anything to keep you in my life forever. You bring me everything and if you stick around, you'll see how my love will always keep growing for you.",
        "options": [
            {"text": "That sticker belongs there...", "next": "ece_kiss"}
        ]
    },
    "ece_kiss": {
        "text": "If I’m being honest, the world changed in the ECE department. That kiss... it was like someone finally turned on the lights in a room I’d been sitting in for years. Ever since that moment, I've been able to see the light clearly.",
        "options": [
            {"text": "What does that light mean now?", "next": "the_vow"}
        ]
    },
    "the_vow": {
        "text": "It means that I am sorry for the moments I let the darkness back in. I made mistakes which decimated your confidence in me. I regret doing all of that. I want you to know, with everything I am, that I will never leave your hand, not in the blinding light of our best days, and certainly not in the darkness of the hard ones.",
        "options": [
            {"text": "Promise from the bottom of your heart to the top of your soul?", "next": "the_promise"}
        ]
    },
    "the_promise": {
        "text": "I promise. Every bit of it. I'm ready to work on myself and the world we've built so that we can move past the glitches and get back to the music. I will always be there for you and your wounds will seem like distant specks in no time, my darling.",
        "options": [
            {"text": "What's next?", "next": "bridge_to_card"}
        ]
    },
    "bridge_to_card": {
        "text": "I've said a lot here, but the screen feels a bit too cold for the rest of this. You can now check the rest of the card, my bubbu.",
        "options": [] # End of digital journey
    }
}

@app.route('/')
@app.route('/story/<node_id>')
def story(node_id="start"):
    node = STORY.get(node_id, STORY["start"])
    return render_template('story.html', node=node)

if __name__ == '__main__':
    app.run(debug=True)
