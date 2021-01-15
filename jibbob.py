import discord
import os
import urllib.request
import random
from bs4 import BeautifulSoup

client = discord.Client()
#token= "process.env.TOKEN" #토큰값 절대 공개금지 

def Search(url):
 
 html =urllib.request.urlopen(url).read()
 soup = BeautifulSoup(html,'html.parser')
 
 href =soup.find_all(class_='common_sp_link')
 site="https://www.10000recipe.com"
 result=[]
 for i in href:
    result.append(i.attrs['href'])
 if  result: 
     Choice = random.choice(result)
 
     return (site+str(Choice)) 



def Page(url, Page_range):
 Page_num = random.randint(1,int(Page_range))
 Page=(url+str(Page_num))
 return Page

def Searchinput(url,text):
 last="&order=reco&page="
 
 link=(url+text+last)#확인필요
 return link 
 
def speech(speaking):
    speek_num=random.randint(0,3)
    return speaking[speek_num]



Lazy_comments=("게으르시군요 제가 간단한 식단을 가져왔습니다","게으를때는 이처럼 간단한 요리가 최고입니다","그래도 끼니를 거르지는 말아요","힘을 덜 들이고 할수있는 요리를 추천해드릴게요")
A_little_lazy_comments=("조금만 힘내셔서 좋은밥 드세요","그래도 밥같은거 드셔야죠","간단하지만 맛있는!","당신의 피곤을 씻어줄 요리")
common_comments=("오늘의 레시피는~","짜자잔~","저도 먹고싶은 메뉴예용","이 요리 맛있어요")
Diligent_comments=("완성하고 사진찍어주세요 *^^*","부지런한 당신을 위한 아름다운 요리~","요리는 이래야죠 저도 반했습니다","도전해보세요")
Ready_to_search_comments=("제가한번 찾아보겠습니다.","제가 아는 조리법을 알려드릴게요.","음...","당신이 원하는 요리라면..")
no_food=("그런건 없네요 ㅎㅎ;;","저는 독특한 요리는 잘 모릅니다..","그건 찾아보기 힘들것 같네요","ㅎㅎ;;그건 없습니다")

# 집밥봇 사용법 임베드
How_to_use_embed = discord.Embed(title="집밥봇을 사용하는 방법", description="이용해주셔서 감사합니다.*^^*", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
How_to_use_embed.set_footer(text="또한 !비건 메뉴도 있답니다 .*^^*")
How_to_use_embed.add_field(name="게으른 정도에 따른 집밥메뉴 추천이 있습니다", value="[!귀찮아] [!조금 귀찮아] [!보통이야] [!부지런해]\n 이중에서 당신의 상태를 입력해주세요.\n그러면 아저씨가 상황에 맞게 요리를 추천해줄게요. ㅎ", inline=False)
How_to_use_embed.add_field(name="혹시나 조리법을 찾고싶은 요리가 있다면 ", value="[!요리법] 뒤에 찾을 음식을 입력해주세요\n (ex: !요리법 당근케이크)\n  당신이원하는 요리의 조리법을 찾아드릴게요 ", inline=False)
How_to_use_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/769261579253841983/799558455534026782/pngwing.com.png")
How_to_use_embed.set_image(url="https://cdn.discordapp.com/attachments/769261579253841983/799555645425713152/low-angle-chef-seasoning-salad_23-2148471931.jpg")



@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")


@client.event
async def on_message(message):
     if message.content =="!집밥봇 사용법":
         await message.channel.send("안내해드리겠습니다 ㅎㅎ", embed=How_to_use_embed)



     if message.content=="!귀찮아":
         await message.channel.send(speech(Lazy_comments))
         await message.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=18&order=reco&page=',35)))#초스피드 요리
     
     if message.content=="!조금 귀찮아":
         await message.channel.send(speech(A_little_lazy_comments))
         await message.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=12&cat4=56&order=reco&page=',35)))#일상 메인
    
     if message.content=="!보통이야":
          await message.channel.send(speech(common_comments))
          await message.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=13&cat4=56&order=reco&page=',25)))#손님접대 메인
    
     if message.content=="!부지런해":
         await message.channel.send(speech(Diligent_comments))
         await message.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=20&cat4=56&order=reco&page=',3)))#푸드스타일링 메인
    
     if message.content=="!비건":
         await message.channel.send(speech(common_comments))
         await message.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?q=%EB%B9%84%EA%B1%B4&order=reco&page=',5)))#비건

     if message.content=="!어제 뭐 먹었어":
         await message.channel.send("어제 뭐 먹었는지는 제가 모르죠 ^^..")
     
     if message.content.startswith('!요리법'):
         Text=""
         learn=message.content.split(" ")
         vrsize=len(learn)
         vrsize=int(vrsize)
         for i in range(1,vrsize):
             Text=(Text+'+'+learn[i])
         
         encText=urllib.parse.quote(Text)
         link=Searchinput('https://www.10000recipe.com/recipe/list.html?q=',encText)
  
         
         result = Search(Page(link,1))
         if not result:
              await message.channel.send(speech(no_food))
         else:
              await message.channel.send(speech(Ready_to_search_comments))
              await message.channel.send(result)
              

client.run(os.environ['BOT_TOKEN'])
