import qrcode
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
style = Style(theme='flatly')
style.theme_use()

#generate QR main function
def generate_QR():
    text = text_entry.get()

    qr = qrcode.QRCode(version=1, box_size=10, border=10)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    #display the qr code in GUI
    img = img.resize((300,300))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.configure(image=img_tk)
    qr_label.image = img_tk

#Text input field for the text
text_label = ttk.Label(master=root, text="Enter the text or URL:")
text_label.pack(pady=10)
text_entry = ttk.Entry(master=root, width=50)
text_entry.pack()

#create a button to generate the QR code
generate_button = ttk.Button(master=root, text="Generate QR", command=generate_QR, style='success.TButton')
generate_button.pack(pady=10)

#display QR
qr_label = ttk.Label(master=root)
qr_label.pack(pady=10)

root.mainloop()