import sys
sys.path.append('./modules/')   
import modules.utils as utils
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import PlainTextResponse


app = FastAPI()

@app.get("/")
async def test(): 
    return "hello world"

@app.post("/extract_styles_names",)
async def extract_styles(
    part_file: UploadFile = File(...),
    desc_file: UploadFile = File(...), 
    response_class=PlainTextResponse
):
    
    parts_txt = await part_file.read()
    desc_parts_txt = await desc_file.read()

    file_name_new = utils.name_parts(parts_txt, desc_parts_txt)
    for part in file_name_new: 
        print(part)

    return 0

    # parts = line.strip for line in content.decode("utf-8").splitlines() if line.strip()
    # print(parts)
    # part_file_data = await part_file.read()
    # desc_file_data = await part_file.read()
    # return utils.name_parts(part_file_data, desc_file_data)
    


