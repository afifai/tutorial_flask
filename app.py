from flask import Flask, render_template
app = Flask(__name__)

konten = [
    {
        'penulis': 'Afif A. Iskandar',
        'judul': 'Postingan Pertama',
        'sinopsis': 'Ini adalah postingan pertama',
        'isi': 'Ini adalah isi dari postingan pertama',
        'tanggal': '12 Desember 2020',
        'jam': '16.00'
    },
    {
        'penulis': 'NgodingPython',
        'judul': 'Tutorial Flask',
        'sinopsis': 'Ini adalah tutorial flask',
        'isi': 'Ini adalah isi dari tutorial flask',
        'tanggal': '13 Desember 2020',
        'jam': '18.00'
    }
]

@app.route('/')
def home():
    return render_template('home.html', konten=konten, judul='Beranda')

@app.route('/tentang/')
def tentang():
    return render_template('tentang.html', judul='Tentang')

if __name__ == '__main__':
    app.run(debug=True)
