from fpdf import FPDF, XPos, YPos


def main():
    name = input("Name: ")
    make_shirtificate(name)


def make_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    image_width = 150
    x = (210 - image_width) / 2
    pdf.image("shirtificate.png", x=x, y=40, w=image_width)

    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 90)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
