import pytesseract
from PIL import Image
import pdf2image


def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.
    """

    image = Image.open(image_path)

    text = pytesseract.image_to_string(
        image,
        lang="eng"
    )

    return text


def extract_text_from_scanned_pdf(pdf_path):
    """
    Convert PDF pages to images and perform OCR.
    """

    pages = pdf2image.convert_from_path(pdf_path)

    full_text = ""

    for page_num, page in enumerate(pages):

        text = pytesseract.image_to_string(
            page,
            lang="eng"
        )

        full_text += f"\n--- Page {page_num + 1} ---\n"
        full_text += text

    return full_text


if __name__ == "__main__":

    sample_pdf = "sample.pdf"

    text = extract_text_from_scanned_pdf(sample_pdf)

    print(text[:1000])
