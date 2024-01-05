from fastapi import APIRouter,File,UploadFile
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/upload/")
async def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

@router.get("/getfile/")
async def read_file(file_name: str):
    file_path = f"D:\PythonLearning\dummy_project\1.PNG"
    return FileResponse(file_path)