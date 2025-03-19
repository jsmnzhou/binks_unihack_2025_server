import easyocr

reader = easyocr.Reader(['en']) 
image_data: str = reader.readtext('test_data/assessment-plan-2.png', detail = 0)


