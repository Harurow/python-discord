# Pythonつかって discord でメッセージ送信

## 用途

タイトル通りpythonを利用してdiscordでメッセージを送信します

## 準備

* pythonが利用できる環境
* `discord.py`が利用できる環境
* `python-dotenv`が利用できる環境
* discordAPI認証情報

### `discord.py`,`python-dotenv`について

`discord.py`,`python-dotenv`を利用しているので事前に`pip`または`pip3`でインストールが必要です

```sh
# 例
pip install discord.py python-dotenv
```

### discordAPI認証情報について

discordを外部から利用する場合、認証情報が別途必要です。
必要に応じて別途発行してください。必要な情報は、

* TOKEN

となります。

セキュリティの関係上、今回のコードには記載しておらず
`.env`ファイルに以下のような形で記載しています。

```sh:.env
TOKEN="xxxxxxxxxxxxxxxxxx...xxxx"
```

また`.gitignore`で`.env`を追加しているので`git`の追跡対象外にしています。

### 注意事項

discordでは同じ発言を連続でしようとするとエラーが発生します。
その仕様の為このコードは連続で実行すると2回目以降は失敗します。
時間を空けるか送信内容のメッセージを変更する必要があります。
