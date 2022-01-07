# mypkg
## 概要    
ファイル名【scripts】内にある２つのノード、【count.py】と【twice.py】を使って数字をカウントしていき、それをメッセージとして表示するパッケージです。

## 動作環境 
・Raspberry pi 4B  
・OS：Ubuntu 20.04  
・ROS1

## 実行方法
**パッケージを構築する**
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/tamiharu/mypkg.git
$ cd ~/mypkg
$ catkin_make
```

## 実行方法
このパッケージを実行する際には端末が３つ必要になるのでそれぞれの操作方法を解説します。
### ・端末１
ROSを有効にします。  
```$ roscore```

### ・端末２
2つあるノードのうちの一つ【count.py】を起動します。  
```$ rosrun mypkg count.py```  
起動した後、何も表示されませんが、実行できているのでそのままにしておきます。  

### ・端末３
最後にもう一つのノードである【twice.py】を起動します。  
```$ rosrun mypkg twice.py```  
すると数字が表示され、数字がどんどん増えていきます。  

## 動作結果（動画）  
動作した結果をyoutubeにて公開しています。  
動画は[こちら](https://www.youtube.com/watch?v=_PnO3ojpHpU)です。  

## その他(ライセンス、著作権者等)
・ライセンス：[BSD 3-Clause License](https://github.com/tamiharu/mypkg/blob/master/LICENSE)  
・著作権者：上田隆一(Ryuichi Ueda)

・Pushの際に参考にしたサイト  
HatenaBlog AI can fly !! 【Git】ローカルで作成したリポジトリをGithubにPushする【GitHub】  
URL：https://ai-can-fly.hateblo.jp/entry/first-git-push-to-github
