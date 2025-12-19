# 일주일간의 던전 생존기

def game():
    player_name = input("닉네임을 설정하세요. :")
    player_health = 100
    inventory = []

    print(f"{player_name}님, 일주일간 던전 생존기에 오신 걸 환영합니다.\n")
    print(f"체력 : {player_health}\n")
    print(f"소지품 : {inventory}\n")

    print("1일차(월요일)")
    player_health -= 10
    print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {player_health})\n")
    print(f"인벤토리: {inventory}\n")
    print('''
      [월요일]
      배고픈 아침입니다.
      사과를 발견했습니다.\n"
      ''')
    while True:
        eat_apple = input("사과를 얻었습니다. 먹겠습니까? (예 / 아니오) : \n")    
        if eat_apple == "예":
            player_health += 20
            inventory.append("사과")
            print("사과를 먹고 기운이 납니다. (체력 + 20)\n")

        else:
            player_health -= 20
            print("아침은 꼭 챙겨드세요!(체력 - 20)\n")

        print(f'현재 체력 : {player_health}')
        if player_health <= 0:
            print("배고파서 죽는다는 건 슬픈 일이죠! 게임 오버.\n")
            return False
        elif player_health <= 50:
            print("버틸만 하네요 하지만 슬슬 배가 고파 옵니다.(먹을 것을 구하세요!)\n")
        else:
            print("배가 부르니 졸립니다. 다음 날로 이동합니다.\n")

        print("2일차(화요일)")
        player_health -= 10
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {player_health})\n")
        print(f"인벤토리: {inventory}")
        if player_health > 0:
            print('''
                [화요일]
                기분 좋은 아침입니다.
                버섯을 발견했습니다.\n"
                ''')
            mushroom = input("버섯을 발견했습니다. 드시겠습니까? (예 / 아니오)\n")
            if mushroom == "예":
                inventory.append("버섯")
                player_health -= 30
                print("모르는 것을 주워먹으면 탈이나는 법이죠!(체력 - 30)\n")

            else:
                inventory.append("버섯")
                print("자세히 살펴보면 예쁘게 생겼습니다. 독버섯 같아요! 일단 가지고 있죠!\n")
            
            print(f"현재 체력 : {player_health}")
            if player_health <= 0:
                print("배고파서 죽는다는 건 슬픈 일이죠! 게임 오버.\n")
                return False
            elif player_health <= 50:
                print("버틸만 하네요 하지만 슬슬 배가 고파 옵니다.(먹을 것을 구하세요!)\n")
            else:
                print("배가 부르니 졸립니다. 다음 날로 이동합니다.\n")

        print("3일차(수요일)")
        player_health -= 10
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {player_health})\n")
        print(f"인벤토리: {inventory}\n")
        if player_health > 0:
            print('''
                [수요일]
                피곤한 아침입니다.
                사자를 발견했습니다\n."
                ''')
            lion = input("사자를 발견했습니다. 도망가시겠습니까? (예 / 싸운다)\n")
            if lion == "예":
                player_health -= 100
                print("사나운 짐승한테는 등을 보이면 안되죠!\n")

            elif lion == "싸운다":
                fight_lion = input("가방에 버섯이 있네요 이걸 먹이면 이길 수 있겠어요! (먹인다 / 싸운다)\n")
                if fight_lion == "싸운다":
                    player_health -= 100
                    print("사자에게 덤비는 멍청이가 어디있나요?\n")
                else :
                    player_health += 60
                    inventory.remove("버섯")
                    inventory.append("고기")
                    print("사나운 사자를 죽이고 고기를 획득했습니다. 포식하시네요! (체력 + 60)\n")

                
            
            print(f"현재 체력 : {player_health}")
            if player_health <= 0:
                print("사자와 싸워서 이길뻔 했네요! 아쉽습니다. 게임 오버.\n")
                return False
            elif player_health <= 50:
                print("슬슬 배가 고파 옵니다.(먹을 것을 구하세요!)\n")
            else:
                print("배가 부르니 졸립니다. 다음 날로 이동합니다.\n")

        print("4일차(목요일)")
        player_health -= 10
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {player_health})\n")
        print(f"인벤토리: {inventory}\n\n")
        if player_health > 0:
            print('''
                [목요일]
                풍요로운 아침입니다.
                다친 누군가를 발견했습니다.\n"
                ''')
            friend = input("누군가 쓰러져 있습니다. 도와주시겠습니까? (예 / 아니오)\n")
            if friend == "예":
                inventory.remove("고기")
                player_health += 20
                print("곤경에 처한 사람을 구해주셨군요. 같이 식사를 하며 친구가 생겼습니다! (체력 + 20)\n")
            else:
                player_health -= 100
                print("위험한 세상이라지만 한 번쯤은 선의를 베풀어도 되지 않을까요? 다친 누군가가 쏜 활에 맞았습니다.\n")
            
            print(f"현재 체력 : {player_health}")
            if player_health <= 0:
                print("베풀 줄 아는 사람이 되어야 겠네요! 게임 오버.\n")
                return False
            elif player_health <= 50:
                print(f"{friend}이(가) 생기니 먹을 것도 두배!(먹을 것을 구하세요!)\n")
            else:
                print("배가 부르니 졸립니다. 다음 날로 이동합니다.\n")

        friend = input("친구의 이름을 지어주세요! : \n")
        friend_health = 100

        print("5일차(금요일)")
        player_health -= 10
        friend_health -= 10
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {player_health})\n")
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {friend_health})\n")
        print(f"인벤토리: {inventory}\n")
        if player_health > 0:
            print(f'''"
                [금요일]
                외롭지 않은 아침입니다.
                {friend}와 함께하니 무섭지 않아요.
                깊은 호수를 발견했습니다.\n"
                ''')
            
            lake = input("많이 깊어 보이네요 돌아서 가시겠습니까? (예 / 아니오)\n")
            if lake == "예":
                inventory += "물고기"
                player_health += 30
                friend_health += 30
                print("호수를 돌다보니 누군가 자리를 비운 낚시터를 발견했습니다. 물고기를 획득합니다!!(체력 + 30)\n")

            else:
                player_health -= 1000
                friend_health -= 1000
                print("이 호수를 수영해서 간다니요 호수 속에 괴물을 만났습니다!\n")
            
            print(f"{player_name}현재 체력 : {player_health}")
            print(f"{friend}현재 체력 : {friend_health}")
            if player_health <= 0:
                print("친구따라 강남간다더니 같이 빠지셨네요! 게임 오버.\n")
                return False
            elif player_health <= 50:
                print(f"{friend}이(가) 생기니 먹을 것도 두배!(먹을 것을 구하세요!)\n")
            else:
                print("배가 부르니 졸립니다. 다음 날로 이동합니다.\n")

        print("6일차(토요일)")
        player_health -= 10
        friend_health -= 10
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {player_health})\n")
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {friend_health})\n")
        print(f"인벤토리: {inventory}\n")
        if player_health > 0:
            print('''
                [토요일]
                심상치 않은 아침입니다.
                바람이 거세네요!
                태풍이 옵니다."
                ''')
            typhoon = input("태풍이 옵니다. 근처 피할 곳을 찾아야합니다. 동굴을 찾겠습니까? (예 / 아니오)\n")
            if typhoon == "예":
                cave1 = input("이 동굴에 들어가시겠습니까? 예 / 아니오\n")
                if cave1 == "예":
                    friend_health -= 50
                    print(f"잠을 자던 곰을 깨웠습니다. {friend}를 버리고 도망갑니다.\n")
                else :
                    print("위험해보이네요 바로 옆에 동굴이 있네요 저기 숨어야겠습니다.\n")
            else :
                player_health -= 1000
                friend_health -= 1000
                print("사람이 자연을 어떻게 이기나요?\n")
            
            print(f"{player_name}현재 체력 : {player_health}")
            if player_health <= 0:
                print("사람은 원래 바람에 날아갈 수 있답니다. 모르셨군요! 게임 오버.\n")
                return False
            else:
                print("오늘도 무사히 살아남았습니다.. 다음 날로 이동합니다.\n")
            print(f"{friend}현재 체력 : {friend_health}")
            
            if friend_health < 50:
                print(f"{friend}이(가) {player_name}을(를) 노려봅니다!\n")

        print("7일차(일요일)")
        player_health -= 10
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {player_health})\n")
        print(f"[아침] 체력이 10 감소했습니다. (현재 체력: {friend_health})\n")
        print(f"인벤토리: {inventory}\n")
        if player_health > 0:
            print('''
                [일요일]
                던전의 마지막 아침입니다.
                고요하네요....\n"
                ''')
            
            friend1 = input(f"먹여주고 재워줬더니 뒤통수를 칩니다. 마지막 시련이에요 {friend}와 싸웁니다!! 예 / 아니오\n")

            if friend1 == "예":
                friend_health -= 1000
                print(f"제 손으로 {friend}를 죽였지만 어쩔수 있나요. 먼저 덤볐는걸요!\n")
            else:
                friend_health += 1000
                player_health -= 1000
                print(f"억울하고 원통합니다! 끝까지 믿었던 {friend}에게 배신당했습니다!!\n\n")

            print(f"현재 체력 : {player_health}")
            if player_health <= 0:
                print("친한 친구여도 자신을 100% 보여줄 필요는 없죠! 게임 오버.\n")
                return False
            else:
                print(f"지긋지긋하던 일주일간의 던전이 끝났습니다!\n 축하드립니다!! {player_name}님 생존하셨습니다!\n" )
            
            print(f"현재 체력 : {friend_health}")
            
            if friend_health < 0:
                print("친구를 잃으셨네요..아쉽지만 인생은 독고다이!")
            else:
                print(f"결국 던전은 {friend}가 독점했네요! 다음 생엔 강단있는 사람이 되길!!")
                return False

while True:
    result = game()
    if result:
        replay = input("\n게임을 다시 시작하겠습니까? (예 / 아니오): ")
        if replay == "예":
            continue
        else:
            print("게임을 종료합니다.")
            break
    else:

        replay = input("\n게임을 다시 시작하겠습니까? (예 / 아니오): ")
        if replay == "예":
            continue
        else:
            print("게임을 종료합니다.")
            break