# sample-sendgrid

## 個別送信
- 個別送信及び一括送信どちらも ```send-email-api-sample.http``` 内で実行
**手順**
1. [公式ドキュメント](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/manage_api_key.html)を参考にAPIキーを発行し、コピーする。再度表示させることはできないので注意。
1. コピーしたAPIキーを ```send-email-api-sample.http``` の ```@apikey``` に代入する。
1. toやfromのmailやsubject, contentを編集する。
1. エディタ上でPOSTを実行

### Pythonライブラリを利用する方法
- 個別送信: ```send-each.py```
- 一括送信: ```send-all.py```

**手順**

参考: https://github.com/sendgrid/sendgrid-python

1. (Macの場合の設定方法。その他のOSは上記リンク参照) SendGridのAPIキーを環境変数に設定する。APIキーはシングルクォーテーションで括る。
```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```
1. ```pip install sendgrid```
2. toやfromのアドレスやsubject, contentを適宜編集する。
1. ```python send-hoge.py``` で実行

## Event Webhook
1. （オプション）SendGridからPOSTを受けるURLの設定。[公式ドキュメント](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/debug.html)を参考にRequestBinのアカウントを作成し、Create Request BinでエンドポイントURLを生成する。
1. [公式ドキュメント](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/event.html#:~:text=%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82-,%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97,-Event%20Webhook%20%E3%82%92)を参考にSendGridのSettingsページでEvent Webhookを有効にする。
1. ```send-each.py``` を実行するなど、POST先のURLで設定したWebhookが機能しているか確認する。

## Inbound Parse Webhook
特定のホストへのメールをSendGridが受け取り、自動的に本文・添付ファイル・ヘッダといった要素に分け、それらのデータを指定されたURLへPOSTすることができるもの。これにより、SendGridを経由してメールを受け取ることが可能になる。

kenshiro-ata.com というドメインを作り、[公式ドキュメント](https://sendgrid.kke.co.jp/docs/Tutorials/E_Receive_Mail/receive_mail.html)通りの手順で試した。


## Reference
- [API](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/send_transaction_mail.html#:~:text=%E3%81%AB%E6%8C%87%E5%AE%9A%E5%8F%AF%E8%83%BD-,Web%20API%E3%81%A7%E9%80%81%E4%BF%A1%E3%81%99%E3%82%8B,-Web%20API%E3%82%92)
- [Event Webhook](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/event.html)
- [Inbound Webhook1](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/parse.html)
- [Inbound Webhook2](https://sendgrid.kke.co.jp/docs/User_Manual_JP/Settings/parse.html)
- [Inbound Webhook3](https://docs.sendgrid.com/for-developers/parsing-email/setting-up-the-inbound-parse-webhook)
- [Python library](https://github.com/sendgrid/sendgrid-python)
