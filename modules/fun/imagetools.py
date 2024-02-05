from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import textwrap
import requests
from io import BytesIO
import time

def get_pfp(pfp:str,resize=(800,800)):
    if str(pfp).startswith("https://") or pfp.startswith("http://"):
        try:
            response = requests.get(pfp)
            image = Image.open(BytesIO(response.content))
        except:
            return False
    else:
        try:
            image = Image.open(pfp)
        except:
            return False
    image = image.convert(mode="RGBA")
    if resize:
        image = image.resize(resize)
    return image

def quote(id, username, display_name="Anonymous", pfp=None, quote=""):
    quote = "\"" + quote + "\""
    background = Image.new("RGBA",(1280,720))
    gradient = Image.open("./modules/fun/assets/quote_gradient.png").resize((1280,720)).convert(mode="RGBA")
    font = ImageFont.truetype("./modules/fun/assets/fonts/DejaVuSans.ttf",28) #28
    font2 = ImageFont.truetype("./modules/fun/assets/fonts/DejaVuSans.ttf",20)
    font3 = ImageFont.truetype("./modules/fun/assets/fonts/DejaVuSans.ttf",20)

    draw = ImageDraw.Draw(background)

    if pfp:
        pfp = get_pfp(pfp)
        background.paste(pfp)

    background.paste(gradient,(0,0),gradient)

    #Quote
    draw.text((980,140),textwrap.fill(quote,35),None,font,align="left",anchor="ms")

    #Display name
    draw.text((915,600),textwrap.fill("- " + display_name,45),None,font,align="left",anchor="ms")

    if username:
        #Username
        draw.text((915,630),textwrap.fill("@" + username if not "#" in username else username ,45), None, font3, align="left", anchor="ms")

    if __name__ == "__main__":
        background.show()
    else:
        filename = f"{id}_{time.strftime('%d_%m_%Y_%H_%M_%S')}.png"
        background.save(f"./modules/fun/temp/{filename}")
        return "./modules/fun/temp/" + filename

def dice(id,number):
    dice = Image.open("./modules/fun/assets/dice.png").convert(mode="RGBA")
    draw = ImageDraw.Draw(dice)
    font = ImageFont.truetype("./modules/fun/assets/fonts/DejaVuSans.ttf",175)

    draw.text((515,500),str(number),align="center",anchor="mm",font=font)

    if __name__ == "__main__":
        dice.show()
    else:
        filename = f"{id}_{time.strftime('%d_%m_%Y_%H_%M_%S')}.png"
        dice.save(f"./modules/fun/temp/{filename}")
        return f"./modules/fun/temp/{filename}"

def rip(id, username=str, description=None, pfp=None):
    tombstone = Image.open("./modules/fun/assets/tombstone.png")

    text_layer = Image.new("RGBA", tombstone.size)

    font = ImageFont.truetype("./modules/fun/assets/fonts/DejaVuSans.ttf",35)

    if pfp:
        pfp = get_pfp(pfp, (300, 300))
        pfp = ImageEnhance.Contrast(pfp).enhance(2)
        pfp = pfp.filter(ImageFilter.EMBOSS)
        pfp = ImageEnhance.Color(pfp).degenerate
        tombstone.paste(pfp, ((450, 180)), pfp)

    text_draw = ImageDraw.Draw(text_layer)
    text_draw.text((600,130),textwrap.fill(username if username else "Anonymous",30),fill="white",stroke_fill="black",stroke_width=4,font=font,align="center",anchor="ms")
    
    if description:
        text_draw.text((600,517),textwrap.fill(description,30),fill="white",stroke_fill="black",stroke_width=4,font=font,align="center",anchor="ms")
    
    text_layer = text_layer.filter(ImageFilter.EMBOSS)
    tombstone.paste(text_layer, text_layer)

    tombstone = ImageEnhance.Contrast(tombstone).enhance(2)

    if __name__ == "__main__":
        tombstone.show()
    else:
        filename = f"{id}_{time.strftime('%d_%m_%Y_%H_%M_%S')}.png"
        tombstone.save(f"./modules/fun/temp/{filename}")
        return f"./modules/fun/temp/{filename}"

if __name__ == "__main__":
    id = 69
    #rip(id, "Moonlight Dorkreamer 🌓", "Was too much of a dork to be left alive! here's some more text to feasten your eyes!", "./modules/fun/temp/pfp.jpg")
    #dice(id,999)
    #quote(id, "@dorkreamer", "Moonlight Dorkreamer 🌓",f"./modules/fun/temp/pfp.jpg","I friggin love pudding, anyways here's a long thing OwO, how about we make this even longer and much more lovely, I think we just done it, it's properly wrapping rn")