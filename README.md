# 白川鄉點燈巴士票務監控工具 (Shirakawa-go Ticket Reminder)

這個專案是一個基於 Python 實作的網頁自動化工具，旨在解決人工頻繁刷新特定旅遊票務網站（如日本白川鄉點燈活動巴士票）以搶購稀有票券的痛點。

## 🚀 專案亮點與解決的問題
* **自動化輪詢與監控：** 透過定時執行爬蟲，自動檢查目標網站（J-Bus）的座位釋出狀態。
* **即時狀態推播：** 結合第三方 API (LINE Notify / Messaging API)，在發現空位時第一時間發送通知到使用者的手機。
* **環境差異化處理：** (若有將 LINE Token 抽離，可寫：將機敏資訊如 API Token 抽離，增強程式碼安全性與可移植性。)

## 🛠 使用技術 (Tech Stack)
* **程式語言：** Python
* **自動化測試/爬蟲：** Selenium (處理動態網頁互動與滾動)
* **網頁解析：** BeautifulSoup (解析 DOM 結構提取特定日期與座位資訊)
* **API 串接：** `requests` (介接 LINE API)

## ⚙️ 運作流程
1.  Selenium 啟動 Chrome 瀏覽器並導航至目標票務網頁。
2.  自動點擊並載入特定日期與路線的座位表。
3.  BeautifulSoup 解析網頁結構，尋找特定日期的空位標籤（如 "few", "some", "many"）。
4.  若條件符合（特定日期有空位），則透過 `requests` 發送 POST 請求至 LINE API，觸發手機推播通知。
