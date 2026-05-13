# FastAPI Memo Portfolio

Simple FastAPI portfolio project for server program evaluation.

Topic:

- Memo list
- Image upload
- PostgreSQL raw SQL
- Static file service from `public/uploads`

## 1. Install

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Database

Edit `.env` and write PostgreSQL settings.

Tables are created automatically when the FastAPI server starts.

Table names:

- `t_memo_desc`
- `t_memo_contents`

## 3. Run

```powershell
python main.py
```

Open:

```text
http://127.0.0.1:8000
```

Pages:

- `http://127.0.0.1:8000/upload` - upload sample
- `http://127.0.0.1:8000/select` - select sample

For a different topic like fish, corn, or clothes, edit only the `MY_TYPE` line in `pages/MY_TYPE.js`.

```js
const MY_TYPE = "수산물";
```

In `pages/select.html`, add fields to `LIST_FIELDS` when the server returns more JSON keys.

```js
const LIST_FIELDS = [
  { label: "내용", key: "content" },
  { label: "가격", key: "price" },
  { label: "이미지", key: "img_url", type: "image" }
];
```

## Evaluation Points

- Environment: `requirements.txt`, `.env`
- DB connection module: `dbconnect.py`
  - `getConnect()`
  - `create_table()`
- Server program: `main.py`
  - `GET /`
  - `GET /upload`
  - `GET /select`
  - `GET /api/memo_desc`
  - `GET /api/memos`
  - `POST /api/add_memo_desc`
  - `POST /api/add_memo_contents`
- Page file send/receive: `pages/index.html`, `pages/upload.html`, `pages/select.html`
- Static upload path: `public/uploads`
- Batch program: `batch.py`
  - Prints post count every 30 seconds

## API Body Example

`POST /api/add_memo_desc` uses form data.

```text
memo_welcome_msg=hello
memo_sub_msg=simple memo
```

`POST /api/add_memo_contents` uses form data.

```text
memo_id=1
content=memo content
img_url=https://example.com/sample.jpg
image=file upload
```

If `image` is uploaded, the server saves it in `public/uploads` and stores that public path in DB.
If `image` is empty, the server stores the submitted `img_url` in DB.
