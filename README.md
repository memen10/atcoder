# AtCoder 用リポジトリ
AtCoder 参加用リポジトリ。
コンペ毎のディレクトリ作成・submit 等には以下のツールを使用。
- atcoder-cli:
http://tatamo.81.la/blog/2018/12/07/atcoder-cli/
- online-judge-tools: https://github.com/kmyk/online-judge-tools

ディレクトリ名は AtCoder Problems のコンペティション分類に準拠。  
https://kenkoooo.com/atcoder#/table/



以下、コンペ時利用コマンド例：
```
cd OC
acc new abs
cd abs/practicea
// main.py 編集
oj t -c "python3 main.py" 
oj login https://atcoder.jp/
acc login
acc submit  # to use submit function, you have to install online-judge-tools
```

または
`oj t -c "python3 main.py"` の代わりに、以下を .zshrc へ登録の上で `ojt-py` をテストコマンドとして利用。
```
alias ojt-py='oj t -c "python3 main.py"'
```