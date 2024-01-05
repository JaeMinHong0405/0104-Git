def print2():
  print('빅 사이즈 로다가')

# 우선 실수를 해서 정말 죄송합니다 ㅠㅠ 
# 어제 배웠던 내용 복습하는데 제가 과제를 잘못 이해해서 결과는 맞게 했는데 방법을 CMD (command prompt) 를 안 써서 
# 다시 해보았습니다ㅜㅠ 이 메모가 도움이 조금 되시길 바래요ㅠㅠ 죄송합니다
  
# main.py에 제가 local repository랑 remote repository (Github) connection 했던 command line prompts 다 적어놓았습니다!
# 사진은 어쨌든 똑같은 result일거라 변동이 없어도 되지만 마지막 result 를 reach하기 위한 process만 다시 이해하면 될것같습니다!!
# 혹시라도 다시 연습하실 수 있게 제가 revise한 steps들 순서대로 여기에다가 적어놓겠습니다..!!

# 1) git clone https://github.com/JaeMinHong0405/0104-Git.git [name of your clone repository]
# 1번은 대솔님이 제 remote repository를 다운을 받고, 대솔님의 local environment에서 print2.py를 다시 작성하시기위한 코드입니다

# 2) git log
# 이걸 치시면 head-> main, origin/main이런게 뜰거에요! head-> main이랑 origin/main이 같이 있어야 connection 이 successful한거라고 보심 될것같습니다!

# 대솔님이 clone repository 다운 받으신 후에 print2.py를 예를 들어서 
# def print2():
  # print('빅 사이즈 로다가!')
# 이렇게 쓰시고 수정하셨으면 다시 CMD 로 들어가셔서 

# 3) git add . 
# (수정된 파일 전부 다 upstaging 하기 위한 작업)

# 4) git status 
# 파일 수정 체크

# 5) git commit -m "[committed_version_name]"
# commit을 하셔야 file change가 되어서 이 부분을 꼭 하셔야해요!

# 6) git push origin main

# 이렇게 까지 하시면 저희가 원래 해야했던 방법대로 과제 마치게 됩니다..!! 어저께 잘못 이해해서 죄송합니다 ㅠㅠㅠㅠ
# 혹시라도 수정해야할부분이 있거나 피드백이 있으시면 카톡 편하게 주세요!! 감사합니다
