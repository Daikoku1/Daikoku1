import feedparser
def make_readme():
    blog_url = "https://rss.blog.naver.com/jjys9047"
    rss_feed = feedparser.parse(blog_url)
    
    max_post = 5
    post_list = ""
    for idx, feed in enumerate(rss_feed['entries']):
        if idx > max_post: break

        feed_date = feed['published_parsed']
        post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

    return f"""
<h2> "안녕하세요"👋 </h2>
<img align='right' src="https://user-images.githubusercontent.com/50973778/144942576-b2f10b31-e628-43e4-b7da-3cc2144a5b73.gif" width="230">
<p><em> 데이터 분석가를 꿈꾸는 정윤성입니다.</br> 어제의 나보다 성장하기 위한 </br> 노력들을 기록하고 있습니다.</em></p>

### For Connect
<a href="https://blog.naver.com/jjys9047" target="_blank"><img src="https://img.shields.io/badge/-BLOG-brightgreen?style=flat-square&logo=Bloglovin&logoColor=white">
<a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=jys9047@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-c14438?style=flat-square&logo=Gmail&logoColor=white" alt="Email">
<a href="mailto:jjys9047@naver.com" target="_blank"><img src="https://img.shields.io/badge/-Naver-brightgreen?style=flat-square&logo=Naver&logoColor=white" alt="Email">

[![GitHub Daikoku1](https://img.shields.io/github/followers/Daikoku1?label=follow&style=social)](https://github.com/Daikoku1)

</br>

## 💻 Latest Blog Posts
{post_list}
<img align="center" src="/>

### ⚡ Work Stats
<p align = 'center'>
  <img src="https://github-readme-stats.vercel.app/api?username=Daikoku1&show_icons=true&theme=midnight-purple" alt="Anurag's GitHub stats" height="130" hspace="20"/>
  <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=jys9047" alt="BOJ_profile" height="130" hspace="20"/>
</p>

<p align="right"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/Daikoku1/count.svg" />
</p>
""" 


def update_readme():
    readme = make_readme()
    return readme 


if __name__ == "__main__": 
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f: 
        f.write(readme)


