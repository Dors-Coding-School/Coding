from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", size=50)
        # Create the Heading
        self._pdf.cell(w=0, h=60, txt="CS50 Shirtificate",
                       new_x="LMARGIN", new_y="NEXT", align="C")
        # Create the Image
        self._pdf.image("shirtificate.png", w=self._pdf.epw,
                        alt_text="CS50 Shirtificate")
        # Create the Text in the Image
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")
    # Save the changes
    def save(self, name):
        self._pdf.output(name)

#Get user's name
name = input("Name: ")
# Create pdf
pdf = PDF(name)
# Create output file
pdf.save("shirtificate.pdf")
