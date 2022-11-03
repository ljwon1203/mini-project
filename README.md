## 깃헙에서 가져온 파일을 터미널을 이용해서 서버를 실행하는 방법

아래의 커멘드를 차례대로 입력하세요!

```
python3 -m venv venv
source venv/bin/activate
pip install flask pymongo dnspython
python app.py
```

커멘드별 설명은 다음과 같습니다.

```
python3 -m venv venv                 1. 파이썬 가상환경 설치  -> 이 커멘드는 코드를 처음 받았을 때만 입력해주세요!
source venv/bin/activate             2. 파이썬 가상환경 접속
pip install flask pymongo dnspython  3. 필요 라이브러리 다운로드
python app.py                        4. 서버실행
```

## 주의사항

1. app.py 내의 DB주소는 git push 로 올리지 않습니다.
2. 코드를 가져온 후 실행시키기 위해선, DB주소를 채워주어야 합니다.

## 각 팀원별 페이지 주소

localhost:5000 뒤에 붙히실 주소입니다.
ex) http://localhost:5000/~~~

- 서우 : /members?name=seowoo
- 현진 : /members?name=hyunjin
- 혜은 : /members?name=hyeeun
- 재원 : /members?name=jaewon
- 태훈 : /members?name=taehoon
