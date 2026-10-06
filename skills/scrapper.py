import os
import requests
import pandas as pd
from bs4 import BeautifulSoup


OUTPUT_FOLDER = r"D:\hasil_scrape"


def scrape_website(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/154.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    # Ambil title website
    title_tag = soup.find("title")

    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        title = "Tidak ada title"

    # Ambil data
    elements = soup.find_all(
        ["h1", "h2", "h3", "h4", "p", "li", "a"]
    )

    data = []

    for element in elements:

        text = element.get_text(
            " ",
            strip=True
        )

        if text:

            # Kalau link, ambil URL-nya juga
            if element.name == "a":

                href = element.get("href", "")

            else:

                href = ""

            data.append({
                "Jenis": element.name.upper(),
                "Isi": text,
                "Link": href
            })

    return {
        "title": title,
        "url": url,
        "data": data
    }


def save_to_files(data):

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    df = pd.DataFrame(data["data"])

    if df.empty:
        raise ValueError(
            "Tidak ada data yang berhasil diambil."
        )

    # ==========================
    # CSV
    # ==========================

    csv_path = os.path.join(
        OUTPUT_FOLDER,
        "hasil_scrape.csv"
    )

    df.to_csv(
        csv_path,
        index=False,
        encoding="utf-8-sig"
    )

    # ==========================
    # EXCEL
    # ==========================

    excel_path = os.path.join(
        OUTPUT_FOLDER,
        "hasil_scrape.xlsx"
    )

    with pd.ExcelWriter(
        excel_path,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Hasil Scrape"
        )

        worksheet = writer.sheets["Hasil Scrape"]

        # Aktifkan filter
        worksheet.auto_filter.ref = (
            worksheet.dimensions
        )

        # Freeze header
        worksheet.freeze_panes = "A2"

        # Atur lebar kolom
        worksheet.column_dimensions["A"].width = 15
        worksheet.column_dimensions["B"].width = 80
        worksheet.column_dimensions["C"].width = 60

    return csv_path, excel_path