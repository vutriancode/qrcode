import qrcode
from docxtpl import DocxTemplate, InlineImage
from fastapi import FastAPI
from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
import uvicorn
import cv2
from docx.shared import Mm
import cv2
import pdf2image
from typing import List
from fastapi import FastAPI, File, UploadFile
import json


app = FastAPI()
@app.post("/")
async def encode_qr(request: Request):
    #from docx.
    body = await request.body()
    body = json.loads(body)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data({"id":body["common_record_id"],"chuyenvien1":body["lawyer_1_personal_legal_paper_number"],"chuyenvien2":body["lawyer_2_personal_legal_paper_number"]})
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("vutrian.png")
    if body["company_type"]==1:
        report_template = "du_thao_co_phan.docx"
        report_output = "giay_de_nghi2.docx"
        doc = DocxTemplate(report_template)
        context_to_load = body
    elif body["company_type"]==4:
        report_template = "ban_du_thao_cong_ty_tnhh_mot_thanh_vien.docx"
        report_output = "giay_de_nghi2.docx"
        doc = DocxTemplate(report_template)
        context_to_load = body
    elif body["company_type"]==5:
        report_template = "ban_du_thao_cty_tnhh_2_tv.docx"
        report_output = "giay_de_nghi2.docx"
        doc = DocxTemplate(report_template)
        context_to_load = body
    context_to_load['qr_code'] = InlineImage(doc,"vutrian.png",width=Mm(35))

    # load the context to the word template
    doc.render(context_to_load)
    doc.save(report_output)
    return FileResponse("giay_de_nghi2.docx")

@app.post("qr_decode")
def decode_qr(request: Request,uploaded_files: List[UploadFile] = File(...)):
    qrCodeDetector = cv2.QRCodeDetector()
    for uploaded_file in uploaded_files:
        images = pdf2image(uploaded_file)
        decodedText, points, _ = qrCodeDetector.detectAndDecode(images[0])
        if points!=None:
            return decodedText
    return {}
  
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)