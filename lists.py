import random

monkey_gif = ["https://tenor.com/view/monkey-tapaatap-tapatap-monkey-tapatap-dance-gif-23864133",
       "https://tenor.com/view/monkey-smile-george-monkey-gif-22183141",
       "https://tenor.com/view/monkey-wtf-monkey-gasp-monkey-gif-22578374",
       "https://tenor.com/view/monkey-gangster-monkey-monk-monke-shaptic-gif-21239890",
       "https://tenor.com/view/monkey-artificialbloom-monkey-hulahoop-monkey-dancing-gif-23688613",
       "https://tenor.com/view/monkey-sunglasses-on-orangutan-sunglasses-monkey-sunglasses-baller-gif-23723639",
       "https://tenor.com/view/funny-monkey-eat-hungry-adorable-cute-gif-16750529",
       "https://tenor.com/view/monkey-cool-monkey-monkey-eating-pog-monkey-snub-nosed-monkey-gif-21132579",
       "https://tenor.com/view/monkey-monkeys-excited-excited-monkey-monkey-excited-gif-21718012",
       "https://tenor.com/view/monkey-excited-excited-monkey-monkey-noises-excited-monkey-noises-gif-23721513",
       "https://tenor.com/view/monke-funny-monke-monke-funny-monke-meme-funny-monkey-gif-24802020",
       "https://tenor.com/view/super-cute-monkey-wholesome-wholesome-chungus-moneky-pc-gaming-monkey-gif-24419892",
       "https://tenor.com/view/monkey-monke-monk-funny-funny-monkey-gif-21468769",
       "https://tenor.com/view/cli%C3%A7-cli%C3%A7monkey-monkey-sleepy-sleepy-monkey-gif-24594700",
       "https://tenor.com/view/monkey-orangatan-ape-golira-monkey-supreme-gif-21836370",
       "https://tenor.com/view/honeycardi-george-monkey-monkey-gif-20972657",
       "https://tenor.com/view/monkey-rabbit-monkey-with-rabbit-ears-car-nekoglai-gif-24804988",
       "https://tenor.com/view/shaptic-monkey-monke-monk-monkey-eating-gif-21571556",
       "https://tenor.com/view/shaptic-monkey-monke-monk-monkey-eating-gif-21571556",
       "https://tenor.com/view/stealing-monkey-monkey-steal-churaana-choree-gif-21006154",
       "https://tenor.com/view/dancing-monkey-style-monkey-tango-monkey-best-dancer-the-dancing-monkey-gif-19480759",
       "https://tenor.com/view/monke-monke-funny-funny-monke-meme-monke-monke-meme-gif-24802019",
       "https://tenor.com/view/abble-angry-monke-angry-monkey-abble-right-now-frown-gif-20243861",
       "https://tenor.com/view/hey-joe-monkey-monkey-joe-monkey-heart-love-joe-gif-23020196",
       "https://tenor.com/view/fridathemonkey-monkey-smile-zzsoobn-cute-monkey-gif-22937147",
       "https://tenor.com/view/monkey-exercise-zzsoobn-monkey-exercise-cute-monkey-gif-22992001",
       "https://tenor.com/view/voice-chat-vc-monkey-monkey-vc-monkey-voice-chat-gif-24921966",
       "https://tenor.com/view/chimp-monke-monkey-monky-muscles-gif-21212025",
       "https://tenor.com/view/monkey-pog-pog-poggers-monke-pog-monkey-poggers-gif-19560507",
       "https://tenor.com/view/monkey-watching-in-the-monkey-looks-at-the-skull-gif-25484214",
       "https://tenor.com/view/sleepy-monkey-dean-schneider-dean-schneider-vlogs-petting-a-monkey-caressing-head-gif-17967212",
       "https://tenor.com/view/alexswrld-alexswrid-monkey-heresyourmonkeycontent-georgie-monkey-gif-21907193",
       "https://tenor.com/view/money-rich-monkey-wealthy-monkey-business-gif-17154331",
       "https://tenor.com/view/monkey-gif-25042719"]

attention = ["HELLO!", "HI!", "*mhuack*", "*licks you*", "你好小猫"]

shop = {"Get purred: 100" : ":drooling_face:",
        "Kitten: 1500": ":heart_eyes_cat:",
        "Woman: 5000": ":dress:"}

def get_shop():
  return shop
  
def get_attention():
  attention_phrase = random.choice(tuple(attention))
  return (attention_phrase)

def get_monke():
  monke_link = random.choice(tuple(monkey_gif))
  return (monke_link)