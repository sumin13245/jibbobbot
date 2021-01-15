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
 



@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")


@client.event
async def on_message(massage):
     if massage.content =="!집밥봇 사용법":
         await massage.channel.send ("[!오늘 뭐 먹지] 를 입력하시고\n 제가 말씀드리는 게으름의 정도를\n  !~~~ 이런식으로 말씀주시면 \n추천해드릴게요.\n당신이 찾고싶은 \n요리가 있을때는 [!집밥추천]\n또한[!비건요리] 있답니다.^^ \n사용법은 간단하죠?\n  자주 이용해주세요❤❤" )
         

     if massage.content == "!오늘 뭐 먹지":
         await massage.channel.send("당신의 게으름의 정도를 입력하세요")
         await massage.channel.send("[귀찮아] [조금 귀찮아] [보통이야] [부지런해]")
     
     if massage.content=="!귀찮아":
         await massage.channel.send("게으르시군요 제가 간단한 식단을 가져왔습니다")
         await massage.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=18&order=reco&page=',35)))#초스피드 요리
     
     if massage.content=="!조금 귀찮아":
         await massage.channel.send("조금만 힘내셔서 좋은밥 드세요")
         await massage.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=12&cat4=56&order=reco&page=',35)))#일상 메인
    
     if massage.content=="!보통이야":
         await massage.channel.send("이런건 어떠세요?")
         await massage.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=13&cat4=56&order=reco&page=',25)))#손님접대 메인
    
     if massage.content=="!부지런해":
         await massage.channel.send("완성하고 사진찍어주세요 *^^* ")
         await massage.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?cat2=20&cat4=56&order=reco&page=',3)))#푸드스타일링 메인
    
     if massage.content=="!비건":
         await massage.channel.send("이번 음식은~")
         await massage.channel.send(Search(Page('https://www.10000recipe.com/recipe/list.html?q=%EB%B9%84%EA%B1%B4&order=reco&page=',5)))#비건

     if massage.content=="!어제 뭐 먹었어":
         await massage.channel.send("어제 뭐 먹었는지는 제가 모르죠 ^^..")
     
     if massage.content.startswith('!집밥추천'):
         Text=""
         learn=massage.content.split(" ")
         vrsize=len(learn)
         vrsize=int(vrsize)
         for i in range(1,vrsize):
             Text=(Text+'+'+learn[i])
         
         encText=urllib.parse.quote(Text)
         link=Searchinput('https://www.10000recipe.com/recipe/list.html?q=',encText)
  
         
         result = Search(Page(link,1))
         if not result:
              await massage.channel.send("그런건 없네요 ㅎㅎ;;")
         else:
              await massage.channel.send("한번 찾아보겠습니다")
              await massage.channel.send(result)



client.run(os.environ['BOT_TOKEN'])
