# sample-sendgrid

## 一括送信
1. [公式ドキュメント](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/manage_api_key.html)を参考にAPIキーを発行し、コピーする。サイド表示させることはできないので注意。
1. コピーしたAPIキーを ```send-email-api-sample.http``` の ```@apikey``` に代入する。
1. toやfromのmailやsubject, contentを編集する。
1. エディタ上でPOSTを実行

## Event Webhook
1. （オプション）SendGridからPOSTを受けるURLの設定。[公式ドキュメント](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/debug.html)を参考にRequestBinのアカウントを作成し、Create Request BinでエンドポイントURLを生成する。
1. [公式ドキュメント](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/event.html#:~:text=%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82-,%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97,-Event%20Webhook%20%E3%82%92)を参考にSendGridのSettingsページでEvent Webhookを有効にする。
1. ```send-all.py```を実行するなど、POST先のURLで設定したWebhookが機能しているか確認する。
## Reference
- [公式（ほぼこちらから引用）](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/send_transaction_mail.html#:~:text=%E3%81%AB%E6%8C%87%E5%AE%9A%E5%8F%AF%E8%83%BD-,Web%20API%E3%81%A7%E9%80%81%E4%BF%A1%E3%81%99%E3%82%8B,-Web%20API%E3%82%92)