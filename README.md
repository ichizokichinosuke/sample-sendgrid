# sample-sendgrid
1. [こちら](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/manage_api_key.html)を参考にAPIキーを発行し、コピーする。サイド表示させることはできないので注意。
1. コピーしたAPIキーを ```send-email-api-sample.http``` の ```@apikey``` に代入する。
1. toやfromのmailやsubject, contentを編集する。
1. エディタ上でPOSTを実行

## Reference
- [公式（ほぼこちらから引用）](https://sendgrid.kke.co.jp/docs/Tutorials/A_Transaction_Mail/send_transaction_mail.html#:~:text=%E3%81%AB%E6%8C%87%E5%AE%9A%E5%8F%AF%E8%83%BD-,Web%20API%E3%81%A7%E9%80%81%E4%BF%A1%E3%81%99%E3%82%8B,-Web%20API%E3%82%92)